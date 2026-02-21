# print(5 + 5)

# commenting

# 1. line comment
# 2. block comment
"""
Hello Techies
Welcome to Python class 
This is an example of block comment
"""

# print("Welcome Mr. Tope Tunji")


# # Identation

# print(2+2)

# def run():
#     print("I can run very fast")
    

# run()
    

# Python Variable
name = "Ojo Ola"
# variable name, assignment operator and value

# Types of variable declaration

# 1. single variable and single value
basket = "moimoi"
# 2. single variable and multiple value
basket = "moimoi", "eko", "eggs"
# print(basket)
# 3. multiple variable and single value
x = y = z = 10
y = 20
# print(x, y, z)
# 4. Multiple variable and multiple value
x, y, z = 10, 20, 30
# print(z)

# Rules 
# 1. The name must only contain alphabet, number or underscore
# 2. Variable name don't start with any character aside alpahabet or underscore
# 3. a variable name does not allow space
# first_name = 'john' # snake casing
# firstName = 'john' # camel casing
# FirstName = "john"  # Pascal casing 
# 4. Your variable must be descriptive 


# Dynamic variable value

# first_name = input("Firstname: ")
# last_name = input("Lastname: ")
# print(first_name)
# print(last_name)


# Concatenation
""    # string

# print("Habeeb " + "Oke")
# print("Habeeb" + "2")

# print("Habeeb", "Oke")
# print("habeeb", 2)


# name = input("Name: ")

# print("Welcome", name)
# print("Welcome " + name)

# fullname = "Arise Damilare"
# course = "Datascience"
# age = 20
# account_balance = 2000000

# print("My name is " + fullname + " I am a student of " + course + " I am " + str(age) + "years old")

# print("My name is", fullname, "I am a student of" , course , "I am " , age, "years old")


# f - string
# print(f"My name is {fullname}.  I am a student of {course}. I am {age}years old")


# Python Datatypes 

"""
1. Text type: String  str() e.g "Tayo", 'Ope'
2. Number type:
    i. Integer int() e.g 12 , 123, 1234
    ii. Float float() e.g 12.12
    iii. Complex complex() e.g 2 + 3j

3. Bolean Type: bool()  e.g True, False
4. Sequence types:
    i. list()  e.g [1, 2, 3, 4]
    ii. tuple() e.g (1, 2, 3, 4)
    iii. range() e.g range(5)

5. Mapping type:
    i. Dictionary: Dict() e.g {key: value}
    
6. NoneType: None

7. Binary Type:
    i. Byte
    ii. Bytearray
    iii. memoryView
    
8. Set type:
    i. set() e.g {}

"""
# Check the lecture for Datatypes and python operator

# var1 = "Tayo"
# var = 12.23 + 2j
# var = True
# var = ("tope", "chioma", "eniola", True, 50)
# var = ["tope", "chioma", "eniola", True, 50]
# var = list(range(1, 6, 2))

# print(type(var))
# print(var)
# print(len(var))
# print(var[-3])

student = {
    "name": "Chioma",
    "gender": "Female",
    "course": "Data Science"
}

# print(type(student))
# print(student["gender"])

var = None
# print(type(var))
# print(var)

# var = b"Chioma"
# var = bytearray([12, 34, 56])
# print(type(var))
# print(var)
# var1 = memoryview(var)
# print(var1)


# setA = {"tope", "chioma", "eniola"}
# setB = {4, 5, 1, 2, 3}
# print(type(setB))

# int("Tayo")

# empty states 
# 1. 0
# 2. None 
# 3. ""
# 4. []

# num = bool([""])
# print(num)


# Python operators
# 1. Arithmetic operator: +, -, *, /, **, //, %
# print(5%3)
# 2. Assignment operator: =, +=, -= , *=, **=
# x = 5
# x += 1
# x -= 2
# print(x)

# 3. comparison operator: ==, !=, >, <, >=, <=
x = 5
# print(x < 6)
# print( x < 6 < x)

# 4. Logical operator: and, or, not

"""
A   B   AND     OR      NOT OR
0   0   0       0       1
0   1   0       1       0
1   0   0       1       0
1   1   1       1       0

"""
rice = True
beans = False

# print(rice and beans)

# 5. Membership operator: in, not in

# python_class = ["Habeeb", "Caleb", "Chioma", "Eniola"]
# print("Eniola" not in python_class)
# print("chioma" not in python_class and "Caleb" in python_class)

