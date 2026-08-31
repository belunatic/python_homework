import sqlite3

#connect to DB
with sqlite3.connect("../db/magazines.db") as conn:
    print('Database created and connected successfully')
    
    cursor = conn.cursor()

try:
    #create the publishers table
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE)""")

    #create the magazines table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
        magazine_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
    )""")

    #create subscribers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )""")

    #create subscriptions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        FOREIGN KEY (subscriber_id) REFERENCES Subscribers(subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES Magazines(magazine_id)
    )""")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
    