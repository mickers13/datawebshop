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
    mycursor.execute("CREATE TABLE products (id VARCHAR(255) PRIMARY KEY, brand VARCHAR(50), color VARCHAR(20), "
                     "gender VARCHAR(20), category VARCHAR(255), sub_category VARCHAR(255), "
                     "sub_sub_category VARCHAR(255), name VARCHAR(255), price DECIMAL(10, 2), "
                     "recommendable BOOLEAN)")


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