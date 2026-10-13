A=int(input("Enter any 3 digit number: "))
a= A//10
b= a//10
c= a%10
d= A%10
print("The reverse of digits is:",d*100 +c*10+b)