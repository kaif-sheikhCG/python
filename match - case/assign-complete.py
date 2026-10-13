question = int(input("Enter question number (1-34): "))

match question:

    # Q1
    case 1:
        choice = int(input("Enter your choice: "))
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

    # Q2
    case 2:
        choice = int(input("Enter choice: "))
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

    # Q3
    case 3:
        choice = int(input("Enter choice: "))
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

    # Q4
    case 4:
        signal = input("Enter signal: ").lower()
        match signal:
            case "red":
                print("Stop")
            case "yellow":
                print("Wait")
            case "green":
                print("Go")
            case _:
                print("Invalid Signal")

    # Q5
    case 5:
        choice = int(input("Enter choice: "))
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
                print("Logged Out")
            case _:
                print("Invalid Choice")

    # Q6
    case 6:
        choice = int(input("Enter category: "))
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

    # Q7
    case 7:
        choice = int(input("Enter service: "))
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

    # Q8
    case 8:
        choice = int(input("Enter show: "))
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

    # Q9
    case 9:
        weather = input("Enter weather: ").lower()
        match weather:
            case "sunny":
                print("Wear sunglasses")
            case "rainy":
                print("Carry an umbrella")
            case "cloudy":
                print("Weather may change")
            case "snowy":
                print("Wear warm clothes")
            case _:
                print("Unknown Weather")

    # Q10
    case 10:
        payment = input("Enter payment method: ").lower()
        match payment:
            case "upi":
                print("UPI Payment Selected")
            case "card":
                print("Card Payment Selected")
            case "cash":
                print("Cash Payment Selected")
            case "wallet":
                print("Wallet Payment Selected")
            case _:
                print("Invalid Payment Method")

    # Q11
    case 11:
        extension = input("Enter extension: ").lower().lstrip(".")
        match extension:
            case "pdf":
                print("Document")
            case "jpg" | "png":
                print("Image")
            case "mp3":
                print("Audio File")
            case "mp4":
                print("Video File")
            case _:
                print("Unknown File Type")

    # Q12
    case 12:
        role = input("Enter role: ").lower()
        match role:
            case "admin":
                print("Full Access")
            case "teacher":
                print("Teacher Dashboard")
            case "student":
                print("Student Dashboard")
            case "guest":
                print("Limited Access")
            case _:
                print("Invalid Role")

    # Q13
    case 13:
        day = int(input("Enter day number: "))
        match day:
            case 1 | 2 | 3 | 4 | 5:
                print("Weekday")
            case 6 | 7:
                print("Weekend")
            case _:
                print("Invalid Day")

    # Q14
    case 14:
        priority = int(input("Enter priority: "))
        match priority:
            case 1 | 2:
                print("Normal Priority")
            case 3 | 4:
                print("Urgent Priority")
            case _:
                print("Invalid Priority")

    # Q15
    case 15:
        level = int(input("Enter membership level: "))
        match level:
            case 1 | 2:
                print("Basic Membership")
            case 3 | 4:
                print("Premium Membership")
            case _:
                print("Invalid Membership")

    # Q16
    case 16:
        user_type = int(input("Enter user type: "))
        match user_type:
            case 1:
                option = int(input("Enter option: "))
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
                option = int(input("Enter option: "))
                match option:
                    case 1:
                        print("Opening Teacher Students")
                    case 2:
                        print("Opening Teacher Marks Entry")
                    case 3:
                        print("Opening Teacher Attendance")
                    case _:
                        print("Invalid Option")
            case _:
                print("Invalid User Type")

    # Q17
    case 17:
        account = int(input("Enter account type: "))
        match account:
            case 1:
                print("Savings Account")
                operation = int(input("Enter operation: "))
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
                operation = int(input("Enter operation: "))
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

    # Q18
    case 18:
        category = int(input("Enter category: "))
        match category:
            case 1:
                product = int(input("Enter product: "))
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
                product = int(input("Enter product: "))
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

    # Q19
    case 19:
        category = int(input("Enter category: "))
        match category:
            case 1:
                food = int(input("Enter food: "))
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
                food = int(input("Enter food: "))
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

    # Q20
    case 20:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operator = input("Enter operator: ")
        match operator:
            case "+":
                print("Result =", a + b)
            case "-":
                print("Result =", a - b)
            case "*":
                print("Result =", a * b)
            case "/":
                if b != 0:
                    print("Result =", a / b)
                else:
                    print("Cannot divide by zero")
            case _:
                print("Invalid Operator")

    # Q21
    case 21:
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                temp = float(input("Enter temperature: "))
                print("Temperature =", (temp * 9 / 5) + 32, "F")
            case 2:
                temp = float(input("Enter temperature: "))
                print("Temperature =", (temp - 32) * 5 / 9, "C")
            case _:
                print("Invalid Choice")

    # Q22
    case 22:
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                value = float(input("Enter value: "))
                print(value * 1000, "meters")
            case 2:
                value = float(input("Enter value: "))
                print(value / 1000, "kilometers")
            case 3:
                value = float(input("Enter value: "))
                print(value * 1000, "grams")
            case 4:
                value = float(input("Enter value: "))
                print(value / 1000, "kilograms")
            case _:
                print("Invalid Choice")

    # Q23
    case 23:
        account = int(input("Enter account type: "))
        match account:
            case 1:
                print("Savings Account")
                amount = float(input("Enter amount: "))
                if amount > 0:
                    print("Withdrawal Request Accepted")
                else:
                    print("Invalid Amount")
            case 2:
                print("Current Account")
                amount = float(input("Enter amount: "))
                if amount > 0:
                    print("Withdrawal Request Accepted")
                else:
                    print("Invalid Amount")
            case _:
                print("Invalid Account Type")

    # Q24
    case 24:
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                age = int(input("Enter age: "))
                if age >= 18:
                    print("You can start the exam")
                else:
                    print("You cannot start the exam")
            case 2:
                print("Viewing Result")
            case 3:
                print("Exiting Portal")
            case _:
                print("Invalid Choice")

    # Q25
    case 25:
        ticket = int(input("Enter ticket type: "))
        match ticket:
            case 1:
                ticket_name = "Regular Ticket"
            case 2:
                ticket_name = "Premium Ticket"
            case 3:
                ticket_name = "VIP Ticket"
            case _:
                ticket_name = ""
                print("Invalid Ticket Type")

        if ticket_name != "":
            age = int(input("Enter age: "))
            if age < 5:
                print("Free Entry")
            else:
                print(ticket_name)

    # Q26
    case 26:
        device = int(input("Enter device: "))
        match device:
            case 1:
                print("Light Controller Opened")
            case 2:
                print("Fan Controller Opened")
            case 3:
                print("AC Controller Opened")
            case 4:
                print("TV Controller Opened")
            case _:
                print("Invalid Device")

    # Q27
    case 27:
        choice = int(input("Enter department: "))
        match choice:
            case 1:
                print("General Medicine Selected")
            case 2:
                print("Cardiology Selected")
            case 3:
                print("Orthopedics Selected")
            case 4:
                print("Pediatrics Selected")
            case 5:
                print("Emergency Selected")
            case _:
                print("Invalid Department")

    # Q28
    case 28:
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                print("Book Ticket Selected")
            case 2:
                print("Cancel Ticket Selected")
            case 3:
                print("Check PNR Selected")
            case 4:
                print("Train Schedule Selected")
            case 5:
                print("Exit Selected")
            case _:
                print("Invalid Choice")

    # Q29
    case 29:
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                print("Searching Book")
            case 2:
                print("Issuing Book")
            case 3:
                print("Returning Book")
            case 4:
                print("Viewing Issued Books")
            case 5:
                print("Exiting Library")
            case _:
                print("Invalid Choice")

    # Q30
    case 30:
        status = input("Enter status: ").lower()
        match status:
            case "placed":
                print("Your order has been placed")
            case "confirmed":
                print("Your order has been confirmed")
            case "preparing":
                print("Your order is being prepared")
            case "out_for_delivery":
                print("Your order is on the way")
            case "delivered":
                print("Your order has been delivered")
            case "cancelled":
                print("Your order has been cancelled")
            case _:
                print("Invalid Order Status")

    # Q31
    case 31:
        banking_type = int(input("Enter banking type: "))
        match banking_type:
            case 1:
                option = int(input("Enter option: "))
                match option:
                    case 1:
                        print("Personal Balance Selected")
                    case 2:
                        print("Personal Transfer Selected")
                    case 3:
                        print("Personal Loan Selected")
                    case _:
                        print("Invalid Option")
            case 2:
                option = int(input("Enter option: "))
                match option:
                    case 1:
                        print("Business Balance Selected")
                    case 2:
                        print("Payroll Selected")
                    case 3:
                        print("Business Loan Selected")
                    case _:
                        print("Invalid Option")
            case _:
                print("Invalid Banking Type")

    # Q32
    case 32:
        user_type = int(input("Enter user type: "))
        match user_type:
            case 1:
                option = int(input("Enter option: "))
                match option:
                    case 1:
                        print("Viewing Student Marks")
                    case 2:
                        print("Viewing Student Attendance")
                    case 3:
                        print("Viewing Student Homework")
                    case _:
                        print("Invalid Option")
            case 2:
                option = int(input("Enter option: "))
                match option:
                    case 1:
                        print("Entering Marks")
                    case 2:
                        print("Viewing Attendance")
                    case 3:
                        print("Assigning Homework")
                    case _:
                        print("Invalid Option")
            case 3:
                option = int(input("Enter option: "))
                match option:
                    case 1:
                        print("Viewing Child Marks")
                    case 2:
                        print("Viewing Child Attendance")
                    case 3:
                        print("Contacting Teacher")
                    case _:
                        print("Invalid Option")
            case _:
                print("Invalid User Type")

    # Q33
    case 33:
        transport = int(input("Enter transport: "))
        match transport:
            case 1:
                option = int(input("Enter option: "))
                match option:
                    case 1:
                        print("Economy Selected")
                    case 2:
                        print("Business Selected")
                    case _:
                        print("Invalid Option")
            case 2:
                option = int(input("Enter option: "))
                match option:
                    case 1:
                        print("Sleeper Selected")
                    case 2:
                        print("AC Selected")
                    case _:
                        print("Invalid Option")
            case 3:
                option = int(input("Enter option: "))
                match option:
                    case 1:
                        print("Ordinary Selected")
                    case 2:
                        print("Volvo Selected")
                    case _:
                        print("Invalid Option")
            case _:
                print("Invalid Transport")

    # Q34
    case 34:
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                print("Starting Game")
            case 2:
                print("Loading Game")
            case 3:
                setting = int(input("Enter setting: "))
                match setting:
                    case 1:
                        print("Sound Settings Opened")
                    case 2:
                        print("Graphics Settings Opened")
                    case 3:
                        print("Controls Settings Opened")
                    case _:
                        print("Invalid Setting")
            case 4:
                print("Exiting Game")
            case _:
                print("Invalid Choice")
