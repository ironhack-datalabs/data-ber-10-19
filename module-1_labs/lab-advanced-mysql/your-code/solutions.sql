-- Challenge 1
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