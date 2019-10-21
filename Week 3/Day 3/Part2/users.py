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
        
user1 = Users("nate", "email@here")
user2 = Users("bob", "bob@here")

user1.make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawl(200).transfer_money(user2,2000).display_user_balance()

user2.make_deposit(800).display_user_balance()


#     make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance