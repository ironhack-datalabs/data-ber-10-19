USE publications;

# Challenge 1 - Who Have Published What At Where

SELECT
	aut.au_id 						AS author_id,
	aut.au_lname					AS last_name,
	aut.au_fname					AS first_name,
	tit.title						AS title,
	pub.pub_name					AS publisher
FROM authors aut
	INNER JOIN titleauthor ta
		ON aut.au_id = ta.au_id
	INNER JOIN titles tit
		ON tit.title_id = ta.title_id
	INNER JOIN publishers pub
		ON pub.pub_id = tit.pub_id;
		
		

# Challenge 2 - Who Have Published How Many At Where 

SELECT 
	aut.au_id 						AS author_id,
	aut.au_lname					AS last_name,
	aut.au_fname					AS first_name,
	COUNT(ta.title_id)				AS TITLE_C,
	pub.pub_name					AS publisher
FROM authors aut
	INNER JOIN titleauthor ta
		ON aut.au_id = ta.au_id
	INNER JOIN titles tit
		ON tit.title_id = ta.title_id
	INNER JOIN publishers pub
		ON pub.pub_id = tit.pub_id
GROUP BY aut.au_id, pub.pub_id
ORDER BY author_id DESC;


# Challenge 3 - Best Selling Authors

SELECT
	aut.au_id 						AS author_id,
	aut.au_lname					AS last_name,
	aut.au_fname					AS first_name,
	SUM(sal.qty)					AS total
FROM authors aut
	INNER JOIN titleauthor ta
		ON aut.au_id = ta.au_id
	INNER JOIN sales sal
		ON sal.title_id = ta.title_id
GROUP BY author_id
ORDER BY total DESC
LIMIT 3;

# Challenge 4 - Best Selling Authors Ranking

SELECT
	aut.au_id 						AS author_id,
	aut.au_lname					AS last_name,
	aut.au_fname					AS first_name,
	SUM(sal.qty)					AS total
FROM authors aut
	INNER JOIN titleauthor ta
		ON aut.au_id = ta.au_id
	INNER JOIN sales sal
		ON sal.title_id = ta.title_id
GROUP BY author_id
HAVING total >= 0
ORDER BY total DESC;