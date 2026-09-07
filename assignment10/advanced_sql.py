import sqlite3

conn = sqlite3.connect('../db/lesson.db')
cursor = conn.cursor()

query = ''' 
SELECT o.order_id,ROUND(SUM(li.quantity * p.price), 2) AS total_per_order
FROM orders AS o
JOIN line_items AS li
ON o.order_id = li.order_id 
JOIN products AS p
ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5 '''

cursor.execute(query)
print(cursor.fetchall())

print("--------------------------------------------------")
print('Task 1 completed')

query = '''
SELECT customer_name , ROUND(AVG(total_price), 2) AS average_order_price
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
print(cursor.fetchall())

print("--------------------------------------------------")
print('Task 2 completed')


conn.close()