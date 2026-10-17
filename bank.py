balance = 30000

def withdrawal():
    global balance

    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)


def deposit():
    global balance

    amount = int(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Please enter a valid amount.")
    else:
        balance = balance + amount
        print("Deposit successful!")
        print("Updated balance:", balance)


def checkbalance():
    print("Your current balance is:", balance)


while True:
    print("===== BANK APP =====")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        withdrawal()
        
    elif choice == 2:
        deposit()
        
    elif choice == 3:
        checkbalance()
        
    elif choice == 4:
        print("Thank you for using our bank app!")
        break
    else:
        print("Invalid choice! Please try again.")
