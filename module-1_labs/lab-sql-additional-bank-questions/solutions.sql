-- Q1 Count the number of clients per gender

CREATE TEMPORARY TABLE client_gender (
    SELECT 
        disp.account_id                                     AS Account_ID,
        disp.type                                           AS Client_type,                       
        IF(LEFT((RIGHT(c.birth_number,4)),2)>12,'F','M')    AS Gender
    FROM client c
        JOIN disp 
        ON disp.client_id = c.client_id);
    

SELECT 
    cg.Gender   AS GENDER,
    COUNT(*)    AS COUNTNUM
FROM client_gender cg
GROUP BY Gender;    

-- Q2 Are there any accounts that have more than 2 linked clients?

CREATE TEMPORARY TABLE client_gender (
    SELECT 
        disp.account_id                                     AS Account_ID,
        disp.type                                           AS Client_type,                       
        IF(LEFT((RIGHT(c.birth_number,4)),2)>12,'F','M')    AS Gender
    FROM client c
        JOIN disp 
        ON disp.client_id = c.client_id);

SELECT
    COUNT(Client_type) AS LINKED_ACC
FROM client_gender cg
GROUP BY Account_ID
HAVING LINKED_ACC>2;


-- Q3 What is the average transaction amount for each region?

CREATE TEMPORARY TABLE account_region (
    SELECT 
        d.A3                    AS Region,
        FLOOR(AVG(t.amount))    AS AVG
    FROM account a
        JOIN district d
        ON  d.A1 = a.district_id
        JOIN trans t
        ON t.account_id = a.account_id
    GROUP BY 1
    ORDER BY 1
    LIMIT 100);

SELECT *
FROM account_region;


-- Q4 Based on the entire transaction volume (total amount), what's the percentage that was sent to another bank?



SELECT 
    operation                                   AS TRAN_TYPE,
    (COUNT(*)/(SELECT COUNT(*) FROM trans))     AS PERCENT
FROM trans
GROUP BY 1
HAVING TRAN_TYPE = 'PREVOD Z UCTU';




-- Q5 From which region do most of the clients that are account owners come from, that either have finished loan contracts that haven't been paid, or have running contracts but are in debt? Show the top 10 regions including the number of client that are owners. 




