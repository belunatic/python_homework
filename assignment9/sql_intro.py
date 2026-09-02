import sqlite3

#add a publisher
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

#add a magazine
def add_magazine(cursor, name, publisher_name):
    try:
        #get the publisher id
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        row= cursor.fetchone()
        publisher_id = row[0] if row else None
        if publisher_id is None:
            print(f"Publisher {publisher_name} does not exist.")
            return
        #add the magazine
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

#add a subscriber
def add_subscriber(cursor, name, address):
    try:
        #check to see if name and address already exist in the database
        cursor.execute("SELECT name,address FROM subscribers WHERE name = ? AND address = ?", (name, address))
        result = cursor.fetchone()
        if result is not None:
            print(f"{name} with address {address} is already in the database.")
            return
        #add the subscriber
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?,?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

#add a subscription
def add_subscription(cursor, subscriber_name, magazine_name, expiration_date):
    try:
        #get the subscriber id
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,))
        row = cursor.fetchone()
        subscriber_id = row[0] if row else None
        if subscriber_id is None:
            print(f"Subscriber {subscriber_name} does not exist.")
            return
        #get the magazine id
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        row = cursor.fetchone()
        magazine_id = row[0] if row else None
        if magazine_id is None:
            print(f"Magazine {magazine_name} does not exist.")
            return
        #check to see if the subscription already exists
        cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
        result = cursor.fetchone()
        if result is not None:
            print(f"{subscriber_name} is already subscribed to {magazine_name}.")
            return
        #add the subscription
        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)", (subscriber_id, magazine_id, expiration_date))
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
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE )""")

    #create the magazines table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
    )""")

    #create subscribers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )""")

    #create subscriptions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        expiration_date DATE NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id),
        UNIQUE (subscriber_id, magazine_id)
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
    add_subscription(cursor, 'John Doe', 'Global', '2031-11-20')
    add_subscription(cursor, 'Jane Smith', 'Fashion', '2044-01-11')
    add_subscription(cursor, 'Alice Johnson', 'New York Cooking', '2027-12-17')
    add_subscription(cursor, 'John Doe', 'Fashion', '2024-12-31')

    conn.commit() 

    ##---SELECT DATA---##
    #retrieve all subscribers
    cursor.execute("SELECT * FROM subscribers")
    result = cursor.fetchall()
    print("\nSubscribers:")
    for row in result:
        print(row)

    #retrieve all magazines in sorted by name
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    result = cursor.fetchall()
    print("\nMagazines:")
    for row in result:
        print(row)

    #retrieve all magazines from a particular publisher
    cursor.execute(""" SELECT magazines.* FROM magazines
    JOIN publishers ON magazines.publisher_id = publishers.publisher_id
    WHERE publishers.name = 'Vouge' """)
    result = cursor.fetchall()
    print("\nMagazines from Publisher 'Vouge':")
    for row in result:
        print(row)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
    