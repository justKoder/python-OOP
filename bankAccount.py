# exercise 1

# customer name
# customer Id
# customer account number
class Customer:
    def __init__(self, customer_name, customer_ID, customer_account_number):
        self.customerName = customer_name
        self.customerID = customer_ID
        self.customerAccountNumber = customer_account_number

    def display(self):
        print('Customer Name : ', self.customerName)
        print('Customer ID : ', self.customerID)
        print('Customer Account Number : ', self.customerAccountNumber)


name = input("Enter Name : ")
customerId = input('Enter ID : ')
customerAccountNumber = input("Enter account Number : ")

# name of acc. holder
# acc. number
# acc. type
# balance amount


class Account(Customer):
    def __init__(self, custName, custID, accNum, typeAcc, balAcc):
        super().__init__(custName, custID, accNum)
        self.account_type = typeAcc
        self.balance = balAcc


    def deposit(self):
        amount = int(input("Enter amount ou want to deposite: "))
        self.balance = amount + self.balance

    def withdraw(self):
        amount = int(input("Enter amount you want to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance", self.balance)
        else:
            self.balance = self.balance - amount
            print('Remaining balance', self.balance)

    def printBalance(self):
        super().display()
        print("Account Balance is: ", self.balance)


account_type = input("Enter your account type [Savings/Current]: ")
account_balance = int(input("Enter initial balance of your account: "))
acc = Account(name, customerId, customerAccountNumber, account_type, account_balance)


while 1:
    print("Enter 1 to withdraw money")
    print("Enter 2 to deposite money")
    print("Enter 3 to check balance")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        acc.withdraw()
    elif choice == 2:
        acc.deposit()
    elif choice == 3:
        acc.printBalance()
    else:
        print("Invalid input")
        break
