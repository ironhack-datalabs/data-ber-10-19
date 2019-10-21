# 1
SELECT client_id
FROM bank.client
WHERE district_id = 1
LIMIT 5;


# 2

SELECT client_id
FROM bank.client
WHERE district_id = 72
ORDER BY client_id DESC
LIMIT 1;

# 3

SELECT amount
FROM bank.loan
ORDER BY amount
LIMIT 3;

# 4

SELECT DISTINCT status
FROM bank.loan
ORDER BY status ASC;

# 5
SELECT loan_id
FROM bank.loan
ORDER BY payments DESC
LIMIT 1;

# 6

SELECT 
	account_id,
	amount
FROM bank.loan
ORDER BY account_id ASC
LIMIT 5;

# 7

SELECT account_id
FROM bank.loan
WHERE duration = 60
ORDER BY amount
LIMIT 5;

# 8

SELECT DISTINCT k_symbol
FROM bank.order
ORDER BY k_symbol ASC;

# 9

SELECT order_id
FROM bank.order
WHERE account_id = 34;

# 10

SELECT DISTINCT account_id
FROM bank.order
WHERE 
	order_id >= 29540
	AND order_id <= 29560
LIMIT 5;

# 11

SELECT amount
FROM bank.order
WHERE account_to = 30067122;

# 12

SELECT trans_id, date, type, amount
FROM bank.trans
WHERE account_id = 793
ORDER BY date DESC
LIMIT 10;