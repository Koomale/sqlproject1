import sqlite3

def run_app():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS Students (id INTEGER PRIMARY KEY, name TEXT, major TEXT, gpa REAL)")
    
    print("--- Student Management System ---")
    name = input("Enter Student Name: ")
    major = input("Enter Major: ")
    
    cursor.execute("INSERT INTO Students (name, major) VALUES (?, ?)", (name, major))
    conn.commit()
    print("Student saved to SQL database.")
    conn.close()

if __name__ == "__main__":
    run_app()
