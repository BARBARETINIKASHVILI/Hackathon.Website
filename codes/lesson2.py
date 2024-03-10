class BankAccount: 
  
    
    # def-ით შევქმენით რამოდენიმე ცვლადი და დავიხმარეთ self-ი რომ შევქმნათ ახალი ცვლადებიც
    def __init__(self, account_number, account_holder, balance=0): 
        self_account_number = account_number
        self_account_holder = account_holder
        self_balance = balance

#ვქმნით def-ს რომლის დახმარებითაც შეგვაქ ფული
    def deposit(self, amount):
        if amount > 0:
            self_balance += amount
            print("Deposited ${amount}. New balance: ${self_balance}")
        else:
            print("Invalid Deposit Amount. Please Enter A Positive Value.")


#ვქმნით def-ს რომლის დახმარებითაც შეგვიძლია გამოვიტანოთ ფული
    def withdraw(self, amount):
        if 0 < amount <= self_balance:
            self_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self_balance}")
        else:
            print("Invalid Withdrawal Amount Or Insufficient Funds.")
        def get_balance(self):
            return self_balance

#ვქმნით def-ს რომლის დახმარებითაც გვაქვს 2 აქქაუნთი
        def main():
            account1 = BankAccount(account_number=1, account_holder="Nikolozi popkhadze", balance=190)
            account2 = BankAccount(account_number=2, account_holder="Daniel Abramiani", balance=157)
        
            q1 =str(input("Would you like to see your initial balances?"))
            if q1=="yes":
                print("Initial balances:")
                print(f"Account {account1.account_number}: ${account1.get_balance()}")
                print(f"Account {account2.account_number}: ${account2.get_balance()}")
            elif q1=="no":
                print("ok")
#ვეკითხებით მომხმარებელის სახელს თუ სახელი უდრის ნიკოლოზს დაწეროს ნიკოლოზის ინფორმაცია ან თუ დანიელს უდრის დაწეროს დანიელის ინფორმაცია
            name = str(input("What Is Your Username"))
            if name =="Nikolozi Popkhadze":
                print(f"Account {account1.account_number}: ${account1.get_balance()}")

            elif name =="Daniel Abramiani":
                print(f"Account {account2.account_number}: ${account2.get_balance()}")

            else:
                print("That IS Not A Valid Name.")


            account1.deposit(500)
            account2.withdraw(200)
            #პრინტავს საბოოლო ბალნსებს
            print("\nFinal balances:")
            #ვიღებთ თითო თითო აქაუნთის ბალანსებს
            print(f"Account {account1.account_number}: ${account1.get_balance()}")
            print(f"Account {account2.account_number}: ${account2.get_balance()}")
            #თუ სახელი == main-ს რომელიც გამოყენებულია 29-ე ხაზზე ვწერთ მაგას რაც არის მაგ ხაზზე გამოყენებული 
            if __name__ == "__main":
                main()

#მორჩა :D