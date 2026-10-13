while True:
    try:
        num = float(input("Enter a number: "))
        
        if num > 0:
            print(f"Square: {num ** 2}")
            break
        elif num < 0:
            print(f"Number as it is: {num}")
            break
        else:
            print("Error: Number cannot be zero. Please try again.\n")
            
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")