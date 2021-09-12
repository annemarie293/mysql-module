import os
import pymysql

username = os.getenv('C9_USER')

# Connect to the datbase
connection = pymysql.connect(host='localhost',
                             user='',
                             password='',
                             db='Chinook')

try:
    # Run a Query
    with connection.cursor() as cursor:
        sql = "Select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection regardless of success or not
    connection.close()