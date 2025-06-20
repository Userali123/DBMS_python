import sqlite3
import os
print("Database saved at:", os.path.abspath("student_db.db"))
#Connect to DB (creates if not exists)
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

#Creating the student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade INTEGER,
    roll_number INTEGER UNIQUE
)
""")
conn.commit()

#Function to edit full student details
def edit_student_details():
    roll_number = int(input("Enter current roll number of the student: "))
    cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
    student = cursor.fetchone()

    if student:
        print(f"Current Details → ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}, Roll: {student[3]}")

        new_name = input("Enter new name (or press Enter to keep same): ") or student[1]
        new_grade_input = input("Enter new grade (or press Enter to keep same): ")
        new_grade = int(new_grade_input) if new_grade_input else student[2]
        new_roll_input = input("Enter new roll number (or press Enter to keep same): ")
        new_roll = int(new_roll_input) if new_roll_input else student[3]

        try:
            cursor.execute("""
                UPDATE students SET name = ?, grade = ?, roll_number = ? WHERE roll_number = ?
            """, (new_name, new_grade, new_roll, roll_number))
            conn.commit()
            print("Student details updated successfully!\n")
        except sqlite3.IntegrityError:
            print("Roll number already exists. Please choose another one.\n")
    else:
        print("Student not found.\n")

#Function to add student
def add_student():
    name = input("Enter student's name: ")
    grade = int(input("Enter grade (class): "))
    roll_number = int(input("Enter roll number: "))
    try:
        cursor.execute("INSERT INTO students (name, grade, roll_number) VALUES (?, ?, ?)", (name, grade, roll_number))
        conn.commit()
        print("Student added successfully!\n")
    except sqlite3.IntegrityError:
        print("Roll number must be unique.\n")
#code created by mir alif ali github.com/Userali123
#Function to update student
def update_student():
    roll_number = int(input("Enter roll number of student to update: "))
    cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
    data = cursor.fetchone()
    if data:
        print(f"Current data: {data}")
        new_name = input("Enter new name (leave blank to keep same): ") or data[1]
        new_grade = input("Enter new grade (leave blank to keep same): ") or data[2]
        cursor.execute("UPDATE students SET name = ?, grade = ? WHERE roll_number = ?", (new_name, new_grade, roll_number))
        conn.commit()
        print("Student updated successfully!\n")
    else:
        print("No student found with that roll number.\n")

#Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        print("\n All Student Records:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}, Roll: {row[3]}")
        print()
    else:
        print("No records found.\n")

# Function to search by name
def search_student():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    if rows:
        print("\n Search Results:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}, Roll: {row[3]}")
        print()
    else:
        print("No student found with that name.\n")

#Function to delete student
def delete_student():
    roll_number = int(input("Enter roll number to delete: "))
    cursor.execute("DELETE FROM students WHERE roll_number = ?", (roll_number,))
    if cursor.rowcount > 0:
        conn.commit()
        print("Student deleted successfully!\n")
    else:
        print("No student found with that roll number.\n")
#Function to edit full student details
def edit_student_details():
    roll_number = int(input("Enter current roll number of the student: "))
    cursor.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
    student = cursor.fetchone()

    if student:
        print(f"Current Details → ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}, Roll: {student[3]}")

        new_name = input("Enter new name (or press Enter to keep same): ") or student[1]
        new_grade_input = input("Enter new grade (or press Enter to keep same): ")
        new_grade = int(new_grade_input) if new_grade_input else student[2]
        new_roll_input = input("Enter new roll number (or press Enter to keep same): ")
        new_roll = int(new_roll_input) if new_roll_input else student[3]

        try:
            cursor.execute("""
                UPDATE students SET name = ?, grade = ?, roll_number = ? WHERE roll_number = ?
            """, (new_name, new_grade, new_roll, roll_number))
            conn.commit()
            print("Student details updated successfully!\n")
        except sqlite3.IntegrityError:
            print("Roll number already exists. Please choose another one.\n")
    else:
        print("Student not found.\n")

#Menu
def menu():
    while True:
        print("===== Student DBMS Menu =====")
        print("1. Add Student")
        print("2. Update Student (Name & Grade)")
        print("3. View All Students")
        print("4. Search Student by Name")
        print("5. Delete Student")
        print("6. Exit")
        print("7. Edit Full Student Details (Name, Grade, Roll Number)")  # NEW OPTION

        choice = input("Enter your choice (1–7): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            view_students()
        elif choice == '4':
            search_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program.")
            break
        elif choice == '7':
            edit_student_details()
        else:
            print("Invalid choice. Please try again.\n")


menu()


conn.close()
