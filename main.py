import sqlite3

def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            branch TEXT,
            marks INTEGER
        )
    """)
    conn.commit()
    conn.close()

def add_student(roll, name, branch, marks):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll, name, branch, marks))
    conn.commit()
    conn.close()
    print("✅ Student added successfully!")
    
def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    for row in data:
        print(row)
    conn.close()


 

def update_student(roll, name, branch, marks):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name = ?, branch = ?, marks = ? WHERE roll = ?", (name, branch, marks, roll))
    conn.commit()
    conn.close()
    print("✅ Student updated successfully!")

def delete_student(roll):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll = ?", (roll,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted successfully!")

def menu():
    create_table()
    while True:
        print("\n📚 Student Database Menu")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            branch = input("Enter Branch: ")
            marks = int(input("Enter Marks: "))
            add_student(roll, name, branch, marks)

        elif choice == "2":
            view_students()

        elif choice == "3":
            roll = int(input("Enter Roll No to Update: "))
            name = input("Enter New Name: ")
            branch = input("Enter New Branch: ")
            marks = int(input("Enter New Marks: "))
            update_student(roll, name, branch, marks)

        elif choice == "4":
            roll = int(input("Enter Roll No to Delete: "))
            delete_student(roll)

        elif choice == "5":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice, try again!")

menu()
