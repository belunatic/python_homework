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

    #Enrollment Table [Join Table]
    def enroll_student(cursor, student, course):
        cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # For a tuple with one element, you need to include the comma
        results = cursor.fetchall()
        if len(results) > 0:
            student_id = results[0][0]
        else:
            print(f"There was no student named {student}.")
            return
        cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
        results = cursor.fetchall()
        if len(results) > 0:
            course_id = results[0][0]
        else:
            print(f"There was no course named {course}.")
            return

        #You can't add another UNIQUE constraint to fix this problem, because you need to reuse the course_id and student_id values in multiple records.  But, you can check to see if the record already exists before you do the insert
        cursor.execute("SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"Student {student} is already enrolled in course {course}.")
            return

        #INSERT TO ENROLLMENT TABLE
        cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))

    ... # And at the bottom of your "with" block

    enroll_student(cursor, "Jasmine", "Math 101")
    enroll_student(cursor, "Jasmine", "Chemistry 101")
    enroll_student(cursor, "Pratik", "Math 101")
    enroll_student(cursor, "Pratik", "English 101")
    enroll_student(cursor, "Carlos", "English 101")
    conn.commit() # more writes, so we have to commit to make them final!


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