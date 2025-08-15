import random

class Bankaccount:
    def __init__(self,acc_holder,balance):
        self.acc_number=self.generate_acc_number()
        self.acc_holder=acc_holder
        self.balance=balance
        
    @staticmethod        
    def generate_acc_number():
        return str(random.randint(10**15,(10**16)-1))

    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} deposited. New balance is {self.balance}")
            
        else:
            print("amount must be positive")

    def withdraw(self,amount):
        if amount<0:
            print("amount must be positive")

        if amount>self.balance:
            print("insuffecient balance")

        else:
            self.balance-=amount
            print(f"{amount} withdrawn. New balance is{self.balance}")

    def display_balance(self):
        print(f"current balnce is{self.balance}")

class SavingAccount(Bankaccount):
    interest_rate=4

    def apply_interest(self):
        interest=(self.balance * SavingAccount.interest_rate) / 100
        self.balance+=interest
        print(f"interest of rs.{interest} is applied {SavingAccount.interest_rate}%")
        self.display_balance()

class CurrentAccount(Bankaccount):
    overdraft_limit=5000

    def withdraw(self,amount):
        if amount<=0:
            print("withdraw amt must be postive")
            return
        if self.balance-amount<CurrentAccount.overdraft_limit:
            print("overdraft limit exceeded")
        else:
            self.balance-=amount
            print(f"withdrawn amount{amount}.New balance is{self.balance}")

def main():
    print("welcome to the bank")
    acc_type=input("Enter account type(saving/current):").strip().lower()
    name=input("enter account holder name:")
    initial_bal=float(input("enter initial balance:"))

    if acc_type=="saving":
        account=SavingAccount(name,initial_bal)
        print(f"Saving account created succesfully.\n Account number:{account.acc_number}")
        print(f"Bank fixed interest rate is{SavingAccount.interest_rate}")

    elif acc_type=="current":
        account=CurrentAccount(name,initial_bal)
        print(f"Current account created succesfully.\n Account number:{account.acc_number}")
        print(f"Bank overdraft limit is{CurrentAccount.overdraft_limit}")

    else:
        print("invalid acount type")
        return
    
    while True:
        print("1.choose operation:")
        print("2.withdraw")
        print("3.Display balance")

        if acc_type=="saving":
            print("4. Apply interst(Bank decided rate)")
            print("5. Exit")

        else:
            print("4. Exit")
    
        choice=input("enter your choice:")
        if choice=="1":
            amount=float(input("enter your amount:"))
            account.deposit(amount)

        elif choice=="2":
            amount=float(input("enter your amount:"))
            account.withdraw(amount)

        elif choice=="3":
            account.display_balance()

        elif (acc_type=="saving" and choice=="4"):
            account.apply_interest()

        elif (acc_type=="saving"and choice=="5")or(acc_type=="current" and choice=="4"):
            print(("Thank you banking with us."))
            break

        else:
            print("Invalid choice")


main()


