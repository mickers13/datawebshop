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

    mycursor.execute("CREATE TABLE profiles ("
                     "id VARCHAR(255) PRIMARY KEY,"
                     "segment VARCHAR(255))")

    mycursor.execute("CREATE TABLE buids ("
                     "buid VARCHAR(255) PRIMARY KEY,"
                     "profiles_id VARCHAR(255),"
                     "FOREIGN KEY(profiles_id) REFERENCES profiles(id))")

    mycursor.execute("CREATE TABLE sessions ("
                     "id VARCHAR(255) PRIMARY KEY, "
                     "segment VARCHAR(45), "
                     "has_sale BOOLEAN, "
                     "_order VARCHAR(255), "
                     "sources VARCHAR(45), "
                     "_events VARCHAR(255), "
                     "sessionStart VARCHAR(255), "
                     "sessionEnd VARCHAR(255), "
                     "buids_buid VARCHAR(255),"
                     "FOREIGN KEY(buids_buid) REFERENCES buids(buid))")

    mycursor.execute("CREATE TABLE brands ("
                     "id INT PRIMARY KEY, "
                     "brand VARCHAR(45))")

    mycursor.execute("CREATE TABLE categories ("
                     "id INT PRIMARY KEY, "
                     "cat VARCHAR(45),"
                     "subcat VARCHAR(45),"
                     "subsubcat VARCHAR(45))")

    mycursor.execute("CREATE TABLE genders ("
                     "id INT PRIMARY KEY, "
                     "gender VARCHAR(45))")

    mycursor.execute("CREATE TABLE doelgroepen ("
                     "id INT PRIMARY KEY, "
                     "doelgroep VARCHAR(45))")

    mycursor.execute("CREATE TABLE products ("
                     "id INT PRIMARY KEY, "
                     "name VARCHAR(255), "
                     "selling_price INT, "
                     "discount INT, "
                     "herhaalaankopen BOOLEAN, "
                     "kleur VARCHAR(255), "
                     "descr VARCHAR(255), "
                     "eenheid VARCHAR(255), "
                     "inhoud VARCHAR(255), "
                     "leeftijd VARCHAR(255), "
                     "serie VARCHAR(255), "
                     "soort VARCHAR(255), "
                     "sterkte VARCHAR(255), "
                     "tax VARCHAR(255), "
                     "weekdeal BOOLEAN, "
                     "size VARCHAR(255), "
                     "brand_id INT, "
                     "cat_id INT, "
                     "gender_id INT, "
                     "doelgroep_id INT, "
                     "FOREIGN KEY(brand_id) REFERENCES brands(id),"
                     "FOREIGN KEY(cat_id) REFERENCES categories(id),"
                     "FOREIGN KEY(gender_id) REFERENCES genders(id),"
                     "FOREIGN KEY(doelgroep_id) REFERENCES doelgroepen(id))")

    mycursor.execute("CREATE TABLE orders ("
                     "session_id VARCHAR(255),"
                     "product_id INT,"
                     "FOREIGN KEY(session_id) REFERENCES sessions(id),"
                     "FOREIGN KEY(product_id) REFERENCES products(id))")


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
