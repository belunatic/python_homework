import pandas as pd
import sqlite3

#cononect to database
with sqlite3.connect("../db/lesson.db") as conn:
    #sql query
    sql_statement = """SELECT line_items.line_item_id, line_items.quantity,     line_items.product_id, products.product_name, products.price 
    FROM line_items 
    JOIN products ON line_items.product_id = products.product_id"""

    #DataFrame from SQL query
    df = pd.read_sql_query(sql_statement, conn)

    #print the first 5 rows of the DataFrame
    print('\nFirst 5 rows of the DataFrame:')
    print(df.head())

    #Total column
    df['total'] = df['quantity'] * df['price']
    print('\nDataFrame with Total column:')
    print(df.head())

    #groupby
    df_grouped = df.groupby('product_id').agg({'line_item_id': 'count', 'total': 'sum', 'product_name': 'first'})
    print('\nGrouped DataFrame:')
    print(df_grouped.head())

    #sort
    df_grouped.sort_values(by='product_name', ascending=True, inplace=True)
    print('\nSorted Grouped DataFrame:')
    print(df_grouped.head())

    #write to CSV
    df_grouped.to_csv('./order_summary.csv', index=False)