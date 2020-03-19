USE lab_mysql;

CREATE TABLE IF NOT EXISTS stores (
  	store_id 			int(5) 				AUTO_INCREMENT,
  	store_city 			varchar(20)		NOT NULL,
  	PRIMARY KEY (store_id)
);

CREATE TABLE IF NOT EXISTS cars (
	ID 					int				AUTO_INCREMENT,
  	VIN 				varchar(50) 	NOT NULL, 
	manufacturer 	    varchar(40) 	NOT NULL,
  	model 			    varchar(20)	    NOT NULL,
	manu_year 		    year(4)			NOT NULL DEFAULT (NOW()),									
	color 				varchar(10)	    DEFAULT 'Unknown',
	store_id			int(5)			NOT NULL,
	PRIMARY KEY  (ID),
	FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE IF NOT EXISTS customers (
	ID								int					AUTO_INCREMENT,
  	customer_id 				int (5)				NOT NULL,
 	customer_fname 		varchar(20)		NOT NULL,
 	customer_lname		varchar(40)		NOT NULL,
 	phone_number 		varchar(20)		NOT NULL,
 	email 				varchar(50)		DEFAULT ('-'),
  	address 			varchar(40)		NOT NULL,
  	city 				varchar(20)		NOT NULL,
  	state_or_province 	varchar(20)		NOT NULL,
  	country 			varchar(20)		NOT NULL,
  	postel_code 		int(5)			NOT NULL,
  	PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS  salespersons (
	ID 					int				AUTO_INCREMENT,
  	staff_id 			int(5)			NOT NULL,
  	staff_name 		    varchar(40)	    NOT NULL,
	store_id			int(20)			NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (store_id) REFERENCES stores(store_id)
 );
 
 
CREATE TABLE IF NOT EXISTS invoices (
	ID 					int				AUTO_INCREMENT,
	invoice_no 		    int(9)			NOT NULL,
  	invoice_date 	    datetime		DEFAULT NOW(),
  	store_id 			int(20)			NOT NULL,
  	car_id 				int,
  	customer_id 		int				NOT NULL,
  	staff_id 			int 			NOT NULL,
  	PRIMARY KEY (ID),
  	FOREIGN KEY (customer_id) REFERENCES customers(ID),
  	FOREIGN KEY (car_id) REFERENCES cars(ID),
  	FOREIGN KEY (staff_id) REFERENCES salespersons(ID)
);