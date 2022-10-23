class Account:

    def __init__(self,tittle,balance):
        self.tittle = tittle
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposite(self,amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):

    def __init__(self,tittle,balance,interestRate):
        super().__init__(tittle,balance)
        self.interestRate = interestRate


    def interest_Amount(self):
        interestAmount = (self.interestRate * self.balance)/100
        return interestAmount

          
tittle_ = input("Enter a tittle :- ")
balance_ = int(input("Enter a balance :- "))
interestRate_ = int(input("Enter an interest rate :- "))


SavingsAccount_obj = SavingsAccount(tittle_,balance_,interestRate_)
SavingsAccount_obj.withdrawal(int(input("Enter a withdrawal amount :- ")))
SavingsAccount_obj.deposite (int(input("Enter a deposite amount :- ")))
print(SavingsAccount_obj.getBalance())
print(SavingsAccount_obj.interest_Amount())
