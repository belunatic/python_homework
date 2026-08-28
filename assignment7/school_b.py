import sqlite3 

#TRY/EXCEPT alternative and better method to approach

def add_student(cursor, name, age, major):
    try:
        cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_course(cursor, name, instructor):
    try:
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

# Connect to the database

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables

    add_student(cursor, 'Jasmine', 20, 'Computer Science')  
    add_student(cursor, 'Pratik', 22, 'History')
    add_student(cursor, 'Carlos', 19, 'Biology')
    add_course(cursor, 'Math 101', 'Dr. Smith')
    add_course(cursor, 'English 101', 'Ms. Jones')
    add_course(cursor, 'Chemistry 101', 'Dr. Lee')

    conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")

    cursor.execute("SELECT * FROM Students ")
    result = cursor.fetchall()
    for row in result:
        print(row)

    #---------

    #The code below will cause exception when ran twice bcuz COurse name need to be UNIQUE.

    # # Insert sample data into tables
    # cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Jasmine', 20, 'Computer Science')")
    # cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Pratik', 22, 'History')") 
    # cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Carlos', 19, 'Biology')") 
    # #OR ALL IN ONE SHOT
    # cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Jazzmyn', 38, 'Computer Science'), ('Anita', 22, 'History')")

    # cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Sanchez')")
    # cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('English 101', 'Ms. Jones')") 
    # cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Chemistry 101', 'Dr. Lee')") 

    # conn.commit() 
    # # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    # print("Sample data inserted successfully.")