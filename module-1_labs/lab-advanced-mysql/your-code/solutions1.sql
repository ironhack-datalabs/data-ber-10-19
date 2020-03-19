-- Challenge 1
<<<<<<< HEAD
CREATE TEMPORARY TABLE royalty_sales (
SELECT
    s.title_id                                      AS Title_ID,
    ta.au_id                                        AS Author_ID,
    t.advance                                       AS Advance,
    ta.royaltyper                                   AS Royaltyper,
    (t.advance*ta.royaltyper/100)                   AS Splited_advance,
    SUM(t.price*s.qty*t.royalty/100*ta.royaltyper/100) AS Royalty_per_sale
FROM titles t
    JOIN sales s
    ON s.title_id = t.title_id
    JOIN titleauthor ta
    ON ta.title_id = t.title_id
GROUP BY 1,2
ORDER BY 5 DESC);

SELECT
    rs.Author_ID,
    a.au_lname,
    a.au_fname,
    ROUND(SUM(Splited_advance)+SUM(Royalty_per_sale),2) AS Profit
FROM royalty_sales rs
    JOIN authors a
    ON a.au_id = rs.Author_ID
GROUP BY 1
ORDER BY 4 DESC;




-- Challenge 3

CREATE TABLE most_profiting_authors (
    WITH royalty_sales AS (
        SELECT
        s.title_id                                      AS Title_ID,
        ta.au_id                                        AS Author_ID,
        t.advance                                       AS Advance,
        ta.royaltyper                                   AS Royaltyper,
        (t.advance*ta.royaltyper/100)                   AS Splited_advance,
        SUM(t.price*s.qty*t.royalty/100*ta.royaltyper/100) AS Royalty_per_sale
        FROM titles t
            JOIN sales s
            ON s.title_id = t.title_id
            JOIN titleauthor ta
            ON ta.title_id = t.title_id
        GROUP BY 1,2
        ORDER BY 5 DESC)
    SELECT
        rs.Author_ID  AS "Author ID",
        ROUND(SUM(Splited_advance)+SUM(Royalty_per_sale),2) AS Profits
    FROM royalty_sales rs
        JOIN authors a
        ON a.au_id = rs.Author_ID
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 3);


SELECT*
FROM most_profiting_authors;
=======

-- Step 1
select t.title_id, t.price, t.advance, t.royalty, s.qty, a.au_id, au_lname, au_fname, ta.royaltyper, (t.price * s.qty * t.royalty * ta.royaltyper / 10000) as ROYALTIES
from titles t
-- tables join
inner join sales s on s.title_id = t.title_id
inner join titleauthor ta on ta.title_id = s.title_id
inner join authors a on a.au_id = ta.au_id
-- order by
order by t.title_id, a.au_id;


-- Step 2
select title_id, au_id, au_lname, au_fname, advance, /* aggregate HERE! */ sum(ROYALTIES) as ROYALTIES from 
-- incorporate all in a temp table/sql-object
(
	select t.title_id, t.price, t.advance, t.royalty, s.qty, a.au_id, au_lname, au_fname, ta.royaltyper, (t.price * s.qty * t.royalty * ta.royaltyper / 10000) as ROYALTIES
	from titles t
	inner join sales s on s.title_id = t.title_id
	inner join titleauthor ta on ta.title_id = s.title_id
	inner join authors a on a.au_id = ta.au_id
) as tmp
-- group by
group by au_id, title_id
order by ROYALTIES desc;


-- Step 3
select au_id as "AUTHOR ID", au_lname as "LAST NAME", au_fname as "FIRST NAME", sum(advance + ROYALTIES) as PROFITS from 
-- incorporate previous table
(
	select title_id, au_id, au_lname, au_fname, advance, sum(ROYALTIES) as ROYALTIES from (
		select t.title_id, t.price, t.advance, t.royalty, s.qty, a.au_id, au_lname, au_fname, ta.royaltyper, (t.price * s.qty * t.royalty * ta.royaltyper / 10000) as ROYALTIES
		from titles t
		inner join sales s on s.title_id = t.title_id
		inner join titleauthor ta on ta.title_id = s.title_id
		inner join authors a on a.au_id = ta.au_id
	) as tmp
	group by au_id, title_id
) as tmp2
-- group by author ID
group by au_id
order by PROFITS desc
limit 3;


-- Challenge 2
drop temporary table if exists tmp1;

CREATE TEMPORARY TABLE tmp1
select t.title_id, a.au_id, (t.price * s.qty * t.royalty * ta.royaltyper / 10000) as sale_royalty
from titles t
inner join sales s on s.title_id = t.title_id
inner join titleauthor ta on ta.title_id = s.title_id
inner join authors a on a.au_id = ta.au_id
order by t.title_id, a.au_id;

drop temporary table if exists tmp2;

CREATE TEMPORARY TABLE tmp2
select title_id, au_id, sum(sale_royalty) as ROYALTIES
from tmp1
group by title_id, au_id;

select tmp2.au_id as "AUTHOR ID", a.au_lname as "LAST NAME", a.au_fname as "FIRST NAME", sum(t.advance + ROYALTIES) as PROFITS 
from tmp2
inner join titles t on t.title_id = tmp2.title_id
inner join authors a on a.au_id = tmp2.au_id
group by tmp2.au_id
order by PROFITS desc
limit 3;
>>>>>>> upstream/master
