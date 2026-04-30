class bank:
    bank_name="INDIAN BANK"
    BRANCH="Thiruvallur"
    Type="savings"
    balance=10000
    user_name="santoo"
    account_id=210
    password=123


    def saving(self):
        print("BANK: ",self.bank_name)
        print("Balance: ",self.balance)
        print("NAME: ",self.user_name)


    def transaction(self):
        user=input("Enter a user name :")
        pw=int(input("Enter a password :"))
        ty=input("Enter 'c' has deposit or 'd' has debit (c/d):")
        if user==self.user_name and pw==self.password:
    
            if ty=="d":
                a=int(input("Enter a money: "))
                self.balance -= a
                print ("NEW Balance: ",self.balance)
                print("THANK YOU FOR VISITING")
            elif ty=="c":
            
                a=int(input("Enter a deposit money: "))
                self.balance += a
                print ("NEW Balance: ",self.balance)
                print("THANK YOU FOR VISITING")
            else:
            
                print("only : d/c")

        else:
            print("Invalid username or Password")


user1=bank()

user1.saving()

user2=bank()
user2.balance=5000
user2.user_name="rio"
user2.account_id=390
password=321

user2.saving()

user2.transaction()



        
