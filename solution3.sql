
# Challenge 1 - Most Profiting Authors

# Step 1: Calculate the royalties of each sales for each author

SELECT
	au_id																	AS Author_ID,
	ta.title_id																AS Title_ID,
	tit.price * sal.qty * (tit.royalty / 100) * (ta.royaltyper / 100)		AS Sales_Royalty
FROM titleauthor ta
	INNER JOIN titles tit
	ON ta.title_id = tit.title_id
	INNER JOIN sales sal
	ON tit.title_id = sal.title_id
ORDER BY ta.title_id, au_id;
	
# Step 2: Aggregate the total royalties of each sales for each author

SELECT
	au_id,
	temporar.title_id,
	SUM(Royalties)	AS Royalties 
FROM 
(
		SELECT
			au_id,
			ta.title_id,
			tit.price * sal.qty * (tit.royalty / 100) * (ta.royaltyper / 100) AS Royalties
		FROM titleauthor ta
			INNER JOIN titles tit
				ON ta.title_id = tit.title_id
			INNER JOIN sales sal
				ON tit.title_id = sal.title_id
		ORDER BY ta.title_id, au_id
) AS temporar

GROUP BY au_id, title_id
ORDER BY Royalties DESC;

# Step 3: Calculate the total profits of each author

SELECT
	au_id AS 'Author ID',
	SUM(temporar2.advance + Royalties) AS Profits FROM 
(
		SELECT
	au_id,
	temporar.title_id,
	temporar.advance,
	SUM(Royalties)	AS Royalties 
	FROM 
	(
		SELECT
			au_id,
			ta.title_id,
			advance,
			tit.price * sal.qty * (tit.royalty / 100) * (ta.royaltyper / 100) AS Royalties
		FROM titleauthor ta
			INNER JOIN titles tit
				ON ta.title_id = tit.title_id
			INNER JOIN sales sal
				ON tit.title_id = sal.title_id
		ORDER BY ta.title_id, au_id
	) AS temporar
	GROUP BY au_id, title_id
) AS temporar2
GROUP BY au_id
ORDER BY Profits DESC
LIMIT 3;



# Challenge 2 - Alternative Solution


