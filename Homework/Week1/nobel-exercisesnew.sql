-- SQL Exercises
-- --------------------
-- Use the nobel database from class to answer the following questions.

-- 1. Select the nobel database.

USE nobel;

-- 2. List the tables.

SHOW TABLES;

-- 3. Select the first ten records from the laureate table.

SELECT *
FROM laureate
LIMIT 10;

-- 4. Find the birth and death dates for Albert Einstein.
SELECT laureate.birth_date, laureate.death_date, laureate.name
FROM laureate
WHERE name ='Albert Einstein';

-- 5. Find the Nobel Laureates who died in 2015 and whose name begins with 'Y'.

SELECT laureate.name, laureate.death_date
FROM laureate
WHERE name LIKE 'Y%' AND death_date LIKE '2015%';

-- 6. Find the last three Nobel Laureates born in 1900.

SELECT name, birth_date
FROM laureate
WHERE birth_date LIKE '1900%'
ORDER BY birth_date DESC
LIMIT 3;

-- 7. Find the number of Nobel Prizes awarded between 1950 and 1960.

SELECT COUNT(*)
FROM prize
WHERE (`year` >= '1950') and (`year` <= '1960');

-- 8. Find the number of Nobel Prizes awarded in each year.

SELECT year, COUNT(*)
FROM prize
GROUP BY year;


-- 9. In which year was the greatest number of Nobel Prizes awarded?

SELECT year, COUNT(*) as numyear
FROM prize
GROUP BY year
ORDER BY numyear DESC
LIMIT 1;



-- 10. What is the average number of Nobel Prizes awarded per year? Do we know how to do this yet?
-- must use select function twice 

SELECT  AVG(total)
FROM(	SELECT year , COUNT(*) AS total 
		FROM prize
		GROUP BY year)
AS Average;
-- name as average the outer selection


-- 11. In which years were more than fifteen Nobel Prizes awarded?
-- having is used becuase where cannot be used in aggregate functions 
SELECT year, COUNT(*) as ytotal
FROM prize
GROUP BY year HAVING  ytotal > 15;

-- 12. Who is the Nobel Laureate with the shortest name?

SELECT laureate.name 
FROM laureate
ORDER BY LENGTH(name) ASC
LIMIT 1;

-- 13. Which Nobel Laureate had the longest life? You might need to use IFNULL().

SELECT laureate.name, IFNULL(death_date - birth_date, 0)
FROM laureate
ORDER BY death_date - birth_date DESC
LIMIT 1;


-- 14. Which year has the most women Nobel Laureates?

SELECT year, sex, COUNT(*) 
FROM laureate
JOIN prize
ON laureate.id = prize.laureate_id
WHERE sex = 'F'
GROUP BY year;

-- 15. Which category has the most women Nobel Laureates?

SELECT year, category, COUNT(*) 
FROM laureate
JOIN prize
ON laureate.id = prize.laureate_id
WHERE sex = 'F'
GROUP BY category;

-- 16. What is the average number of Nobel Prizes awarded per year? SAME AS NUMBER 10
