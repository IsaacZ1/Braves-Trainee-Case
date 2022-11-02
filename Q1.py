import requests
import json
import pandas as pd

#call the API to retrieve the data
response = requests.get("https://statsapi.mlb.com/api/v1/stats?stats=season&group=pitching&playerPool=all&season=2018&teamId=144")
#transform and clean the data to make it manipulatable
api = response.json()
api = dict(api)
data = api["stats"]
data = data[0]
playerData = data["splits"]

#create a dataframe to store the data in a cleaner/more oranized way
df = pd.DataFrame()
#creates list for names and ids to capture in the for loop
names = []
ids = []
#This for loop goes into the datastructure containing the stats of the players and puts them into the Data frame as well as astract the names and ids 
for i in range(len(playerData)):
	playerStats = playerData[i]["stat"]
	df = df.append(playerStats, ignore_index=True)
	name = playerData[i]['player']['fullName']
	names.append(name)
	the_id = playerData[i]['player']['id']
	ids.append(the_id)
#add names and ids to the data frame
df["Player Name"] = names
df["Player ID"] = ids

#sets names and ids to be the index
df.set_index(["Player Name", "Player ID"], inplace = True)

#removes the data that is not needed to recreate the PITCHBYPITCH dataframe
noNeed = ["gamesStarted", "atBats", "groundOuts", "airOuts", "runs", "baseOnBalls", "intentionalWalks", "hitByPitch", "avg", "obp", "slg", "ops", "caughtStealing", "stolenBases", "stolenBasePercentage", "groundIntoDoublePlay", "era", "wins", "losses", "saves", 'saveOpportunities', 'holds', 'blownSaves','earnedRuns', 'whip', 'gamesPitched', 'completeGames', 'shutouts', 'strikePercentage', 'pitchesPerInning','hitBatsmen', 'balks', 'wildPitches', 'pickoffs', 'totalBases','groundOutsToAirouts', 'winPercentage', 'gamesFinished', 'strikeoutWalkRatio', 'strikeoutsPer9Inn','walksPer9Inn', 'hitsPer9Inn', 'runsScoredPer9', 'homeRunsPer9','inheritedRunners', 'inheritedRunnersScored', 'catchersInterference','sacBunts', 'sacFlies']
df.drop(labels = noNeed, axis = 1, inplace = True)

#creates the singles value by taking hits and subtracting doubles, triples, and home runs
df = df.assign(singles = df['hits'] - df['homeRuns'] - df["doubles"] - df["triples"])

#creates the balls value by taking total pitches and subtracts strikes
df = df.assign(balls = df['numberOfPitches'] - df['strikes'])

#converts the dataframe to a CSV and exports it as a CSV file
df.to_csv('Braves.csv')


