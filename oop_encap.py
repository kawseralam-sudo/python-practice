class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def deposite(self,amount):
        if amount >= 1:
            self.__balance+=amount
            print("Deposite succesfully")
        else:
            print("you have to deposite minimum one(1) taka")

    def withdraw (self,amount):
        if amount <= 0:
            self.__balance-=amount
            print("Invalide amount")
        elif amount > self.__balance:
            print("Error! Insufficient Balance")
        else:
            self.__balance-=amount
            print("withdrawal succesfull")
    
    def show_balance(self):
        print("New balance is:",self.__balance,"taka")

account=Bank(0)

deposit=int(input("Deposite balance:"))
account.deposite(deposit)

withdraw=int(input("Withdraw balance:"))
account.withdraw(withdraw)

account.show_balance()