# 6. Identity operator: is, is not
x = 5
y = 6
# print(x is y)


# 7. Bitwise opertors: 
#       & - and 
#       | - or  
#       ~ - not 
#       ^ - XOR

# print(bin(10))          # 1  0   1   0
# print(bin(5))           #    1   0   1
# print(bin(10 & 5))      # 0  0   0   0
# print(bin(10 | 5))
# print(bin(10 ^ 5))
# print(~10)


# condition statement (if/else)
# x = 5
# if x >= 5:
#     print("X is greater than or equal 5")
# else: 
#     print('X is less than 5 bro!')


# name = input("Name: ")
# if name:
#     print(f"Welcome {name}")
# else: 
#     print("Kindly input your name")


# USSD
# ussd = input("USSD code: ")
# if ussd == "*312#":
#     print("""
#         1. Buy Data
#         2. Check balance
#         #. Exit
#     """)
#     option = input("option: ")
#     if option == "1":
#         print("""
#         1. Daily plan
#         2. Weekly plan
#         3. Monthly plan
#         """) 
#         option = input("option: ")
#         if option == "1":
#             print("Daily plan")
#         elif option == "2":
#             print("Weekly plan")
#         elif option == "3":
#             print("Monthly plan")
        
#     elif option == "2":
#         print("Your balance is ****")
#     elif option == "#":
#         print("Thank you for banking with us")
#     else:
#         print("Invalid input")
        
# elif ussd == "*140#":
#     print("Oh bro that has been change to *312#")    

# else:
#     print("Invalid ussd code")
    

# 1. Build an application that tells if a number is odd or even
# 2. Build an application that tells if a number is fizz, buzz or fizzbuzz

# fizz - divisible by 3
# buzz - divisible by 5
# fizzbuzz - divisible by 3 and 5



# balance = 0
# while True:
#     print("""
#         1. Deposit
#         2. Withraw
#         3. Check balance
#         #. Exit
#     """)

#     option = input("Your option: ")
#     if option == "1":
#         print("""
#             1. #500
#             2. #1000
#             3. Your amount
#         """)
#         option = input("Option: ")
#         if option == "1":
#             balance += 500
#             print(f"#500 deposit successfully. Your balance is #{balance}")
#         elif option == "2":
#             balance += 1000
#             print(f"#1000 deposit successfully. Your balance is #{balance}")
#         elif option == "3":
#             amount = float(input("Amount: "))
#             balance += amount
#             print(f"#{amount} deposit successfully. Your balance is #{balance}")
#         else: 
#             print("Invalid option")
            
#     elif option == "2":
#         pass

#     elif option == "3":
#         print(f"Your balance is #{balance}")

#     elif option == "#":
#         print("Thanks for banking with us.")
#         break
        
#     else: 
#         print("Invalid option")


# x = 1
# while True:
#     print("hello", x)
#     x += 1
#     if x == 10:
#         break


# PYTHON STRINGS

var = "Hello, Good morning to you all, Welcome back." 
# ['H', 'e', 'l', 'l', 'o', ',', ' ', 'G' ...] # the way python reads the string
# print(type(var))
# print(len(var))
# print(var[-1])

# slicing
# print(var[0:3])
# print(var[3:4])
# var[0] = "L"  # ERROR

# print(var.upper())
# print(var.lower())
# print(var.title())
# print(var.capitalize())


# print(len(var.strip()))
dob = "%&$03-05-1990//*"
# print(dob.strip('%&$/*'))


# print("1. Nigeria is in continent Europe. yes/no: ")
# ans = input('Ans: ')
# if ans.strip().lower() == "no":
#     print("Correct")
# else:
#     print("Worng")

# print(var.startswith('Hello, '))
# check = input("").strip().lower()
# print(var.endswith(check))

# print(var.find('hello'))

# email validator
# email = input('email: ').strip().lower()

# if email.find('@') != -1 and email.find('.') != -1:
# if '@' in email and '.' in email:
#     print("Email is valid")
    
# else:
#     print("Invalid email")


# print(var.index('h'))

# (print(len(var.split())))
# print(var.split(','))

# stmt = ['How', 'are', 'you']
# print(' '.join(stmt))



# class activity  
# 1. build a simple cbt system.
# 2. build a word counter.
# 3 build a simple calculator


# A grading sytem
# 0- 39 => F
# 40 - 44 => E 
# 45 - 49 => D
# 50 - 59 => C
# 60 - 69  => B
# 70 - 100 => A  

