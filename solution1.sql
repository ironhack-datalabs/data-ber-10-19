USE bank;

# 1

SELECT 
	DISTINCT district_id as unique_distinct,
	COUNT(client_id)
FROM client
WHERE district_id < 10
GROUP BY district_id
ORDER BY district_id ASC;

# 2

SELECT
	DISTINCT type,
	COUNT(type) AS frequency
FROM card
GROUP BY type
ORDER BY frequency DESC;

# 3

SELECT 
	accoun_id,
	SUM(amount) AS money
FROM loan
GROUP BY account_id
ORDER BY money DESC
LIMIT 10;

# 4

SELECT 
	date,
	COUNT(loan_id) AS number
FROM loan
GROUP BY date
ORDER BY 1,2 ASC;

# 5 

SELECT
	date,
	duration,
	COUNT(loan_id) AS issued
FROM loan
WHERE date >= 971201 AND date <= 971231
GROUP BY date, duration;

# 6

SELECT
	account_id,
	type,
	SUM(amount) AS total_amount
FROM trans
WHERE 
	account_id = 396
GROUP BY type;

# 7

SELECT
	account_id,
	CASE
		WHEN type = 'PRIJEM'
			THEN 'INCOMING'
		WHEN type = 'VYDAJ'
			THEN 'OUTGOING'
		ELSE NULL
	END								AS transaction_type,
	CAST(SUM(amount) AS SIGNED)		AS total_amount
FROM trans
WHERE 
	account_id = 396
GROUP BY type;

# 8

SELECT
	account_id,
	FLOOR(
		SUM(
			CASE 
				WHEN type = 'PRIJEM' 
					THEN amount 
						ELSE 0 
							END))	AS incoming,
	FLOOR(
		SUM(
			CASE 
				WHEN type = 'VYDAJ' 
					THEN amount 
						ELSE 0 
							END))	AS outgoing,
	FLOOR(
		SUM(
			CASE 
				WHEN type = 'PRIJEM' 
					THEN amount 
						ELSE 0 
							END)) 
							- 
	FLOOR(
		SUM(
			CASE 
				WHEN type = 'VYDAJ' 
					THEN amount 
						ELSE 0 
							END))	AS difference
FROM trans
WHERE 
	account_id = 396;
	
# 9

SELECT
	account_id,
	FLOOR(
		SUM(
			CASE 
				WHEN type = 'PRIJEM' 
					THEN amount 
						ELSE 0 
							END)) 
							- 
	FLOOR(
		SUM(
			CASE 
				WHEN type = 'VYDAJ' 
					THEN amount 
						ELSE 0 
							END))	AS difference
FROM trans
GROUP BY account_id
ORDER BY difference DESC
LIMIT 10;