class User():
    def __init__ (self,first, last_name):
        self.first_name = first
        self.last_name = last_name
        self.email = first + '.' + last_name + '@gmail.com'
        self.balance = 0

    def make_deposit(self, amount):     
        self.balance += amount
        return self

    def make_withdrawl(self, amount):     
        self.balance -= amount
        return self
    def transfer_money(self, amount, toWho):
        self.balance -= amount
        toWho.balance +=amount
        return self


nate = User("nasser", "takkesh")
print(nate.balance)

mike = User("nasser", "takkesh")
print(mike.balance)

bob = User("nasser", "takkesh")
print(bob.balance)


nate.make_deposit(10000000005).make_deposit(10000000005).make_deposit(10000000005).make_deposit(10000000005)
bob.make_deposit(15).make_deposit(1342543534534435343534).make_withdrawl(342345472)
mike.make_withdrawl(15).make_deposit(58748574875878787)
     
print(mike.transfer_money(10000,nate))

print(mike.balance)
print(nate.balance)
print(bob.balance)




