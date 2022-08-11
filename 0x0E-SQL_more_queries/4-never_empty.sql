-- creates the table id_not_null on your MySQL server
-- creates a table and make id have a default of 1
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
