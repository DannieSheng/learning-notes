## [The Course](https://www.udemy.com/course/the-ultimate-mysql-bootcamp-go-from-sql-beginner-to-expert/)

### Slides:
https://webdev.slides.com/coltsteele/first-5-minutes-of-sql

### What is a Database?
A structured set of computerized data with an accessible interface  
1. A collection of data.
2. A method for accessing and manipulating the data. 

`mysql -u root -p`  

`show databases;`

The general command for creating a database:
`CREATE DATABASE <database_name>;`

To drop a database:
`DROP DATABASE <database-name>;`

To use a database:
`USE <database-name>;`

Creating tables
`CREATE TABLE <tablename>
   (
      column_name data_type,
      column_name data_type
   )
`

To show tables
`SHOW TABLES`
`SHOW COLUMNS FROM <tablename>;`
`DESCRIBE tablename`
`DESC tablename`

To delete tables
`DROP TABLE <tablename>;`

Adding data to tables
`INSERT INTO <tablename> (column_name1, column_name2) VALUES (value1, value2);`

### CRUD:  
Create  
Read  
Update  
Delete  


### [Data types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)
- Numeric Types:
   - INT: A whole number, with a max (signed) value of 2147483647 (32 bit)
   - SMALLINT
   - TINYINT
   - MEDIUMINT
   - BIGINT
   - DECIMAL
   - NUMERIC
   - FLOAT
   - DOUBLE
   - BIT
- String Types
   - CHAR
   - VARCHAR: A variable-length string
   - BLOB
   - TINYBLOB
   - MEDIUMBLOB
   - LONGBLOB
   - TEXT
   - TINYTEXT
   - MEDIUMTEXT
   - LONGTEXT
   - ENUM
- Data Types
   - DATE
   - DATETIME
   - TIMESTAMP
   - TIME
   - YEAR