# score = int(input("Score: "))
# if score >= 70 and score <= 100:
#     print("Grade A")
# elif score >= 60 and score <= 69:
#     print("Grade B")
# elif score >= 50 and score <= 59:
#     print("Grade C")
# elif score >= 45 and score <= 49:
#     print("Grade D")
# elif score >= 40 and score <=44:
#     print("Grade E")
# elif score >= 0 and score <= 39:
#     print("Grade F")
# else:
#     print("Invalid score") 
 
 
# Special character
#  \n -> nextline
#  \t -> tab
#  \r -> return
#  \b -> backspace
#  \ -> escape char
#  r -> raw string

# var = "C:\\note.txt"
# var = "Hello\t\thow are you" 
# var = "Hello\rhow are you" 
# var = r"Hello\b\bhow are you" 

# print(var)


# Python collection/arrays
# 1. List: It is Ordered, Indexed, allows duplicate, It is mutable/changeable
cars = ["Benz", "Lexus", "Audi", "BMW", "Benz"]
# print(len(cars))
# print(cars[-2])
# print(cars[0:3])
# print(cars[-2][0])
# print(cars[-3][-1])

# cars.append('Toyota')
# cars.insert(0, 'Lambo')
# cars.extend(['Lambo', 'Ferrari', 'Tesla'])
# print(cars + ['Lambo', 'Ferrari', 'Tesla'])

# cars.pop(2)
# cars.remove("Lexus")
# cars.clear()

# print(cars.index("Lexus"))
# cars.reverse()

# print(cars)

# database = []
# print("\nWelcome to MyTodo App")
# while True:
#     print("""
#         1. Add a todo
#         2. Remove a todo
#         3. Edit a todo
#         4. Clear
#         5. View todo
#         #. Exit
#     """)
    
#     option = input("Option: ")
#     if option == "1":
#         todo = input("Todo: ").strip().title()
#         database.append(todo)
#         print(f"{todo} added to the list.")
        
#     elif option == '2':
#         no = int(input("Remove Todo at number ___: "))
#         no -= 1
#         if no >= len(database):
#             print("Invalid number.")
#             continue
        
#         database.pop(no)
#         print("Item deleted.")
    
#     elif option == "4":
#         confirm = input(r'Confirm clear? Y\N: ') 
#         if confirm.upper() != 'Y':  
#             continue
        
#         database.clear()
#         print('List Cleared.') 

        
        
#     elif option == "5":
#         print(database)
    
#     elif option == "#":
#         print("Goodbye!")
#         break
    
#     else:
#         print("Invalid option.")

# Assignment
# 1. Read up on forloop
# 2. Build a Time/multiplication table using the concept of forloop


# LOOPS
# For Loops and While Loops

# fruits = ["Apple", 'Pineapple', 'Orange']
# count = 1
# for item in fruits:
#     print(item, count)
#     count += 1


# for i in range(10):
#     print(i)

# for letter in "Pineapple":
#     print(letter)

# for i in range(1, 13):
#     # print(i, "Times Table")
#     for x in range(1, 13):
#         # print(f"{i} x {x} = {i * x}")
#         print(f"{i * x} ", end=' ')
#     print()


# While loop

# x = 10
# while x > 0:
#     print(x)
#     if x == 5:
#         break

#     x -= 1


# ticket_no = 10
# while ticket_no > 0: 
#     age = int(input("Age: "))
#     if age < 16:
#         print("The movie is rated 16+ hence you are too young.")
#         continue
    
#     ticket_no -= 1
#     print('Take ticket. remaining', ticket_no)



# 2. Tuple
# tuple is a type of python collection that is indexed, duplicated, unchangeable/immutable,  ordered
# () or tuple()

fruits = ("Apple", 'Pineapple', 'Orange', 'Apple')
# print(type(fruits))
# print(fruits)
# print(fruits[0:3])
# print(fruits[-3:-1])
# print(fruits[::2])
# print(fruits[::-1])

# fruits = list(fruits)
# fruits[0] = 'Cherry'
# fruits = tuple(fruits)
# print(fruits)

# unpacking
# a, b, c, d = fruits
# c, *a, b = fruits
# print(a)

# print(fruits.count('Apple'))
# print(fruits.index('Apple', 1))


prices = [1000, 200, 3250, 900]
products = ['Shoe', 'Cap', 'Jean', 'Shirt']

