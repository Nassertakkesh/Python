class User():
        def __init__ (self,first, last_name):
            self.first_name = first
            self.last_name = last_name
            self.email = first + '.' + last_name + '@gmail.com'
            self.account = bankAccount(interest_rate=0.02, balance=0)

        def make_deposit(self, amount):     
            self.account.deposit(amount)
            return self

        def make_withdrawl(self, amount): 
            self.account.withdraw(amount)    

        def transfer_money(self,amount,user):
            self.account.withdraw(amount)
            user.account.deposit(amount)
            return self

class bankAccount():

        def __init__ (self,interest_rate, balance ):
            self.balance = 0
            self.interest_rate = interest_rate
        def deposit(self, amount):     
            self.balance += amount
            return self
        def withdraw(self, amount):  
            if self.balance < amount:  
                print("Insufficient funds: Charging a $5 fee" )
                self.balance -= 5
            else:
                self.balance -= amount
            return self
        def display_account_info(self):
                print("Balance: $", self.balance)
                return self
        def yield_interest(self):
                if self.balance < 0:  
                    print("Insufficient funds: Charging a $5 fee" )
                else:
                    self.balance = self.balance * self.interest_rate
                return self

nate = User("nasser", "takkesh")


nate.make_deposit(5000)
print(nate.account)

# mike = User("nasser", "takkesh")
# print(mike.balance)

# bob = User("nasser", "takkesh")
# print(bob.balance)

# account1 = bankAccount(.15, balance=150)

# print(account1.deposit(15).deposit(55).withdraw(20).withdraw(45).display_account_info().yield_interest())

# account1.deposit(25)
# print(account1.balance)
# account1.withdraw(15)
# print(account1.balance)
# account1.display_account_info()
# print(account1.balance)
# account1.yield_interest()
# print(account1.balance)


# nate = User("nasser", "takkesh")
# print(nate.balance)

# mike = User("nasser", "takkesh")
# print(mike.balance)

# bob = User("nasser", "takkesh")
# print(bob.balance)


# nate.make_deposit(10000000005).make_deposit(10000000005).make_deposit(10000000005).make_deposit(10000000005)
# bob.make_deposit(15).make_deposit(1342543534534435343534).make_withdrawl(342345472)
# mike.make_withdrawl(15).make_deposit(58748574875878787)
     
# print(mike.transfer_money(10000,nate))

# print(mike.balance)
# print(nate.balance)
# print(bob.balance)
