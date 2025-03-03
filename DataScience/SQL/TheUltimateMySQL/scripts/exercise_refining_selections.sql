INSERT INTO books
    (title, author_fname, author_lname, released_year, stock_quantity, pages)
    VALUES ('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
           ('fake_book', 'Freida', 'Harris', 2001, 287, 428),
           ('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);
           
SELECT * FROM books;

SELECT 
    title
FROM
    books
WHERE
    title LIKE '%stories%';

SELECT title, pages
FROM books
ORDER BY pages DESC
LIMIT 1;

SELECT CONCAT(title, ' - ', released_year) AS summary
FROM books
ORDER BY released_year DESC
LIMIT 3;

SELECT title, author_lname
FROM books
WHERE author_lname LIKE '% %';

SELECT title, released_year, stock_quantity
FROM books
ORDER BY stock_quantity, released_year DESC
LIMIT 3;

SELECT title, author_lname
FROM books
ORDER BY author_lname, title;

SELECT UPPER(CONCAT('MY FAVORITE AUTHOR IS ', author_fname, ' ', author_lname, '!')) AS yell
FROM books
ORDER BY author_lname;