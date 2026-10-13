x = int(input("Enter a number to know if its prime :"))
count=0
for i in range(1,x+1):
    if x%i==0:
        count=count+1
if count==2:
    print(x,"is prime a number")
else:
    print(x,"is not prime a number")