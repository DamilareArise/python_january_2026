import random as rnd
import time
import datetime
from gtts import gTTS
import pyttsx3



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
            return f"Deposit successful. balance is #{self.__balance:,}"
        
    def withdraw(self, amount):
        if not amount or amount < 0:
            return 'Amount is Invalid'
        elif amount > self.__balance:
            return 'insufficient fund'
        else:
            self.__balance -= amount
            return f"Withrawal successful. balance is #{self.__balance:,}"
        
    def getBalance(self):
        return self.__balance
    
    
    
def generate_account_no():
    return rnd.randint(2100000000, 2199999999)
    
# print(generate_account_no())

# print('processing....')
# time.sleep(3)
# print('Done')

# print(datetime.datetime.now())


# gtts = gTTS('Hello! Welcome to python class')
# gtts.save('hello.mp3')

engine = pyttsx3.init()
engine.say('Hello! Welcome to python class')
engine.runAndWait()