items_price = [
    ('Shoe', 1000),
    ('Cap', 200),
    ('Jean', 3250),
    ('Shirt', 900)
]

# x = 0
# for i in prices:
#     x += i
    
# print(x)
# print(sum(prices))
# print(max(prices))
# print(min(prices))

# print(sum(prices)/len(prices))

# for item, price in zip(products, prices):
#     print( price)
    
# for item, price in items_price:
#     print(price)


# print('1. What is the capital of Nigeria. a) Lagos b.) Abuja')
# ans = input("Answer: ").strip().lower()
# if ans == 'a':
#     print


# questions = [
#     'What is the capital of Nigeria. a) Lagos b.) Abuja',
#     'What is the capital of Ghana. a) Accra b.) Abuja'
# ]

# answers = ['b', 'a']

# score = 0
# for ques, ans in zip(questions, answers):
#     print(ques)
#     user = input("Answer: ").strip().lower()
#     if user == ans:
#         score += 1

# print("Total =", score)


# 3. Set : unordered, unindexed, does not allow duplicate item, unchangeable/immutable
# {} or set()

fruits = {"Apple", "Orange", "Watermelon", "Cherry", "Orange"}
# print(type(fruits))
# print(fruits[0])
setA = {8, 6, 5, 3, 4, 2, 1, 9, 7}
setB = {11, 13, 12}
setC = {8, 7, 9, 6}
# print(setA)

# fruits.add("Banana")
# fruits.update({"Tomato", "Strawberry"})
# fruits.pop()
# fruits.remove("apple")
# fruits.discard('apple')

# print(fruits)
# print(setA.union(setB))
# print(setA.intersection(setB))
# print(setA.difference(setB))
# print(setB.difference(setA))
# print(setA.symmetric_difference(setB))
# setA.intersection_update(setB)
# print(setA)

# print(setA.isdisjoint(setB))
# print(setC.issubset(setA))
# print(setA.issuperset(setC))

# 4. Dictionary 
student1 = {
    'name': 'Oke Habeeb',
    'gender': 'Male',
    'id': 12345,
    "address": {
        "country": "Nigeria",
        "state": "Oyo State",
        "coord": {
            'lat': 2343,
            "lon": 234
        }
    }
}
# print(student1["address"]['coord']['lat'])

# print(student1["name"])
# print(student1.values())
# print(student1.keys())
# print(student1.items())

# for key, value in student1.items():
#     print(value)
    
# [('name', 'Oke Habeeb'), ('gender', 'Male'), ('id', 12345)]

# print(student1.get('Name', 'Not Found'))
# student1.pop('id')
# student1.popitem()
# student1.update({"dept": "Data Science"})

# print(student1)



# Python Function

# 1. declaration stage
# 2. definition stage
# 3. invokation stage

def run():
    print("I am running")
    
# run()

def sum():
    num1 = int(input('Num 1: '))
    num2 = int(input('Num 2: '))
    print("Ans:", num1 + num2)
    
# sum()

# Types of functions
# 1. Parametized
# 2. unparametized

def run(speed):
    print(f"I am running at {speed}km/hr")

# run(20)


# name = input("Name: ")
# speed = input("speed: ")

# def run(name, speed = 10):
#     print(f"{name} is running at {speed}km/hr")

# run(name, speed)


# return function

def sum():
    num1 = int(input('Num 1: '))
    num2 = int(input('Num 2: '))
    
    return num1 + num2

# print(sum())

def calculator():
    print("""
        1. Add
        2. Subtract
        3. Multiply
        #. exit
    """)
    option = input("Option: ")
    
    if option in ['1', '2', '3']:
        val1 = float(input("Value 1: "))
        val2 = float(input("Value 2: "))


    if option == '1':
       print(add(val1, val2))

    elif option == '2':
        print(subtract(val1, val2))

    elif option == "3":
        print(multiply(val1, val2))
        
    elif option == "#":
        exit()
    
    else:
        print("Invalid Input")
    
    calculator() # recursive function

def add(val1, val2):
    return val1 + val2

def subtract(val1, val2):
    return val1 - val2

def multiply(val1, val2):
    return val1 * val2


# calculator()


# Local variables and global variables


balance = 0 # global

def deposit():
    print("Deposit...")
    global balance
    
    amount = float(input("amount: "))
    if amount <= 0:
        print("Amount is required")
        deposit()
        
    balance += amount
    # balance + amount
    print(f"{amount} deposited successfully.")
    
    
