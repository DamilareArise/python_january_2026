
# Database: A place where data is stored, retrieved and managed

# Database management system:- Softwares that help manage databases
# Types
# 1. Relational DBMS or SQL(structured query language)
# a. data are stored in tables 
# b. Structured
# c. It support relationships between tables using primary and foriegn key
# examples are MySQL, Oracle, Postgre, MSQL, SQLlite e.t.c

# process 
# 1. create a Database (e.g Ecommerce database)
# 2. create tables (e.g orders, users, product, transaction)
# user table
'''
id(pk)      fullname            email           role
-------------------------------------------------------
1           Ayomide             ayo@mail        admin
2           Tolu                tolu@mail       vendor
3           Femi                femi@mail       customer


# profile  table
id          gender              bio             dob        user_id
---------------------------------------------------------------------
1           Female              student         1990        2
2           Male                Farmer          1993        3

'''

# product table 
'''
id          title                       price          quantity        user_id
------------------------------------------------------------------------------------------
1           Pr1                        1000           20              1
2           Pr2                        2000           20              1


'''

# orders 
'''
id(pk)      product_id             user_id(fk)          quantity        total price
----------------------------------------------------------------------------------
1           1                       2                   2                   2000
2           2                       2                   1                   2000


'''

# category 
'''
id      Name           description
--------------------------------------
1.      Electronics
2.      Family
3.      Fashion

'''

# productcategory table
'''
id          product_id          category_id
---------------------------------------------------
1.          1                     1
2.          1                     2
3.          2                     3
4.          2                     2

'''
# pr1 -> electronics and family
# family -> pr1 and pr2


# Types of relationships
# 1. one to one relationship e,g user table and profile table
# 2. one to many relationship e.g user table product table or user table and order tablez
# 3. many to many relationship


# 2. Non-Relational DBMS or NoSQL


import mysql.connector as sql

conn = sql.connect(
        host = "localhost",
        user = "root",
        password = "password",
        port = 3306,
        database = "jan_bank_db"
    )

cursor = conn.cursor()

# Types of sql queries
# 1. DDL (Data Definition Language) - used to define the structure of the database
# CREATE, ALTER, DROP, TRUNCATE

# 2. DML (Data Manipulation Language) - used to manipulate the data in the database
# INSERT, UPDATE, DELETE

# 3. DQL (Data Query Language) - used to query the data in the database 
# SELECT


# cursor.execute("DROP DATABASE IF EXISTS jan_bank_db")
# cursor.execute("CREATE DATABASE IF NOT EXISTS jan_bank_db")

# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())
# for db in cursor:
#     print(db)


# cursor.execute("""
#         CREATE TABLE users_table(
#             id INT PRIMARY KEY AUTO_INCREMENT,
#             fullname VARCHAR(50),
#             email VARCHAR(50) UNIQUE,
#             password VARCHAR(50),
#             account_no VARCHAR(10) UNIQUE,
#             balance FLOAT(10, 2) DEFAULT 0.0,
#             created_at DATETIME DEFAULT CURRENT_TIMESTAMP
#         )       
#     """)

# cursor.execute("DROP TABLE users_table")


# cursor.execute("ALTER TABLE users_table DROP COLUMN balance")
# cursor.execute("ALTER TABLE users_table ADD COLUMN balance FLOAT(10, 2) DEFAULT 0.0 AFTER account_no")
# cursor.execute("ALTER TABLE users_table CHANGE balance account_balance FLOAT(10, 2) DEFAULT 0.0")



