-- USE information_schema;

INSERT INTO cats(name, age) VALUES ('meatball',5), ('Turkey', 1), ('doudou', 4);
DESC cats;

CREATE TABLE people (first_name varchar(20), last_name varchar(20), age INT);
INSERT INTO people (first_name, last_name, age) VALUES ('Tina', 'Belcher', 13);
INSERT INTO people (first_name, last_name, age) VALUES ('Bob', 'Belcher', 42);
INSERT INTO people (first_name, last_name, age) VALUES ('Linda', 'Belcher', 45), ('Phillip', 'Frond', 38), ('Calvin', 'Fischoeder', 70);

CREATE TABLE unique_cats (
	cat_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT
);
-- another way:
CREATE TABLE unique_cats2 (
	cat_id INT AUTO_INCREMENT, -- auto-incremented
    name VARCHAR(100),
    age INT,
    PRIMARY KEY (cat_id)
);
INSERT INTO unique_cats2 (name, age) VALUES ('dannie', 1);
INSERT INTO unique_cats2 () VALUES ();

CREATE TABLE employees
	(
		id INT AUTO_INCREMENT PRIMARY KEY,
        last_name VARCHAR(100) NOT NULL,
        first_name VARCHAR(100) NOT NULL,
        middle_name VARCHAR(100),
        age INT NOT NULL,
        current_status VARCHAR(100) NOT NULL DEFAULT 'employed'
    );
INSERT INTO employees (last_name, first_name, age) VALUES ('chickenman', 'thomas', 87);



CREATE TABLE cats
(
	cat_id INT AUTO_INCREMENT,
    name VARCHAR(100),
    breed VARCHAR(100),
    age INT,
    PRIMARY KEY (cat_id)
);
INSERT INTO cats(name, breed, age)
VALUES  ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);

-- rapid file exercise
SELECT name, breed FROM cats;
SELECT name, age FROM cats WHERE breed='Tabby';
SELECT cat_id, age FROM cats WHERE cat_id=age;

SELECT * FROM cats;
SET SQL_SAFE_UPDATES = 0;
UPDATE cats SET age=14 WHERE name='Misty';
UPDATE cats SET breed='Shorthair' WHERE breed='Tabby';

UPDATE cats SET name='Jack' WHERE name='Jackson';
UPDATE cats SET breed='British Shorthair' WHERE name='Ringo';
UPDATE cats SET age=12 WHERE breed='Maine Coon';

DELETE FROM cats WHERE name='Egg';
DELETE FROM cats WHERE age=4;

SELECT * FROM cats WHERE age=cat_id;
DELETE FROM cats WHERE age=cat_id;

DELETE FROM cats;
DESC cats;
