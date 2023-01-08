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
    )