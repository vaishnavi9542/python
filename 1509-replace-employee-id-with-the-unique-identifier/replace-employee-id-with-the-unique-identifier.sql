# Write your MySQL query statement below
select unique_id,name from Employees e left join EmployeeUNI em on e.id=em.id;