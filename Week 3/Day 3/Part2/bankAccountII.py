class Users:
    def __init__(self,username,email):
        self.name= username
        self.email= email
        self.balance= 0

    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.balance -= amount
        return self
    
    def display_user_balance(self):
        print("Balance: ",self.balance)
        print("name: ",self.name)
        return self
    
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self
        
# user1 = Users("nate", "email@here")
# user2 = Users("bob", "bob@here")

# user1.make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawl(200).transfer_money(user2,2000).display_user_balance()

# user2.make_deposit(800).display_user_balance()

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

        


# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive


