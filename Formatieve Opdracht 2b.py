import pymongo
import mysql.connector as mysql
import csv


f = open("password.txt", "r")
password = f.readline()
f.close()


def create_database():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=password
    )
    mycursor = mydb.cursor()

    mycursor.execute("DROP DATABASE IF EXISTS webshop")
    mycursor.execute("CREATE DATABASE webshop")


def create_table():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="webshop"
    )
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS products")
    mycursor.execute("DROP TABLE IF EXISTS sessions")
    mycursor.execute("DROP TABLE if EXISTS profiles")

    mycursor.execute("CREATE TABLE products ("
                     "id VARCHAR(255) PRIMARY KEY, "
                     "name VARCHAR(255), "
                     "cat VARCHAR(255), "
                     "subcat VARCHAR(255), "
                     "subsubcat VARCHAR(255), "
                     "brand VARCHAR(255), "
                     "gender VARCHAR(45), "
                     "price DECIMAL(10,2), "
                     "herhaalaankopen BOOLEAN, "
                     "doelgroep VARCHAR(45), "
                     "kleur VARCHAR(45), "
                     "descr VARCHAR(255), "
                     "discount VARCHAR(255), "
                     "eenheid VARCHAR(15), "
                     "inhoud VARCHAR(20), "
                     "leeftijd VARCHAR(45), "
                     "serie VARCHAR(45), "
                     "soort VARCHAR(45), "
                     "sterkte VARCHAR(45), "
                     "tax VARCHAR(20), "
                     "weekdeal BOOLEAN, "
                     "size VARCHAR(45), "
                     "recommendable BOOLEAN)")

    mycursor.execute("CREATE TABLE profiles ("
                     "id VARCHAR(255) PRIMARY KEY)")

    mycursor.execute("CREATE TABLE sessions ("
                     "id VARCHAR(255) PRIMARY KEY, "
                     "build VARCHAR(255), "
                     "segment VARCHAR(45), "
                     "has_sale BOOLEAN, "
                     "order_table VARCHAR(255), "
                     "sources VARCHAR(45), "
                     "events_table VARCHAR(255), "
                     "user_agent VARCHAR(45), "
                     "session_start VARCHAR(255), "
                     "session_end VARCHAR(255), "
                     "profile_id VARCHAR(255), "
                     "product_id VARCHAR(255), "
                     "FOREIGN KEY(product_id) REFERENCES products(id), "
                     "FOREIGN KEY(profile_id) REFERENCES profiles(id))")

def show_tables():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="webshop"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)


def add_data():
    mydb = mysql.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="webshop"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO products ()"


def run():
    create_database()
    create_table()
    show_tables()
    #add_data()

run()