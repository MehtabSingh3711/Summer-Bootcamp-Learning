-- DDL COMMANDS
CREATE database mydb;
use mydb;
-- Create table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE,
    salary DECIMAL(10, 2)
);
-- Alter Table
ALTER TABLE employees
ADD COLUMN department VARCHAR(50) AFTER last_name;

-- Drop Table
DROP TABLE IF EXISTS backup_employees;

-- DML COMMANDS
-- INSERT
INSERT INTO employees (first_name, last_name, email, hire_date, salary)
VALUES ('John', 'Doe', 'john.doe@company.com', '2022-05-01', 55000.00);

-- Update
UPDATE employees
SET salary = salary * 1.1
WHERE hire_date < '2021-01-01';

-- Delete
DELETE FROM employees
WHERE emp_id = 105;

-- Select
SELECT first_name, last_name, department, salary
FROM employees
WHERE department = 'Marketing'
ORDER BY salary DESC;