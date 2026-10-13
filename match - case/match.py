# exit=True
# while exit:
#     a = int(input("enter number one: "))
#     b=int(input("enter 2nd number: "))
#     print("available operators (+,-,*,/,'exit'-to exit)")
#     c=input("enter operation (+,-,*,/,'exit'-to exit) :")
    
#     match c:
#         case "+":
#             print("addition:",a+b)
#         case "-":
#                 print("subtraction:",a-b)
#         case "*":
#                 print("multiplication:",a*b)
#         case "/":
#                 print("divition:",a/b)
#         case "exit":
#                 print("exited succesfully")
#                 exit=False
#         case _:
#                 print("invalid input")

# num = int(input("Enter a number: "))

# print("\nMenu:")
# print("1. Check Even"
# "2. Check Odd"
# "3. Check Prime")


# choice = int(input("Enter your choice: "))

# match choice:
#     case 1:
#         if num % 2 == 0:
#             print("Result: Even")
#         else:
#             print("Result: Not Even")

#     case 2:
#         if num % 2 != 0:
#             print("Result: Odd")
#         else:
#             print("Result: Not Odd")

#     case 3:
#         if num < 2:
#             print("Result: Not Prime")
#         else:
#             prime = True

#             for i in range(2, num):
#                 if num % i == 0:
#                     prime = False
#                     break

#             if prime:
#                 print("Result: Prime")
#             else:
#                 print("Result: Not Prime")

#     case _:
#         print("Invalid choice")

# n = int(input("Enter a number: "))

# number = n
# digits = len(str(n))
# sum = 0

# while number > 0:
#     digit = number % 10
#     sum = sum + digit ** digits
#     number = number // 10

# if sum == n:
#     print("Armstrong")
# else:
#     print("Not an Armstrong")

# marks = 82

# match marks:
#     case x if x >= 90:
#         print("A")
#     case x if x >= 75:
#         print("B")
#     case x if x >= 60:
#         print("C")
#     case x if x >= 40:
#         print("D")
#     case _:
#         print("Fail")

print("===== WELCOME =====")

print("1. Banking")
print("2. Gas Booking")
print("3. Language")

main_choice = int(input("Enter your choice: "))

match main_choice:

    case 1:
        print("\n===== BANKING =====")
        print("1. Balance Enquiry")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")

        bank_choice = int(input("Enter your choice: "))

        pin = int(input("Enter your PIN: "))

        if pin == 1234:

            balance = 25000

            match bank_choice:

                case 1:
                    print("Your balance is ₹", balance)

                case 2:
                    amount = int(input("Enter withdrawal amount: "))

                    if amount <= balance:
                        if amount % 100 == 0:
                            balance -= amount
                            print("Withdrawal successful")
                            print("Remaining balance:", balance)
                        else:
                            print("Amount must be a multiple of ₹100")
                    else:
                        print("Insufficient balance")

                case 3:
                    amount = int(input("Enter deposit amount: "))

                    if amount > 0:
                        balance += amount
                        print("Deposit successful")
                        print("New balance:", balance)
                    else:
                        print("Invalid amount")

                case 4:
                    old_pin = int(input("Enter old PIN: "))

                    if old_pin == 1234:
                        new_pin = int(input("Enter new PIN: "))
                        print("PIN changed successfully")
                    else:
                        print("Incorrect old PIN")

                case _:
                    print("Invalid banking option")

        else:
            print("Incorrect PIN")

    case 2:
        print("\n===== GAS BOOKING =====")
        print("1. Book Gas Cylinder")
        print("2. Check Booking Status")
        print("3. Cancel Booking")
        print("4. Check Gas Price")

        gas_choice = int(input("Enter your choice: "))

        match gas_choice:

            case 1:
                print("\nSelect Gas Company")
                print("1. Indane")
                print("2. Bharat Gas")
                print("3. HP Gas")

                company = int(input("Enter company: "))

                match company:

                    case 1:
                        print("Indane Gas selected")

                    case 2:
                        print("Bharat Gas selected")

                    case 3:
                        print("HP Gas selected")

                    case _:
                        print("Invalid company")
                        exit()

                print("\nSelect Cylinder Type")
                print("1. Domestic")
                print("2. Commercial")

                cylinder = int(input("Enter cylinder type: "))

                match cylinder:

                    case 1:
                        price = 900
                        print("Domestic cylinder selected")

                    case 2:
                        price = 1800
                        print("Commercial cylinder selected")

                    case _:
                        print("Invalid cylinder type")
                        exit()

                print("Cylinder price: ₹", price)

                confirm = input("Confirm booking? (yes/no): ")

                match confirm.lower():

                    case "yes":
                        print("Gas cylinder booked successfully!")

                    case "no":
                        print("Booking cancelled")

                    case _:
                        print("Invalid input")

            case 2:
                print("Booking Status: Delivered")

            case 3:
                confirm = input("Are you sure you want to cancel? (yes/no): ")

                match confirm.lower():

                    case "yes":
                        print("Booking cancelled successfully")

                    case "no":
                        print("Cancellation stopped")

                    case _:
                        print("Invalid input")

            case 4:
                print("\nSelect Cylinder Type")
                print("1. Domestic")
                print("2. Commercial")

                cylinder = int(input("Enter choice: "))

                match cylinder:

                    case 1:
                        print("Domestic Gas Price: ₹900")

                    case 2:
                        print("Commercial Gas Price: ₹1800")

                    case _:
                        print("Invalid choice")

            case _:
                print("Invalid gas option")

    case 3:
        print("\n===== LANGUAGE =====")
        print("1. English")
        print("2. Hindi")
        print("3. Gujarati")

        language = int(input("Select language: "))

        match language:

            case 1:
                print("Language changed to English")

            case 2:
                print("भाषा हिंदी में बदल दी गई है")

            case 3:
                print("ભાષા ગુજરાતીમાં બદલવામાં આવી છે")

            case _:
                print("Invalid language")

    case _:
        print("Invalid main option")