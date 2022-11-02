--2
select 
name,
Case 
    When war >= 1.0 then 1 
    else 0
    end as war_1,
Case 
    when war >= 2.0 then 1
    else 0
    end as war_2,
Case
    when war >= 3.0 then 1
    else 0
    end as war_3,
war

from PERF 
where year = 2018 and org = "ATL" and level like '%mlb%'





