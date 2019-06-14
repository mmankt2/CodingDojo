#!/usr/bin/python3

class User:		# here's what we have so far
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account_balance = 0
    # adding the deposit method
  def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    self.account_balance += amount	# the specific user's account increases by the amount of the value receivedc
    return self
  def make_withdrawal(self, amount): #taks an argument that is the amount of the withdrawal
    self.account_balance = self.account_balance - amount #the specific user's account decreases by the amount of the withdrawal
    return self
  def display_user_balance(self): #print the user's name and account balance
    print("{}: ${}".format(self.name,self.account_balance))
    return self

#create 3 instances of the User classe
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
melissa = User("Melissa Littleton","mmankt2@gmail.com")

print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

#have the first user make 3 deposits and 1 withdrawal. display balance.
guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

#have the third user make 1 deposit and 3 withdrawals. display balance.
melissa.make_deposit(100).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()
