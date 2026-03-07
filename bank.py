# import config
# import index

# from config import BankAccount, generate_account_no
from config import BankAccount as Bk

class NewBank(Bk):
    def __init__(self, name):
        super().__init__(name)
        self.dashboard()
    
    def dashboard(self):
        print('''
            1. Deposit
            2. Withdraw
            3. Check Balance
            #. Exit
        ''')
        option = input('Option: ')
        
        if option == "1":
            self.perform_deposit()
        elif option == '2':
            self.perform_withrawal()
        elif option == '3':
            balance = self.getBalance()
            print(f"Your balance is #{balance:,}")
            self.dashboard()
        elif option == '#':
            print("Goodbye")
            exit()
        else:
            print("Invalid input")
            self.dashboard()
                     
    def perform_deposit(self):
        amount = float(input("Amount: "))
        message = self.deposit(amount)
        print(message)  
        self.dashboard()
          
    def perform_withrawal(self):
        amount = float(input("Amount: "))
        message = self.withdraw(amount)
        print(message)  
        self.dashboard()  
        
        
        

bk = NewBank('Ojo Ade')