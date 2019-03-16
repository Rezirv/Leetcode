# Write your MySQL query statement below
select IFNULL((select distinct(Salary)#ifnull 判空
               from Employee
               order by Salary desc
               limit 1,1 #第一数表示跳过几个数，第二个表示读取几个数
),null) as SecondHighestSalary

