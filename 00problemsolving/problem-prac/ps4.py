A=int(input("Enter any integer number:"))
if A%5==0 and A%3==0:
    print("The number is divisible by both 5 and 3")
elif A%5==0 and A%3!=0:
    print("The number is divisible by 5 but not by 3")
elif A%3==0 and A%5!=0:
    print("The number is divisible by 3 but not by 5")
else:
    print("The number is not divisible by both 5 and 3")