import mysql.connector
f = open("password.txt", "r")
password = f.readline()
print(password)

def csv_push():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE webshop",


                     )

csv_push()

def create_table():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=Pindakaas123,
        database="webshop"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE products (id VARCHAR(255) PRIMARY KEY, brand VARCHAR(50), color VARCHAR(20), "
                     "gender VARCHAR(20), category VARCHAR(255), name VARCHAR(255), price DECIMAL(10, 2), "
                     "recommendable BOOLEAN)")

