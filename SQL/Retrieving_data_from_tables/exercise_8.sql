/*
Write a query which will retrieve the value of salesman id of all salesmen, 
getting orders from the customers in orders table without any repeats.
*/

SELECT DISTINCT salesman_id
FROM orders;