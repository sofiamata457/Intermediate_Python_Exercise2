class BankAccount:

  #BankAccount Constructor
  def __init__(self, account_name, starting_balance):
      #attrubute stored to instance fields
      self.account_name = account_name
      self.starting_balance = starting_balance

  #method to deposit money into the account
  def deposit(self,money):
      self.starting_balance += money 

  #method to withdraw money from the account
  def withdraw(self,money):
      self.starting_balance -= money 

   #returns the name of the account owner and the amount in the account
  def get_balance(self):
       return ( f"{self.account_name} has a balance of {self.starting_balance}")