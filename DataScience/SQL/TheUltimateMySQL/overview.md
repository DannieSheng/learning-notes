## [The Course](https://www.udemy.com/course/the-ultimate-mysql-bootcamp-go-from-sql-beginner-to-expert/)

### Slides:
https://webdev.slides.com/coltsteele/first-5-minutes-of-sql

### What is a Database?
A structured set of computerized data with an accessible interface  
1. A collection of data.
2. A method for accessing and manipulating the data. 

- Access from terminal  
`mysql -u root -p`  
  - Troubleshooting for `zsh: command not found: mysql`:  
    (optional)`touch ~/.bash_profile`  
  `open ~/.bash_profile`  
  add `export PATH=${PATH}:/usr/local/mysql/bi`, save and close  
  `source ~/.bash_profile`

`show databases;`

- The general command for creating a database:  
`CREATE DATABASE <database_name>;`

- To drop a database:  
`DROP DATABASE <database-name>;`

- To use a database:  
`USE <database-name>;`

- Creating tables  
`CREATE TABLE <tablename>
   (
      column_name data_type,
      column_name data_type
   )`

- To show tables  
`SHOW TABLES`
`SHOW COLUMNS FROM <tablename>;`
`DESCRIBE tablename`
`DESC tablename`

- To delete tables  
`DROP TABLE <tablename>;`

- Adding data to tables  
`INSERT INTO <tablename> (column_name1, column_name2) VALUES (value1, value2);`

### CRUD:  
- Create  
- Read  (SELECT)
- Update: alter existing data  
  `UPDATE <tablename> SET column_name1=value1, column_name2=value2 WHERE xxx;`  
  Tip: `SELECT` to check before update
- Delete  
  `DELETE FROM <tablename> WHERE xxx;`


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

### [String Functions](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html)
[slides](https://webdev.slides.com/coltsteele/mysql-refining-selections)
- `CONCAT`
- `CONCAT_WS`
- `SUBSTRING` or `SUBSTR`
- `REPLACE`
- `REVERSE`
- `CHAR_LENGTH`
- `LENGTH`
- `UPPER` or `UCASE`
- `LOWER` or `LCASE`
- `INSERT`
- `LEFT`
- `RIGHT`
- `REPEAT`
- `TRIM`

### Refining Selections
[slides](https://webdev.slides.com/coltsteele/mysql-refining-selections#/42)
- `DISTINCT`
- `ORDER BY`
- `LIMIT`
- `LIKE` (WILDCARDS %: 0 or 1 character, _: exact 1 character)

### [Aggregate Functions](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html)
[slides](https://webdev.slides.com/coltsteele/mysql-refining-selections#/80)
- `COUNT`
- `GROUP BY`
- `MIN` and `MAX`
- `SUM`
- `AVG`

### "ideal" query writing sequence 
[Don’t Start Your SQL Queries with the ‘Select’ Statement](https://towardsdatascience.com/dont-start-your-sql-queries-with-select-clause-d30fa1b701f6)
1. Start with `FROM`/`JOIN`
2. Move to `WHERE`
3. Use `GROUP BY`
4. `HAVING`
5. `SELECT`
6. `ORDER BY`
7. `LIMIT`