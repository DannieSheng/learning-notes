-- Create a database
CREATE DATABASE shirts_db;
USE shirts_db;

-- Create a table 
CREATE TABLE shirts 
(
	shirt_id INT AUTO_INCREMENT,
    article VARCHAR(50),
    color VARCHAR(50),
    shirt_size VARCHAR(5),
    last_worn INT,
    PRIMARY KEY (shirt_id)
);

DESC shirts; 

-- Add records to table
INSERT INTO shirts(article, color, shirt_size, last_worn)
VALUES ('t-shirt', 'white', 'S', 10),
('t-shirt', 'green', 'S', 200),
('polo shirt', 'black', 'M', 10),
('tank top', 'blue', 'S', 50),
('t-shirt', 'pink', 'S', 0),
('polo shirt', 'red', 'M', 5),
('tank top', 'white', 'S', 200),
('tank top', 'blue', 'M', 15);

-- Show table
SELECT * FROM shirts;

-- Add an additional record
INSERT INTO shirts(color, article, shirt_size, last_worn)
VALUES ('purple', 'polo shirt', 'M', 50);

-- Several selects
SELECT article, color FROM shirts;
SELECT article, color, shirt_size, last_worn FROM shirts WHERE shirt_size='M';

-- Update all polo shirts by changing their size to L
SELECT * FROM shirts WHERE article='polo shirt';
UPDATE shirts SET shirt_size='L' WHERE article='polo shirt';

-- Update the shirt last worn 15 days ago by changing last_worn to 0
SELECT * FROM shirts WHERE last_worn=15;
UPDATE shirts SET last_worn=0 WHERE last_worn=15;
SELECT * FROM shirts; 

-- Update all white shirts by changing size to 'XS' and color to 'off white'
SELECT shirt_size, color FROM shirts WHERE color='white';
UPDATE shirts SET shirt_size='XS', color='off white' WHERE color='white';

-- Delete all old shirts Last worn 200 days ago
SELECT * FROM shirts WHERE last_worn>=200;
DELETE FROM shirts WHERE last_worn>=200;

-- Delete all tank tops
SELECT * FROM shirts WHERE article='tank top'; 
DELETE FROM shirts WHERE article='tank top'; 

-- Delete all shirts
DELETE FROM shirts;

SELECT * FROM shirts;

-- Drop the shirts table
DROP TABLE shirts;