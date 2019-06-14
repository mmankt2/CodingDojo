#!/usr/bin/python3
class BankAccount:
  def __init__(self): # don't forget to add some default values for these parameters!
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

#make 2 accounts
account1 = BankAccount()
account2 = BankAccount()

#to the first account, make 3 deposits and 1 withdrawal, then calculate
#interest and siplay account info in 1 line of code
account1.deposit(50).deposit(50).deposit(50).withdraw(200).yield_interest().display_account_info()
#to the second account, make 2 deposits, 4 withdrawals, then calculate
#interest and siplay account info in 1 line of code

account2.deposit(50).deposit(50).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()