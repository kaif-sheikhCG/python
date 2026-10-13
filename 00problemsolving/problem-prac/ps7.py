A=int(input("Enter any 4 digit integer:"))
a=A//1000
b=A%1000//100
c=A%1000%100//10
d=A%1000%100%10
print("First =",a)
print("Second =",b)
print("Third =", c)
print("Last =" ,d)
if a>b and a>c and a>d:
    print("Largest = ",a)
elif b>a and b>c and b>d:
    print("Largest = ",b)
elif c>a and c>b and c>d:
    print("Largest=",c)
else:
    print("Largest=",d) 
print("sum=",a+b+c+d)
