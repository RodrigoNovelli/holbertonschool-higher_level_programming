-- Making a script that creates a table with mmultiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO  second_table (id, name, score) VALUES
(1, 'Alice', 85),
(2, 'Bob', 90),
(3, 'Charlie', 78),
(4, 'David', 92),
(5, 'George', 88);