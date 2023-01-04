#Create a Bank account with members account number, name, type of account and balance. 
# Write constructor and methods to deposit at the bank and withdraw an amount from the bank.

class BankAccount:
    def __init__(self,AccNo,AccName,AccType,AccBalance=0):
        self.number=AccNo
        self.Name=AccName
        self.Atype=AccType
        self.Balance=AccBalance
    def withdraw(self,Amount):
        if( Amount>self.Balance ):
            print("Low balance")
        else:
            self.Balance= self.Balance-Amount    
    def deposit(self,Amount):
        self.Balance= self.Balance+Amount    

accno=int(input("Enter your acc No:"))
name=input("Enter your Name:")
bala=int(input("Enter your Balance:"))
obj =BankAccount(accno, name, "Savings",bala)

print("Account Number: ",obj.number)
print("Account Name: ",obj.Name)
print("Account type: ",obj.Atype)
print("Account Balance: ",obj.Balance)
dep=int(input("Enter the value to deposite: "))
obj.deposit(dep)
print("Account Balance: ",obj.Balance)
wid=int(input("Enter the value to withdraw: "))
obj.withdraw(wid)