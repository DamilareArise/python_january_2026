
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
conn.autocommit = True

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


# query = "INSERT INTO users_table(fullname, email, password, account_no) VALUES('Arise Damilare', 'dami@gmail.com', '1234', '1234567890')"
# cursor.execute(query)

import random

def get_password():
    password = input('Password: ').strip()
    password2 = input('Confirm Password: ').strip()
    if password == password2:
        return password
    else:
        print('Password do not match')
        return get_password()

def signup():
    print('Signup page\n')
    fullname = input('Fullname: ').strip().title()
    email = input('Email: ').strip().lower()
    password = get_password()
    account_no = random.randint(1000000000, 1099999999)

    query = "INSERT INTO users_table(fullname, email, password, account_no) VALUES(%s, %s, %s, %s)"
    values = (fullname, email, password, account_no)
    cursor.execute(query, values)
    
    print('Registration completed!')

# signup()


# query = "UPDATE users_table SET account_balance = 10000"
# cursor.execute(query)

def deposit():
    amount = float(input('Amount: '))
    email = input('Email: ').strip().lower()
    
    if not amount or amount <= 0:
        print('Invalid amount')
    else:
        
        # fetch the previous balance then update
        query = 'SELECT account_balance FROM users_table WHERE email = %s'
        value = (email, )
        cursor.execute(query, value)
        details = cursor.fetchone()
        if details:
            balance = details[0]
            balance += amount
            
            query = "UPDATE users_table SET account_balance = %s WHERE email = %s"
            values = (balance, email)
            cursor.execute(query, values)
            print('Deposit successful')
        else:
            print('User not found')
        
        
deposit()

# query = "DELETE FROM users_table WHERE email=%s"
# value = ('ade@gmail.com', )
# cursor.execute(query, value)


# query = "SELECT * FROM users_table"
query = "SELECT fullname, account_no, account_balance FROM users_table"
# cursor.execute(query)
# details = cursor.fetchall()
# print(details[1][0])
# for each in details:
#     print(each[0])

def login():
    print('Login\n')
    email = input('Email: ').strip()
    password = input('Passoword: ').strip()
    
    
    query = "SELECT * FROM users_table WHERE email=%s AND password=%s"
    values = (email, password)
    cursor.execute(query, values)
    detail = cursor.fetchone()
    # print(detail)
    if detail:
        print('Welcome', detail[1])
    else:
        print('Invalid email or password')
    
# login()

