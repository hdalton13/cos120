"""Design a set of classes/class hierarchy for a bank
simulation program.  Multiple banks may be a part of
the simulation.  Banks service customers - people or
organizations (entities who have names and addresses,
you may assume US) that may have various types of
bank accounts. The actual types of accounts include
checking accounts, savings accounts, and credit
accounts. Common customer behaviors include adding a
type of account, removing a type of account, and
deposits, withdrawals, and obtaining a balance for
all types of accounts. Accounts are identified by a
number.  Credit and savings accounts have an interest
rate. Credit accounts have a maximum amount that can
be borrowed.  Where appropriate, create classes that
make use of inheritance or composition."""


class account:
    def __init__(self,paccNumber,pamount):
        self.accNumber=paccNumber
        self.amount=pamount
    
class savings(account):
    def __init__(self,pintRate,paccNumber,pamount):
        self.intRate=pintRate
        self.accNumber=paccNumber
        self.amount=pamount
    
class checking(account):
    def __init__(self,pintRate,poverDraft,paccNumber,pamount):
        self.intRate=pintRate
        self.overDraft=poverDraft
        self.accNumber=paccNumber
        self.amount=pamount
    
class credit(account):
    def __init__(self,pintRate,paccNumber,pamount,pLimit):
        self.intRate=pintRate
        self.accNumber=paccNumber
        self.amount=pamount
        self.limit=pLimit
    
class customer:
    def __init__(self,pname,paddr,pssn):
        self.name=pname
        self.addr=paddr
        self.ssn=pssn
    
class teller:
    def __init__(self,pname,paddr,pssn,ppayRate):
        self.name=pname
        self.addr=paddr
        self.ssn=pssn
        self.payRate=ppayRate
    
class bank:
    def __init__(self):
        pass
    def addCustomers(self,customer):
        pass
    def showCustomers(self):
        pass
    def findAccounts(self,customer)
    
#1) Declare a bank
#2) Declare 4 customers
#3) Add three of the customers to the bank
#4) Show all of the customers for the bank
#5) Display all accounts for a customer who exists
#6) Display all accounts for a customer who does not exist
#7) Add a checking and a savings account for one of the customers
#8) Now display all accounts for the customer with the accounts you just added
Sovereign=bank()
Bob=customer("Bob","123 Main","123-45-0000")
Sue=customer("Sue","124 Main","123-45-1111")
Joe=customer("Joe","125 Main","123-45-2222")
Jamie=customer("Jamie","126 Main","123-45-5678")
Sovereign.addCustomers(Bob)
Sovereign.addCustomers(Sue)
Sovereign.addCustomers(Joe)
print("Show Customers",Sovereign.showCustomers())
print("Find accounts for Bob",Sovereign.findAccounts(Bob))
print("Find accounts for Jamie",Sovereign.findAccounts(Jamie))
Bob.add_savings(1000)
Bob.add_checking(100,50)
print("Find accounts for Bob",Sovereign.findAccounts(Bob))
