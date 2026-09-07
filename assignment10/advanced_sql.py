import sqlite3

conn = sqlite3.connect('../db/lesson.db')
cursor = conn.cursor()

query = ''' 
SELECT o.order_id, ROUND(SUM(li.quantity * p.price), 2) AS total_per_order
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

conn.close()