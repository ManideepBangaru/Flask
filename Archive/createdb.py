# pip install mysql-connector
# pip install mysql-connector-python
# pip install mysql-connector-python-rf

from importlib_metadata import Prepared
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "AdMiN1234"
)

my_cursor = mydb.cursor(buffered=True)

# my_cursor.execute("CREATE DATABASE teamalpha;")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)
# my_cursor.execute("CREATE TABLE teamalph_a (Name varchar(255), Age int);")

my_cursor.execute("USE teamalpha;")
my_cursor.execute("INSERT INTO teamalph_a VALUES (%s,%s);",("mani",23))
my_cursor.execute("SELECT * FROM teamalph_a")
mydb.commit()
