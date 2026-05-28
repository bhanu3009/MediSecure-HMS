CREATE DATABASE PRATICES;

USE PRATICES;

CREATE table costumer(
    cust_name VARCHAR(100),
    cust_id INT,
    is_active BOOLEAN
);

create table ACCOUNT(
    acc_id INT,
    cus_id INT,
    balance DECIMAL(10,2),
    CREATED_AT_DATE DATETIME
);

INSERT INTO costumer(cust_name,cust_id,is_active) VALUES
("BHANU",1001,TRUE),
("SATHISH",2001,FALSE)
