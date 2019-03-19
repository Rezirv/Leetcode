# Write your MySQL query statement below
delete from Person
where Id not in (select min(Id) from (select * from Person) as a group by Email having count(Email)>1) and Email in (select Email from (select * from Person) as a group by Email having count(Email)>1)