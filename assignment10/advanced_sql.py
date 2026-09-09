import sqlite3

conn = sqlite3.connect('../db/lesson.db')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

query = ''' 
SELECT o.order_id,ROUND(SUM(li.quantity * p.price), 2) AS total_price
FROM orders AS o
JOIN line_items AS li
ON o.order_id = li.order_id 
JOIN products AS p
ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5 '''

cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

print('Task 1 completed')
print("--------------------------------------------------")

query = '''
SELECT customer_name , ROUND(AVG(total_price), 2) AS average_total_price
FROM customers AS c
LEFT JOIN (
SELECT o.customer_id AS customer_id_b,ROUND(SUM(li.quantity * p.price), 2) AS total_price
FROM orders AS o
JOIN line_items AS li
ON o.order_id = li.order_id 
JOIN products AS p
ON li.product_id = p.product_id
GROUP BY o.order_id
) ON c.customer_id = customer_id_b
GROUP BY c.customer_id 
ORDER BY c.customer_id'''

cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

print('Task 2 completed')
print("--------------------------------------------------")

try:
    #inserting a new order
    cursor.execute("""INSERT INTO orders (customer_id, employee_id) 
    VALUES (
    (SELECT customer_id 
    FROM customers 
    WHERE customer_name = 'Perez and Sons'),
    (SELECT employee_id 
    FROM employees 
    WHERE first_name = 'Miranda' AND last_name = 'Harris')
    ) 
    RETURNING order_id""")

    #fetch the newly inserted order_id
    new_order_id = cursor.fetchone()[0]
    # print(f"New order inserted with ID: {new_order_id}")

    #get the least expensive products for the order
    cursor.execute("""SELECT product_id, price 
    FROM products 
    ORDER BY price 
    LIMIT 5""")
    #create a list of product_ids to be added to the order
    products_id = [row[0] for row in cursor.fetchall()]
    # print(f"Products to be added to the order: {products_id}")

    #insert line items for the new order
    # for product_id in products_id:
    cursor.executemany("""INSERT INTO line_items (order_id, product_id, quantity) 
    VALUES (?, ?, ?)""", 
    [(new_order_id, product_id, 10) for product_id in products_id])   

    #commit the transaction
    conn.commit()

    #print the new order details
    cursor.execute("""SELECT li.line_item_id, li.quantity,p.product_name 
    FROM line_items AS li 
    JOIN products AS p ON li.product_id = p.product_id 
    WHERE li.order_id = ?""", 
    (new_order_id,))

    #print the line items for the new order
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()



print('Task 3 completed')
print("--------------------------------------------------")

cursor.execute("""SELECT e.employee_id,e.first_name, e.last_name, COUNT(o.order_id)
FROM employees AS e
JOIN orders AS o 
ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()