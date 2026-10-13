# Q1. Food Ordering System

choice = int(input("Enter Any Serial Number: "))

match choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Pasta")
    case 4:
        print("You selected Sandwich")
    case _:
        print("Invalid Menu Choice")


# Q2. Mobile Settings

choice = int(input("Enter Any Serial Number: "))

match choice:
    case 1:
        print("Wi-Fi Selected")
    case 2:
        print("Bluetooth Selected")
    case 3:
        print("Mobile Data Selected")
    case 4:
        print("Airplane Mode Selected")
    case 5:
        print("Exit Selected")
    case _:
        print("Invalid Setting")


# Q3. ATM Main Menu

choice = int(input("Enter Any Serial Number: "))

match choice:
    case 1:
        print("Check Balance Selected")
    case 2:
        print("Withdraw Money Selected")
    case 3:
        print("Deposit Money Selected")
    case 4:
        print("Change PIN Selected")
    case 5:
        print("Exit Selected")
    case _:
        print("Invalid Choice")


# Q4. Traffic Signal

choice = int(input("Enter Signal Number (1-Red, 2-Yellow, 3-Green): "))

match choice:
    case 1:
        print("Stop")
    case 2:
        print("Wait")
    case 3:
        print("Go")
    case _:
        print("Invalid Signal")


# Q5. Student Portal

choice = int(input("Enter Any Serial Number: "))

match choice:
    case 1:
        print("Opening Profile")
    case 2:
        print("Opening Courses")
    case 3:
        print("Opening Marks")
    case 4:
        print("Opening Attendance")
    case 5:
        print("Logging Out")
    case _:
        print("Invalid Choice")


# Q6. Online Shopping Menu

choice = int(input("Enter Any Serial Number: "))

match choice:
    case 1:
        print("Opening Electronics")
    case 2:
        print("Opening Clothing")
    case 3:
        print("Opening Books")
    case 4:
        print("Opening Grocery")
    case 5:
        print("Exit Selected")
    case _:
        print("Invalid Category")


# Q7. Banking Service Selection

choice = int(input("Enter Any Serial Number: "))

match choice:
    case 1:
        print("Opening Account Balance")
    case 2:
        print("Opening Mini Statement")
    case 3:
        print("Opening Fund Transfer")
    case 4:
        print("Opening Bill Payment")
    case 5:
        print("Opening Customer Support")
    case _:
        print("Invalid Service")


# Q8. Movie Ticket Booking

choice = int(input("Enter Any Serial Number: "))

match choice:
    case 1:
        print("Morning Show Selected")
    case 2:
        print("Afternoon Show Selected")
    case 3:
        print("Evening Show Selected")
    case 4:
        print("Night Show Selected")
    case _:
        print("Invalid Show")


# Q9. Weather Advice

choice = int(input("Enter Weather Number (1-Sunny, 2-Rainy, 3-Cloudy, 4-Snowy): "))

match choice:
    case 1:
        print("Wear sunglasses")
    case 2:
        print("Carry an umbrella")
    case 3:
        print("Weather may change")
    case 4:
        print("Wear warm clothes")
    case _:
        print("Unknown Weather")


# Q10. Payment Method

choice = int(input("Enter Payment Number (1-UPI, 2-Card, 3-Cash, 4-Wallet): "))

match choice:
    case 1:
        print("UPI Payment Selected")
    case 2:
        print("Card Payment Selected")
    case 3:
        print("Cash Payment Selected")
    case 4:
        print("Wallet Payment Selected")
    case _:
        print("Invalid Payment Method")


# Q11. File Type Detector

choice = int(input("Enter File Number (1-PDF, 2-JPG, 3-PNG, 4-MP3, 5-MP4): "))

match choice:
    case 1:
        print("Document File")
    case 2:
        print("Image File")
    case 3:
        print("Image File")
    case 4:
        print("Audio File")
    case 5:
        print("Video File")
    case _:
        print("Unknown File Type")


# Q12. User Role

choice = int(input("Enter Role Number (1-Admin, 2-Teacher, 3-Student, 4-Guest): "))

