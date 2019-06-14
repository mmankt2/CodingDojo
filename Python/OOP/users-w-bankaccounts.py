#!/usr/bin/python3

class User:		# here's what we have so far
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account = BankAccount(int_rate = 0.02,balance =0)
    # adding the deposit method
  def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    self.account.deposit(amount)	#call the BankAccount deposit method
    return self
  def make_withdrawal(self, amount): #taks an argument that is the amount of the withdrawal
    self.account.withdraw(amount) #call the BankAccount withdraw method
    return self
  def display_user_balance(self): #print the user's name and account balance
    print("{}: ${}".format(self.name,self.account.balance))
    return self

class BankAccount:
  def __init__(self,int_rate,balance): # don't forget to add some default values for these parameters!
		# your code here! (remember, this is where we specify the attributes for our class)
    # don't worry about user info here; we'll involve the User class soon
    self.int_rate = 0.01
    self.balance = 0
  def deposit(self, amount):#increases the account balance by the given amount
		# your code here
    self.balance += amount
    return self
  def withdraw(self, amount):#decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    # your code here
    if self.balance < amount:
      print("Insufficient funds: Charging a $5 fee.")
      self.balance = self.balance - 5
      return self
    else:
      self.balance = self.balance - amount
    return self
  def display_account_info(self):#print to the console: eg. "Balance: $100"
    # your code here
    print("Balance: ${}".format(self.balance))
    return self
  def yield_interest(self):#ncreases the account balance by the current balance * the interest rate (as long as the balance is positive)
    # your code here
    self.balance = self.balance + self.balance * self.int_rate
    return self

melissa = User("Melissa Littleton","mmankt2@gmail.com")
melissa.make_deposit(50).make_withdrawal(25).display_user_balance()