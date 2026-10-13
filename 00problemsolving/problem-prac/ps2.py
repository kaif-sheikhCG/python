a,b,c=map(int,input("enter 3 numbers: ").split()[0:3])
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")