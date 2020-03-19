-- LAB MySQL Select 

-- Challenge 1
USE publications;

SELECT
	authors.au_id AS 'AUTHOR ID',
	authors.au_lname AS 'LAST NAME',
	authors.au_fname AS 'FIRST NAME',
	titles.title AS TITLE,
	publishers.pub_name AS PUBLISHER
FROM publications.authors
JOIN titleauthor 
	ON titleauthor.au_id = authors.au_id
JOIN titles
	ON titles.title_id = titleauthor.title_id
JOIN publishers
	ON titles.pub_id = publishers.pub_id
ORDER BY 1;

-- Challenge 2

SELECT
	authors.au_id AS 'AUTHOR ID',
	authors.au_lname AS 'LAST NAME',
	authors.au_fname AS 'FIRST NAME',
	publishers.pub_name AS PUBLISHER,
	COUNT(*)
FROM publications.authors
JOIN titleauthor 
	ON titleauthor.au_id = authors.au_id
JOIN titles
	ON titles.title_id = titleauthor.title_id
JOIN publishers
	ON titles.pub_id = publishers.pub_id
GROUP BY 1, 4
ORDER BY 1 DESC;


-- Challenge 3

SELECT
	authors.au_id AS 'AUTHOR ID',
	authors.au_lname AS 'LAST NAME',
	authors.au_fname AS 'FIRST NAME',
	SUM(sales.qty) AS TOTAL
FROM publications.authors
JOIN titleauthor 
	ON titleauthor.au_id = authors.au_id
JOIN sales
	ON titleauthor.title_id = sales.title_id
GROUP BY 1
ORDER BY 4 DESC
LIMIT 3;

-- Challenge 4

SELECT
	a.au_id AS 'AUTHOR ID',
	a.au_lname AS 'LAST NAME',
	a.au_fname AS 'FIRST NAME',
	IFNULL(SUM(s.qty),0) AS TOTAL
FROM publications.authors a
	LEFT JOIN titleauthor t
	ON t.au_id = a.au_id
	LEFT JOIN sales s
	ON t.title_id = s.title_id
GROUP BY 1
ORDER BY 4 DESC;



-- Bonus

SELECT *
FROM titles
LIMIT 10;

SELECT *
FROM titleauthor
LIMIT 10;

SELECT 
	a.au_id AS 'AUTHOR ID',
	a.au_lname AS 'LAST NAME',
	a.au_fname AS 'FIRST NAME',
	CONCAT('$',ROUND(SUM(t.advance+(t.ytd_sales*t.price*(t.royalty/100))),2)) AS PROFIT 
FROM publications.authors a
	JOIN titleauthor ta 
	ON ta.au_id = a.au_id
	JOIN titles t
	ON t.title_id = ta.title_id
GROUP BY 1
ORDER BY 4 DESC
LIMIT 3;