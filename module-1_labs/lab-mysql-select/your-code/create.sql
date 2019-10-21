USE lab_mysql;

Insert into Invoices (ID, Invoice_Number, `Date`, Car, Customer, Sales_Person)
Values
(0, 852399038, 22-08-2018, 0, 1, 3),
(1, 731166526, 31-12-2018, 3, 0, 5),
(2, 271135104, 22-01-2019, 2, 2, 7);

select *
from lab_mysql.invoices;