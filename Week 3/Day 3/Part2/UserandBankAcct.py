class Users:
    def __init__(self,username,email):
        self.name= username
        self.email= email
        self.account = BankAccount(balance=0, interest = 2)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print("Balance: ",self.account)
        print("name: ",self.name)
        return self
    
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.balance += amount
        return self

class BankAccount():
    def __init__(self,balance, interest):
        self.balance = 0
        self.interest = interest
    def deposit(self, amount):
        self.balance += amount
        return self 
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance: ",self.balance)
        return self
    def yield_interest(self):
        self.balance *= (self.interest/100)
        return self

user1 = Users("nate", "email@here")
user2 = Users("bob", "bob@here")

user1.make_deposit(500).make_withdrawl(28)

user2.make_deposit(800).display_user_balance()