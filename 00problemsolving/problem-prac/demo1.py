#1st method

stri = input("Enter str to know palindrome: ").strip().lower()
leng = len(stri)
sum=""
for ele in range(leng - 1,-1,-1):
    sum=sum+stri[ele]
if sum==stri:
    print(stri,"is a palindorme")
else:
    print(stri,"is not a palindorome")

#2nd method

stri = input("Enter str to know palindrome: ").strip().lower()
palindrome=False
for i in stri:
    if stri[::1]==stri[::-1]:
        palindrome=True
    else:
        palindrome=False
print("palindrome:",palindrome)