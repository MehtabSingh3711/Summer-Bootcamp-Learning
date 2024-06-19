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
    
-- Joins
-- INNER JOIN
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;

-- LEFT JOIN
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;

-- RIGHT JOIN
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id;

-- CROSS JOIN
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
CROSS JOIN departments d;