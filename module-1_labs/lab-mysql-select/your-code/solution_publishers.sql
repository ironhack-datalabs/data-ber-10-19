USE publications;

-- Challenge 1

select
	a.au_id as Author_ID,
    a.au_lname as Last_Name,
    a.au_fname as First_Name,
    tt.title as Title,
    p.pub_name as Publisher
from authors a
	Inner Join titleauthor t
    on a.au_id = t.au_id
    Inner Join titles tt
    on tt.title_id = t.title_id
    Inner Join publishers p
    on p.pub_id = tt.pub_id;
    
    -- Challenge 2
    
select
	distinct(a.au_id) as Author_ID,
    a.au_lname as Last_Name,
    a.au_fname as First_Name,
    tt.title as Title,
    p.pub_name as Publisher,
    count(tt.title_id) as Title_Count
from authors a
	Inner Join titleauthor t
    on a.au_id = t.au_id
    Inner Join titles tt
    on tt.title_id = t.title_id
    Inner Join publishers p
    on p.pub_id = tt.pub_id
group by a.au_id, p.pub_name
order by a.au_id desc;

-- Challenge 3

select
	a.au_id as Author_ID,
    a.au_lname as Last_Name,
    a.au_fname as First_Name,
    sum(s.qty) as TOTAL
from authors a
	Inner Join titleauthor t
    on a.au_id = t.au_id
    Inner Join sales s
    on t.title_id = s.title_id
group by a.au_id
order by TOTAL desc
Limit 3;

-- Challenge 4

select
	a.au_id as Author_ID,
    a.au_lname as Last_Name,
    a.au_fname as First_Name,
    sum(IFNULL(s.qty, 0)) as TOTAL
from authors a
	Left Join titleauthor t
    on a.au_id = t.au_id
    Left Join sales s
    on t.title_id = s.title_id
group by a.au_id
order by TOTAL desc;
