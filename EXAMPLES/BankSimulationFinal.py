class account:
    def __init__(self,paccNumber,pamount):
        self.__accNumber=paccNumber
        self.__amount=pamount
    def get_accNumber(self):
        return self.__accNumber
    def get_amount(self):
        return self.__amount
    def withdraw(self,howMuch):
        if self.__amount>howMuch:
            if howMuch > 0:
                self.__amount-=howMuch
                return True
            else:
                return False
        else:
            return False
    def deposit(self,howMuch):
        if howMuch>0:
            self.__amount+=howMuch
            return True
        else:
            return False
    def __str__(self):
        return self.__accNumber
        
class savings(account): #(account)<==inheritance
    def __init__(self,pintRate,paccNumber,pamount):
        super().__init__(paccNumber,pamount) #extending
        self.__intRate=pintRate
        
class checking(account):
    def __init__(self,pintRate,poverDraft,paccNumber,pamount):
        super().__init__(paccNumber,pamount)
        self.__intRate=pintRate
        self.__overDraft=poverDraft

class credit(account):
    def __init__(self,pintRate,paccNumber,pamount,pLimit):
        super().__init__(paccNumber,pamount)
        self.__intRate=pintRate
        self.__limit=pintRate

class customer:
    def __init__(self,pname,paddr,pssn):
        self.__name=pname
        self.__addr=paddr
        self.__ssn=pssn
        self.__accounts=[]
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__addr
    def get_ssn(self):
        return self.__ssn
    def get_accounts(self):
        lst=[]
        for obj in self.__accounts:
            lst.append([obj.get_accNumber(),obj.get_amount()])
        return lst
    def add_savings(self,startAmt):
        self.__accounts.append(savings(.05,self.__ssn+"SAV",startAmt))
    def add_checking(self,startAmt,poverDraft):
        self.__accounts.append(checking(.05,poverDraft,self.__ssn+"CHK",startAmt))

class teller:
    def __init__(self,pname,paddr,pssn,ppayRate):
        self.__name=pname
        self.__addr=paddr
        self.__ssn=pssn
        self.__payRate=pssn
    
class bank:
    def __init__(self):
        self.customers={}
    def addCustomers(self,customerObj):
        self.customers[customerObj.get_ssn()]=customerObj
    def showCustomers(self):
        customerList=[]
        for key in self.customers:
            customerList.append(key+" "+self.customers[key].get_name())
        return customerList
    def findAccounts(self,customerObj):
        for customerKey in self.customers:
            if self.customers[customerKey].get_ssn()==customerObj.get_ssn():
                return self.customers[customerKey].get_accounts()
        return "no such customer"

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
