-- Database Schema for Student Management
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    major TEXT NOT NULL,
    gpa REAL
);

-- Sample Data for Testing
INSERT INTO Students (name, major, gpa) VALUES ('Alex Smith', 'Applied Math', 3.8);
