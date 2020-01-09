SELECT *
FROM bank.client
where district_id =1
order by client_id asc
LIMIT 5;

SELECT *
from bank.client
where district_id = 72
order by client_id desc
limit 1;

select *
from bank.loan
order by amount asc
limit 3;

select distinct status
from bank.loan
order by status asc;

select 
	loan_id
from bank.loan
order by payments desc
limit 1;

select
	account_id,
    amount
from bank.loan
order by account_id asc
limit 5;

select
	account_id
from bank.loan
where duration = 60
order by amount asc
limit 5;

select distinct k_symbol
from bank.`order`
limit 5;

select
	order_id
from bank.`order`
where account_id = 34;

select distinct
	account_id
from bank.`order`
where order_id >= 29540 AND order_id <= 29560;

select distinct
	amount
from bank.`order`
where account_to = 30067122;

select
	trans_id, 
    `date`, 
    `type`,
    amount
from bank.trans
where account_id = 793
order by `date` desc
limit 10;