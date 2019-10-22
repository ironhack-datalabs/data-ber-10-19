USE lab_mysql;

-- Create cars table
create table cars (
    VIN varchar(100),
    manufacturer varchar(100),
    model varchar(100),
    year varchar(100),
    color varchar(100)
);

-- Create customers table
create table customers (
    customer_ID varchar(100),
    name varchar(100), 
    phone varchar(100), 
    email varchar(100), 
    address varchar(100), 
    city varchar(100), 
    state_province varchar(100), 
    country varchar(100), 
    zip_postal varchar(100)
);

-- Create salespersons table
create table salespersons (
    staff_ID varchar(100),
    name varchar(100),
    store varchar(100)
);

-- Create invoices table
create table invoices (
    invoice_number varchar(100),
    date varchar(100),
    car varchar(100),
    customer varchar(100),
    sales_Person varchar(100)
);