import sqlite3

#add a publisher
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

#add a magazine
def add_magazine(cursor, name, publisher_name):
    try:
        #get the publisher id
        cursor.execute("SELECT publisher_id FROM Publishers WHERE name = ?", (publisher_name,))
        publisher_id = cursor.fetchone()[0]
        if publisher_id is None:
            print(f"Publisher {publisher_name} does not exist.")
            return
        #add the magazine
        cursor.execute("INSERT INTO Magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

#add a subscriber
def add_subscriber(cursor, name, address):
    try:
        #check to see if name and address already exist in the database
        cursor.execute("SELECT name,address FROM Subscribers WHERE name = ? AND address = ?", (name, address))
        result = cursor.fetchone()
        if result is not None:
            print(f"{name} with address {address} is already in the database.")
            return
        #add the subscriber
        cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?,?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

#add a subscription
def add_subscription(cursor, subscriber_name, magazine_name):
    try:
        #get the subscriber id
        cursor.execute("SELECT subscriber_id FROM Subscribers WHERE name = ?", (subscriber_name,))
        subscriber_id = cursor.fetchone()[0]
        if subscriber_id is None:
            print(f"Subscriber {subscriber_name} does not exist.")
            return
        #get the magazine id
        cursor.execute("SELECT magazine_id FROM Magazines WHERE name = ?", (magazine_name,))
        magazine_id = cursor.fetchone()[0]
        if magazine_id is None:
            print(f"Magazine {magazine_name} does not exist.")
            return
        #check to see if the subscription already exists
        cursor.execute("SELECT * FROM Subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
        result = cursor.fetchone()
        if result is not None:
            print(f"{subscriber_name} is already subscribed to {magazine_name}.")
            return
        #add the subscription
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id) VALUES (?,?)", (subscriber_id, magazine_id))
    except sqlite3.IntegrityError:
        print(f"{subscriber_name} is already subscribed to {magazine_name}.")

#connect to DB
with sqlite3.connect("../db/magazines.db") as conn:
    print('Database created and connected successfully')
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

try:
    ##---CREATE TABLES---##
    #create the publishers table
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE )""")

    #create the magazines table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
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

    ##---INSERT DATA---##
    #insert to publishers table
    add_publisher(cursor, 'Times')
    add_publisher(cursor, 'Vouge')
    add_publisher(cursor, 'New York Times')

    #insert to magazines table
    add_magazine(cursor, 'Global', 'Times')
    add_magazine(cursor, 'Fashion', 'Vouge')
    add_magazine(cursor, 'New York Cooking', 'New York Times')
    add_magazine(cursor, 'Love', 'Vouge')

    #insert to subscribers table
    add_subscriber(cursor, 'John Doe', '123 Main St')
    add_subscriber(cursor, 'Jane Smith', '456 Oak Ave')
    add_subscriber(cursor, 'Alice Johnson', '789 Pine Rd')

    #insert to subscriptions table
    add_subscription(cursor, 'John Doe', 'Global')
    add_subscription(cursor, 'Jane Smith', 'Fashion')
    add_subscription(cursor, 'Alice Johnson', 'New York Cooking')
    add_subscription(cursor, 'John Doe', 'Fashion')  

    conn.commit() 

    ##---SELECT DATA---##
    #retrieve all subscribers
    cursor.execute("SELECT * FROM Subscribers")
    result = cursor.fetchall()
    print("\nSubscribers:")
    for row in result:
        print(row)

    #retrieve all magazines in sorted by name
    cursor.execute("SELECT * FROM Magazines ORDER BY name")
    result = cursor.fetchall()
    print("\nMagazines:")
    for row in result:
        print(row)

    #retrieve all magazines from a particular publisher
    cursor.execute(""" SELECT Magazines.name FROM Magazines
    JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id
    WHERE Publishers.publisher_id = 2 """)
    result = cursor.fetchall()
    print("\nMagazines from Publisher ID 2:")
    for row in result:
        print(row)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
    