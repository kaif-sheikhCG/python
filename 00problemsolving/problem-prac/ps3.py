A=int(input("Enter any 3 digit number: "))
a= A//10
b= a//10
c= a%10
d= A%10
if b==d:
    print("The number is palindrome")
else:
    print("The number is not palindrome")