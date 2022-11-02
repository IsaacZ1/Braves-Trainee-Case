import requests
import json
import pandas as pd
response = requests.get("https://statsapi.mlb.com/api/v1/stats?stats=season&group=pitching&playerPool=all&season=2018&teamId=144")
api = response.json()
api = dict(api)
data = api["stats"]
data = data[0]

playerData = data["splits"]

df = pd.DataFrame()
length = len(playerData)
names = []
ids = []
for i in range(length):
	playerStats = playerData[i]["stat"]
	df = df.append(playerStats, ignore_index=True)
	name = playerData[i]['player']['fullName']
	names.append(name)
	the_id = playerData[i]['player']['id']
	ids.append(the_id)
df["Player Name"] = names
df["Player ID"] = ids
df.set_index(["Player Name", "Player ID"], inplace = True)
noNeed = ["gamesStarted", "atBats", "groundOuts", "airOuts", "runs", "baseOnBalls", "intentionalWalks", "hitByPitch", "avg", "obp", "slg", "ops", "caughtStealing", "stolenBases", "stolenBasePercentage", "groundIntoDoublePlay", "era", "wins", "losses", "saves", 'saveOpportunities', 'holds', 'blownSaves','earnedRuns', 'whip', 'gamesPitched', 'completeGames', 'shutouts', 'strikePercentage', 'pitchesPerInning','hitBatsmen', 'balks', 'wildPitches', 'pickoffs', 'totalBases','groundOutsToAirouts', 'winPercentage', 'gamesFinished', 'strikeoutWalkRatio', 'strikeoutsPer9Inn','walksPer9Inn', 'hitsPer9Inn', 'runsScoredPer9', 'homeRunsPer9','inheritedRunners', 'inheritedRunnersScored', 'catchersInterference','sacBunts', 'sacFlies']
df.drop(labels = noNeed, axis = 1, inplace = True)
#singles
df = df.assign(singles = df['hits'] - df['homeRuns'] - df["doubles"] - df["triples"])
#balls
df = df.assign(balls = df['numberOfPitches'] - df['strikes'])
df.to_csv('Braves.csv')


