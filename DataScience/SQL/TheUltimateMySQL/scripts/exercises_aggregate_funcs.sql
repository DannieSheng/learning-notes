USE book_shop;

SHOW TABLES;
DESC books;

-- # of books in the database 19
SELECT 
    COUNT(*)
FROM
    books;
    
-- # of books released each year
SELECT released_year, COUNT(*) AS yearly_released
FROM books
GROUP BY released_year;

-- # of books in stock 2450
SELECT SUM(stock_quantity)
FROM books;

-- average released_year for each author
SELECT author_fname, author_lname, AVG(released_year) AS averaged_release_year
FROM books
GROUP BY author_fname, author_lname;

-- full name of the author who wrote the longest book
SELECT CONCAT(author_fname, ' ', author_lname) AS author, title, pages
FROM books
WHERE pages=(SELECT MAX(pages) FROM books);

SELECT released_year AS year, COUNT(*) AS '# books', AVG(pages) AS 'avg pages'
FROM books
GROUP BY released_year
ORDER BY year;
