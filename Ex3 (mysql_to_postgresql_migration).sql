-- --------------------------------------------
-- Script: mysql_to_postgresql_migration.sql
-- Purpose: Create employees table in PostgreSQL
-- and insert migrated data from MySQL
-- --------------------------------------------

-- Step 1: Create the table in PostgreSQL
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name VARCHAR(100),
    salary NUMERIC(10,2)
);

-- Step 2: Insert migrated data
INSERT INTO employees (emp_id, emp_name, salary) VALUES (1, 'Alice', 50000.00);
INSERT INTO employees (emp_id, emp_name, salary) VALUES (2, 'Bob', 60000.00);
INSERT INTO employees (emp_id, emp_name, salary) VALUES (3, 'Charlie', 55000.00);

-- Step 3: Data verification queries (optional)
SELECT COUNT(*) FROM employees;
SELECT SUM(salary) FROM employees;
SELECT * FROM employees WHERE emp_name IS NULL OR salary IS NULL;