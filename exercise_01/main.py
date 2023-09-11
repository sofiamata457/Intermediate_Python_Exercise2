from BankAccount import BankAccount

#class instance are instantiate
owner = BankAccount('Sofia',100)

#calling the deposit method
owner.deposit(250)

#calling the withdraw method
owner.withdraw(80)

#calling the get_balance method
print(owner.get_balance())