match choice:
    case 1:
        print("Full Access")
    case 2:
        print("Teacher Dashboard")
    case 3:
        print("Student Dashboard")
    case 4:
        print("Limited Access")
    case _:
        print("Invalid Role")


# Q13. Weekday or Weekend

day = int(input("Enter Day Number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")


# Q14. Customer Support Priority

priority = int(input("Enter Priority Number: "))

match priority:
    case 1 | 2:
        print("Normal Priority")
    case 3 | 4:
        print("Urgent Priority")
    case _:
        print("Invalid Priority")


# Q15. Store Discount Category

level = int(input("Enter Membership Number: "))

match level:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
    case _:
        print("Invalid Membership Level")


# Q16. University Portal

user_type = int(input("Enter User Type (1-Student, 2-Teacher): "))

match user_type:
    case 1:
        option = int(input("Enter Option: "))

        match option:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter Option: "))

        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Entering Marks")
            case 3:
                print("Opening Teacher Attendance")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid User Type")


# Q17. ATM with Account Type

account = int(input("Enter Account Type (1-Savings, 2-Current): "))

match account:
    case 1:
        print("Savings Account")
        operation = int(input("Enter Operation: "))

        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")

    case 2:
        print("Current Account")
        operation = int(input("Enter Operation: "))

        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")

    case _:
        print("Invalid Account Type")


# Q18. E-Commerce Application

category = int(input("Enter Category (1-Electronics, 2-Clothing): "))

match category:
    case 1:
        product = int(input("Enter Product Number: "))

        match product:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop Selected")
            case 3:
                print("Headphones Selected")
            case _:
                print("Invalid Product")

    case 2:
        product = int(input("Enter Product Number: "))

        match product:
            case 1:
                print("Shirt Selected")
            case 2:
                print("Jeans Selected")
            case 3:
                print("Shoes Selected")
            case _:
                print("Invalid Product")

    case _:
        print("Invalid Category")


# Q19. Food Delivery Application

category = int(input("Enter Category (1-Vegetarian, 2-Non-Vegetarian): "))

match category:
    case 1:
        food = int(input("Enter Food Number: "))

        match food:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")
            case _:
                print("Invalid Food")

    case 2:
        food = int(input("Enter Food Number: "))

        match food:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")
            case _:
                print("Invalid Food")

    case _:
        print("Invalid Category")


# Q20. Simple Calculator

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
choice = int(input("Enter Operator Number (1-Add, 2-Subtract, 3-Multiply, 4-Divide): "))

match choice:
    case 1:
        print("Result =", num1 + num2)
    case 2:
        print("Result =", num1 - num2)
    case 3:
        print("Result =", num1 * num2)
    case 4:
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot Divide By Zero")
    case _:
        print("Invalid Operator")


# Q21. Temperature Converter

choice = int(input("Enter Choice (1-Celsius to Fahrenheit, 2-Fahrenheit to Celsius): "))
temperature = int(input("Enter Temperature: "))

match choice:
    case 1:
        result = (temperature * 9 / 5) + 32
        print("Temperature =", result, "F")
    case 2:
        result = (temperature - 32) * 5 / 9
        print("Temperature =", result, "C")
    case _:
        print("Invalid Choice")


# Q22. Unit Converter

choice = int(input("Enter Choice (1-KM to M, 2-M to KM, 3-KG to G, 4-G to KG): "))
value = int(input("Enter Value: "))

match choice:
    case 1:
        print(value * 1000, "meters")
    case 2:
        print(value / 1000, "kilometers")
    case 3:
        print(value * 1000, "grams")
    case 4:
        print(value / 1000, "kilograms")
    case _:
        print("Invalid Choice")


# Q23. ATM Withdrawal

account = int(input("Enter Account Type (1-Savings, 2-Current): "))

match account:
    case 1:
        print("Savings Account")
        amount = int(input("Enter Withdrawal Amount: "))

        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case 2:
        print("Current Account")
        amount = int(input("Enter Withdrawal Amount: "))

        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case _:
        print("Invalid Account Type")
