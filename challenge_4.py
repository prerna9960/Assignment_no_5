class Account:

    def __init__(self,tittle= None,balance= 0):
        self.tittle = tittle
        self.balance = balance
      
class SavingsAccount(Account):

    def __init__(self,interestRate,tittle,balance):
        self.interestRate = interestRate
        super().__init__(tittle,balance)
tittle_ = input("Enter tittle :- ")
balance_= input("Enter balance :- ")
interset_Rate = input("Enter interestRate :- ")

SavingsAccount_obj = SavingsAccount(tittle_,balance_,interset_Rate)
print(SavingsAccount_obj)
     
        
tittle_ = input("Enter tittle :- ")
balance_= input("Enter balance :- ")
interset_Rate = input("Enter interestRate :- ")

SavingsAccount_obj = SavingsAccount(tittle_,balance_,interset_Rate)
print(SavingsAccount_obj)