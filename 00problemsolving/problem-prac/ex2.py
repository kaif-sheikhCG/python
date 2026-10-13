x = int(input("Enter a number: "))

if x > 0:
    if x % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")        
else:
    if x == 0:
        print("Zero")
    else:
        if x % 2 == 0:
            print("Negative Even")
        else:
            print("Negative Odd")