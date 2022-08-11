-- creates the table unique_id on your MySQL server
-- creates a table and make the id have a default 1 and unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
