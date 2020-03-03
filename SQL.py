import mysql.connector
f = open("password.txt", "r")
password = f.readline()

def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE webshop")

#create_database()

def datading():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="webshop"
    )
    print(mydb)

#datading()

def datadinges():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="webshop"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#datadinges()

def dataaa():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="webshop"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)

dataaa()