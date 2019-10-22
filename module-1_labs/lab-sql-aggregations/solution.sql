USE bank;

-- 1.

select
    district_id,
    count(client_id)
from client
where district_id < 10
group by district_id
order by district_id asc;

-- 2.

select
	`type`,
    count(card_id) as Cards
from card
group by `type`
order by Cards desc;

-- 3.

select
	account_id,
	amount
from loan
group by account_id
order by amount desc
limit 10;

-- 4.

select
	`date`,
    count(loan_id)
from loan
where `date` < 930907
group by loan_id
order by `date` desc;

-- 5.

select
	`date`,
    duration,
    count(loan_id)
from loan
where 971130 <`date` and 980101 >`date`
group by `date`, duration
order by `date`, duration asc;

-- 6.

select
	account_id,
    `type`,
    sum(amount) as total_amount
from trans
where account_id = 396
group by `type`;

-- 7.

select
	account_id,
case
	when `type` = 'PRIJEM'
		then 'Incoming'
	when `type` = 'VYDAJ'
		then 'Outgoing'
end as transaction_type,
	floor(sum(amount)) as total_amount
from trans
where account_id = 396
group by `type`;

-- 8.

select
	account_id,
	floor(sum(IF(type = 'PRIJEM', amount, 0))) AS incoming_amount,
    floor(sum(IF(type = 'VYDAJ', amount, 0))) AS outgoing_amount,
    floor(sum(IF(type = 'PRIJEM', amount, 0))) - floor(sum(IF(type = 'VYDAJ', amount, 0))) as difference
from trans
where account_id = 396
group by 1;

-- 9.

select
	account_id,
    floor(sum(IF(type = 'PRIJEM', amount, 0))) - floor(sum(IF(type = 'VYDAJ', amount, 0))) as difference
from trans
group by 1
order by difference desc
limit 10;