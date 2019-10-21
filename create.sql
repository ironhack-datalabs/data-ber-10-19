USE lab_mysql;

CREATE TABLE cars (VIN VARCHAR(255), manufacturer VARCHAR(255), model VARCHAR(255), year YEAR(4), color VARCHAR(255));

CREATE TABLE customers (customer_ID VARCHAR(255), name VARCHAR(255), phone_number VARCHAR(255), email VARCHAR(255), address VARCHAR(255), city VARCHAR(255), state VARCHAR(255), country VARCHAR(255), zip VARCHAR(255));

CREATE TABLE salesperson (staff_id VARCHAR(255), name VARCHAR(255), store VARCHAR(255));

CREATE TABLE invoices (invoice_number VARCHAR(255), date DATE, car VARCHAR(255), customer VARCHAR(255), salesperson VARCHAR(255));