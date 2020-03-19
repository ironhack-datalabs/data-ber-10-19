
-- Challenge 1

SELECT 
	client_id
FROM bank.client
WHERE district_id =1
LIMIT 5;


-- Challenge 2

SELECT 
	client_id
FROM bank.client
WHERE district_id =72
ORDER BY client_id DESC
LIMIT 1;


-- Challenge 3

DESC loan;

SELECT 
	amount
FROM bank.loan
ORDER BY amount
LIMIT 3;


-- Challenge 4

SELECT 
	loan.status
FROM bank.loan
GROUP BY loan.status
ORDER BY loan.status;

-- Challenge 5
DESC loan;

-- highest payment
SELECT 
	loan_id,
	payments
FROM  bank.loan
ORDER BY payments DESC
LIMIT 10;	

-- lowest payment
SELECT 
	loan_id,
	payments
FROM  bank.loan
ORDER BY payments 
LIMIT 1;	

-- Challenge 6
SELECT 
	account_id,
	amount
FROM bank.loan
ORDER BY account_id
LIMIT 5;

-- Challenge 7

SELECT
	account_id
FROM bank.loan
WHERE 	duration = 60
ORDER BY amount
LIMIT 5;

-- Challenge 8

SELECT 
	k_symbol
FROM bank.order
GROUP BY  k_symbol
ORDER BY k_symbol;

-- Challenge 9

SELECT
	order_id
FROM bank.order
WHERE account_id = 34;

-- Challenge 10

SELECT 
	account_id
FROM bank.order
WHERE 
	order_id >= 29540
	AND order_id <= 29560
GROUP BY account_id
ORDER BY account_id;

-- Challenge 11

SELECT 
	amount
FROM bank.order
WHERE 
	account_to = 30067122;
	
-- Challenge 12 

SELECT 
	trans_id,
	trans.date,
	trans.type,
	amount
FROM bank.trans
WHERE account_id = 793
ORDER BY trans.date DESC
LIMIT 10;