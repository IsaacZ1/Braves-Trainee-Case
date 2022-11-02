--1

select name from WAR 
where year in ("2002", "2003")
and name in
(select name from WAR
where (year = "2002" and war > 3 and war != "NULL") or (year = "2003" and war > 3 and war != "NULL")
Union
Select name from WAR 
where year in ("2002", "2003") 
group by name
having SUM(WAR) > 5) 
group by name
order by SUM(WAR) desc

