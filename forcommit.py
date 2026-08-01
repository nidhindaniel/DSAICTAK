account_name = "Nidhin Daniel"
account_number = "1234567890"
balance = [5000.0]  


def check_balance():
    
    print("Current Balance is", balance[0])
    print("Account Name: " + account_name)
    print("Account Number: " + account_number)


def deposit(amount):
    while amount <= 0:
        print("Amount Cannot be less than or equal to 0")
        amount = float(input("You can enter the amount to be deposited: "))

    balance[0] += amount
    print("Deposited:", amount)


def withdraw(amount):
   
    if amount <= balance[0]:
        balance[0] -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient balance.")


print(" BANK ACCOUNT MANAGER ")
print("1. Deposit")
print("2. Withdrawal")
print("3. Check Balance")
print("4. Exit")

choice = int(input("Enter your choice: "))
if choice == 1:
    amount = float(input("Enter the amount to deposit: "))
    deposit(amount)
elif choice == 2:
    amount = float(input("Enter the Amount to be Withdrawn: "))
    withdraw(amount)
elif choice == 3:
    check_balance()
elif choice == 4:
    print("Thank You ")
else:
    print("Invalid Choice")