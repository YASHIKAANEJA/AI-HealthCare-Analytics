-- SQL QUERIES

-- Problem: Hospital management wants to know when and where the hospital is under the most pressure.

USE DATABASE HOSPITAL_DB;
USE SCHEMA HOSPITAL_DB_SCHEMA;

-- QUESTION 1 Busiest day?
SELECT 
    DATE(ENCOUNTER_START) AS encounter_date,
    COUNT(*) AS total_encounters
FROM encounters
GROUP BY DATE(ENCOUNTER_START)
ORDER BY total_encounters DESC
LIMIT 1;
-- INSIGHT = 6 FEBUARY 2014 was the busiest day of the hospital with 57 encounters in one day only.

-- BUSIEST YEAR?
select 
    year(ENCOUNTER_START) as encounter_year,
    count(*) as total_encounters
from encounters
group by year(ENCOUNTER_START)
order by total_encounters desc limit 1;
-- INSIGHT = 2014 was the busiest year in the range of 10 years 2011-2022 with over 3885 encounters.

-- BUSIEST YEAR AND MONTH BOTH?
select 
    year(ENCOUNTER_START) as encounter_year,
    MONTH(ENCOUNTER_START) as encounter_month,
    count(*) as total_encounters
from encounters
group by year(ENCOUNTER_START),month(ENCOUNTER_START)
order by total_encounters desc limit 1;
-- INSIGHT = FEBUARY 2014 WAS THE BUSIEST AMONG ALL THE YEARS

-- Busiest hour?
SELECT 
   HOUR(ENCOUNTER_START) AS encounter_hour,
   count(*) as total_encounters
from encounters
group by HOUR(ENCOUNTER_START)
order by total_encounters desc;
-- INSIGHT = 2 AM TIME is the busiest of all 

-- Emergency vs routine encounters?
SELECT ENCOUNTERCLASS,
COUNT(*) AS total_encounters
FROM encounters 
group by ENCOUNTERCLASS
order by total_encounters desc;

-- Average encounter duration?


-- Total procedure cost = 105517711
select ROUND(SUM(BASE_COST)) as total_procedure_cost from procedures;

-- Average Procedure Cost = 2212
select ROUND(AVG(BASE_COST)) AS average_procedure_cost from procedures;

--Total claim cost = 101514376
select ROUND(SUM(TOTAL_CLAIM_COST)) AS total_claim_cost from encounters;

--Average claim cost = 3640
select ROUND(AVG(TOTAL_CLAIM_COST)) as average_claim_cost from encounters;

-- Cost by procedure ?
SELECT 
    DESCRIPTION AS Procedure,
    SUM(BASE_COST) AS Total_Procedure_Cost
FROM procedures
GROUP BY DESCRIPTION
ORDER BY Total_Procedure_Cost DESC limit 5;
-- INSIGHT = Electrical cardioversion is the most Expensive procedure out of all

-- Cost by encounter type ?
