# Write your MySQL query statement below
select name as Employee
from Employee as a
where  Salary > (select Salary
                from Employee as b
                where b.id = a.ManagerId)
