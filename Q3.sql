--3
select count(*) as "numPA", sum(zero) as "0 and 2", sum(one) as "1 and 2", sum(two) as "2 and 2"
from(
select gamedate, inning, PA_of_inning
, MAX(Case when strikes = '2' and balls = '0' then 1 else 0 end) as "zero"
, MAX(Case when strikes = '2' and balls = '1' then 1 else 0 end) as "one",
MAX(Case when strikes = '2' and balls = '2' then 1 else 0 end) as "two"
from PITCHBYPITCH
where PitcherName = "Jackson, Luke" 
--and strikes = 2
group by gamedate, inning, PA_of_inning
having max(strikes) = '2' and sum(is_strikeout) = 0
) as X

