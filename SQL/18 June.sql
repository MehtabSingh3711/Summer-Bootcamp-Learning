-- Create the database
CREATE DATABASE employees;

-- Use the employees database
USE employees;

-- Create the departments table
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

-- Insert some sample data into the departments table
INSERT INTO departments (department_name) VALUES
    ('Sales'),
    ('Marketing'),
    ('Finance'),
    ('Human Resources');

-- Create the employees table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Insert some sample data into the employees table
INSERT INTO employees (first_name, last_name, department_id) VALUES
    ('John', 'Doe', 1),
    ('Jane', 'Smith', 2),
    ('Michael', 'Johnson', 1),
    ('Emily', 'Williams', 3),
    ('David', 'Brown', NULL),
    ('Sarah', 'Davis', 4);
    
-- DQL (Data Query Language) Commands
-- SELECT with WHERE clause
SELECT first_name, last_name
FROM employees
WHERE department_id = 1;

-- SELECT with ORDER BY clause
SELECT first_name, last_name
FROM employees
ORDER BY last_name ASC;

-- SELECT with LIMIT clause
SELECT first_name, last_name
FROM employees
LIMIT 3;

-- SELECT with DISTINCT clause
SELECT DISTINCT department_id
FROM employees;

-- SELECT with COUNT function
SELECT COUNT(*) AS total_employees
FROM employees;

-- SELECT with LIKE clause
SELECT first_name, last_name
FROM employees
WHERE last_name LIKE 'D%';

-- SELECT with IN clause
SELECT first_name, last_name
FROM employees
WHERE department_id IN (1, 2);

-- SELECT with JOIN clause
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- Built In Functions
-- String functions
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;

-- Numeric functions
SELECT ROUND(AVG(department_id), 2) AS avg_department_id
FROM employees
WHERE department_id IS NOT NULL;

-- Date and Time functions
SELECT DATE_FORMAT(CURDATE(), '%M %d, %Y') AS current_date;

-- Conditional functions
SELECT
    first_name,
    last_name,
    CASE
        WHEN department_id IS NULL THEN 'No Department'
        ELSE (SELECT department_name FROM departments WHERE department_id = employees.department_id)
    END AS department
FROM employees;

-- Aggregate functions
SELECT MAX(department_id) AS max_department_id
FROM employees;

-- Other functions
SELECT COALESCE(department_id, 0) AS department_id_or_zero
FROM employees;