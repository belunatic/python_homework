import sqlite3

# Connect to the database

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    #update a DB
    cursor.execute("UPDATE Students SET name='Abel', age=40 WHERE student_id=1")
    conn.commit()