def withdraw():
    global balance
    
    amount = float(input("amount: "))
    if amount <= 0:
        print("Amount is required")
        withdraw()
    
    elif amount > balance:
        print("Insufficient balance")
    
    else:
        balance -= amount
        print(f"{amount} withdrawn successfully, your balance is {balance}")
        
        
# deposit()
# withdraw()

#
        
    
def sum(num1:float | int, num2: float | int) -> float | int:
    """
    This is a function that sums two input
    """
    return num1 + num2

# sum()


# anonymous func
sum2 = lambda num1, num2 : num1 + num2
# print(sum2(4, 4))


# grading system

def check_grade(score: int):
    if score >= 70 and score <=100:
        return 'A'
    elif score >= 60 and score < 70:
        return 'B'
    else:
        return 'Invalid' 
    
# grade = check_grade(777)
# print(grade)


# ussd app

def home():
    ussd = input("USSD: ").strip()
    if ussd == "*312#":
        dashboard()
    else:
        user = input('Invalid ussd code. Press enter to try again or 1 to exit: ')
        if user == '1':
            exit()
        else:
            home()
        
def dashboard():
    print("""
        1. Data plan
        2. Check Balance
        #. exit 
    """)
    user = input("option: ")
    if user == '1':
        data_plan()
    elif user == '2':
        check_balance()
    elif user == "#":
        exit()
    else:
        print("invalid option")
        dashboard()

def data_plan():
    print("""
        1. 500mb
        2. 1gb
        3. 5gb
        *. dashboard
        #. exit 
    """)
    user = input("Option: ")
    
    if user == "*":
        dashboard()
    elif user == "#":
        exit()
    else:
       print("invalid option")
       data_plan()  

def check_balance():
    pass


# home()



password = "0000" # global variable

def change_password():
    global password
    
    old_pass = input("old password: ").strip()
    new_pass = input("new password: ").strip()
    confirm_pass = input("confirm password: ").strip()
    
    if old_pass != password:
        print("incorrect old password")
    elif new_pass != confirm_pass:
        print("password do not match")
        
    else:
        password = new_pass
        print("Password reset successfully")
        
# change_password()



# OOP -> Object Oriented Programming
# It is a way of writing your python codes in an organized, reusable manner. It help represent your codes like a real world object

# object => is anything that has a property/attributes and can perform a function e.g car, laptop, human

# object student 
# properties -> Name, Course, Gender
# functions -> study(), exam(), payTution()

# object car
# properties -> color, brand_name, model
# functions -> start(), break(), accelerate()


# class -> It is a blue print or model of an object
# self -> Allow the function or proterties in the class to be referenced to the class

class Student:
    Name = 'John Doe'
    Course = 'Data Science'
    Gender = 'Male'
    School = 'SQI College Of ICT'
    
    def __init__(self, name, course):
        self.Name = name
        self.Course = course
        
        print(f"Welcome back {self.Name}")
    
    def study(self):
        print(f'{self.Name} is studying {self.Course} at {self.School}')
        

# chioma = Student() # chioma is an object. choima is an instance of class Student
# habeeb = Student()
# ben = Student()

# habeeb.Name = "Oke Habeeb"
# habeeb.study()

# chioma.Name = 'Mbam Chioma'
# chioma.study()

# ben.Name = "Benjamin"
# ben.Course = "Artificial Intelligence"
# ben.study()


# ben = Student('Benjamin', 'AI')

# 4-Pillars of OOP
# 1. Encapsulation -> public, private, static and protected
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction


class BankAccount:
    account_name = ""
    __balance = 0    # private property
    
    def __init__(self, name):
        self.account_name = name
        print(f"Welcome back {self.account_name}")
        
    
    def deposit(self, amount):
        if not amount or amount < 0:
            return 'Amount is Invalid'
        else:
            self.__balance += amount
            return f"Deposit successful. balance is {self.__balance}"
        
    def withdraw(self, amount):
        if not amount or amount < 0:
            return 'Amount is Invalid'
        elif amount > self.__balance:
            return 'insufficient fund'
        else:
            self.__balance -= amount
            return f"Withrawal successful. balance is {self.__balance}"
        
    def getBalance(self):
        return self.__balance
            
    
    
account1 = BankAccount('Ojo Ade')
# account1.account_name = 'Ojo Adewale'
# print(account1.__balance)

# account1.__balance = 10000 

# message = account1.withdraw(1000)
# print(message)

# balance = account1.getBalance()
# print(balance)
