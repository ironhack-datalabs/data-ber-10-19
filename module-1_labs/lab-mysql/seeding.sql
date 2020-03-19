
	
INSERT INTO stores (store_id,store_city)
VALUES
	(20191,'Madrid'),
	(20183, 'New York'),
	(20182, 'Amstardam'),
	(20181, 'Berlin'),
	(20172,'Paris'),
	(20171, 'Miami'),
	(20162, 'Barcelona'),
	(20161, 'Mexico City'),
	(20151, 'São Paulo');

INSERT INTO cars (VIN, manufacturer, model,manu_year,color,store_id)
VALUES
    ('3K096I98581DHSNUP', 'Volkswagen', 'Tiguan',2019, 'Blue',20191),
    ('ZM8G7BEUQZ97IH46V', 'Peugeot', 'Rifter', 2019, 'Red',20191),
    ('RKXVNNIHLVVZOUB4M', 'Ford', 'Fusion', 2018, 'White',20191),
    ('HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', 2018, 'Silver',20191),
    ('DAM41UDN3CHU2WVF6', 'Volvo', 'V60', 2019, 'Gray',20191),
    ('DAM41UDN3CHU2WVF6', 'Volvo', 'V60 Cross Country', 2019,'Gray',20191)
;

INSERT INTO customers (customer_id, customer_fname, customer_lname, phone_number, address, city, state, country, postel_code)
VALUES
	(10001,'Pablo','Picasso','+34 636 17 63 82','Paseo de la Chopera,14','Madrid','Madrid','Spain',28045),
	(20001,'Abraham','Lincoln','+1 305 907 7086',	'120 SW 8th St','Miami',	'Florida','United States',	33130),
	(30001,'Napoléon','Bonaparte','+33 1 79 75 40 00','40 Rue du Colisée','Paris','Île-de-France','France',75008);


INSERT INTO salespersons (staff_id,staff_name,store_id)
VALUES
	(00001, 'Petey Cruiser',	20191),
	(00002, 'Anna Sthesia', 20162),
	(00003, 'Paul Molive'	, 20181),
	(00004, 'Gail Forcewind', 20172),
	(00005, 'Paige Turner', 20171),
	(00006,'Bob Frapples', 20161),
	(00007,'Walter Melon',20182),
	(00008, 'Shonda Leer', 20151);
	
	
INSERT INTO invoices (invoice_no,invoice_date,store_id, car_id, customer_id, staff_id)
VALUES
	(852399038, '2018-08-22 00:00:00', 20181, 13, 1, 3),
	(731166526, '2018-12-31 00:00:00', 20171, 15, 1, 5),
	(271135104, '2019-01-22 00:00:00', 20182, 18, 2, 7);
