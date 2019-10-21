class User():
    def __init__ (self,first, last_name):
        self.first_name = first
        self.last_name = last_name
        self.email = first + '.' + last_name + '@gmail.com'
        self.balance = 0

    def make_deposit(self, amount):     
        self.balance += amount

    def make_withdrawl(self, amount):     
        self.balance -= amount

    def transfer_money(self, amount, toWho):
        self.balance -= amount
        toWho.balance +=amount


nate = User("nasser", "takkesh")
print(nate.balance)

mike = User("nasser", "takkesh")
print(mike.balance)

bob = User("nasser", "takkesh")
print(bob.balance)

     
print(mike.transfer_money(10000,nate))





nate.make_deposit(15)
nate.make_deposit(15)
nate.make_deposit(15)
nate.make_deposit(15)
nate.make_deposit(15)
nate.make_deposit(15)


bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)
bob.make_deposit(15)

mike.make_withdrawl(15)

nate.make_withdrawl(15)
nate.make_withdrawl(15)
nate.make_withdrawl(15)
nate.make_withdrawl(15)



print(mike.balance)
print(nate.balance)
print(bob.balance)



print(mike.balance)
print(nate.balance)
print(bob.balance)

