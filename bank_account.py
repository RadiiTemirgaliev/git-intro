
class BankAccount:

    # constructor method
    def __init__(self, account_number, account_holder, balance = 0) -> None:
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance


    # create an object method
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit of {amount}$. Your current balance is {self.balance}')

    
    # create an object method
    def withdraw(self, amount):
        if self.balance >= amount:
            print(f'You withdrew {amount}$. Your current balance is {self.balance}')
            self.balance -= amount
        else:
            print(f'Sorry, you have an sufficient funds to withdraw {amount}. Your current balance is {self.balance}.')



    # create an object method
    def check_balance(self):
        print(f'Account Holder: {self.account_holder}')
        print(f'Account Number: {self.account_number}')
        print(f'Current Balance: {self.balance}')

account_1 = BankAccount(123456, 'Radii Temirgaliev', 1000)
account_2 = BankAccount(234567, 'Alex Maxwell')


account_1.deposit(200)
account_1.withdraw(2000)
account_1.check_balance()

# account_2.deposit(1000)
# account_2.withdraw(500)
# account_2.check_balance()