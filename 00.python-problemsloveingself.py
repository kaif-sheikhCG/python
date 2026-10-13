# # Q2
# fail = 0
# ok = 0
# good = 0
# great = 0
# for i in range(10):
#     m = int(input("Enter marks: "))
#     if m < 35:
#         print("Fail")
#         fail += 1
#     elif m < 50:
#         print("Pass")
#         ok += 1
#     elif m < 75:
#         print("Good")
#         good += 1
#     else:
#         print("Excellent")
#         great += 1
# print("Fail:", fail)
# print("Pass:", ok)
# print("Good:", good)
# print("Excellent:", great)

# #Q3

# string=input("enter")
# words = string.split()
 
# vowels = "aeiouAEIOU"
# highest_score =0
# highest_word = ""
 
# for i in words:
#     score = 0
#     for ch in i:
#         if ch in vowels:
#             score += 2
#         elif ch.isdigit():
#             score += 3
#         elif ch.isalpha():
#             score += 1
#         else:
#             score += 4
#     print(f"{i}={score}")
#     if score > highest_score:
#         highest_score = score
#         highest_word =i
 
# print("Highest scoring word:", highest_word, "with score", highest_score)

# # Q4
# for i in range(1,6):
#     p = input("Enter password: ")
#     count = 0
#     up = 0
#     low = 0
#     num = 0
#     sp = 0
#     for ch in p:
#         if ch >= "A" and ch <= "Z":
#             up = 1
#         elif ch >= "a" and ch <= "z":
#             low = 1
#         elif ch.isdigit():
#             num = 1
#         else:
#             sp = 1
#     if len(p) >= 8:
#         count += 1
#     count = count + up + low + num + sp
#     if count == 5:
#         print("Strong")
#     elif count >= 3:
#         print("Medium")
#     else:
#         print("Weak")

# #Q5.
# sen="you are soo funny"
# words=sen.split()
# count1=0
# count2=0
# count3=0
# for i in words:
#     print(i,len(i))
#     if len(i)<=3:
#         count1+=1
#         print("short")
#     elif len(i)>=4 and len(i)<=6:
#         count2+=1
#         print("medium")
#     else:
#         count3+=1
#         print("long")

# print(count1)
# print(count2)
# print(count3)

# #Q6.
# for i in range(5):
#     num = int(input("Enter a number: "))
#     num1 = str(num)

#     even = 0
#     odd = 0

#     for ch in num1:
#         if int(ch) % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     print("Even =", even)
#     print("Odd =", odd)

#     if even > odd:
#         print("Even occurs more")
#     elif odd > even:
#         print("Odd occurs more")
#     else:
#         print("Equal")


# #Q7.
# text = input("Enter a string: ")

# for ch in text:
#     count = 0

#     for x in text:
#         if ch == x:
#             count += 1

# if count > 1:
#     if count == 2:
#         print(ch, "Duplicate")
#     elif count <= 4:
#         print(ch, "Repeated")
#     else:
#         print(ch, "Highly Repeated")

# #Q8.
# total = 0

# budget = 0
# regular = 0
# premium = 0
# luxury = 0

# for i in range(8):

#     price = int(input("Enter price: "))

#     total += price

#     if price < 500:
#         print("Budget")
#         budget += 1

#     elif price <= 1999:
#         print("Regular")
#         regular += 1

#     elif price <= 4999:
#         print("Premium")
#         premium += 1

#     else:
#         print("Luxury")
#         luxury += 1

# average = total / 8

# print("Total amount:", total)
# print("Budget products:", budget)
# print("Regular products:", regular)
# print("Premium products:", premium)
# print("Luxury products:", luxury)
# print("Average price:", average)

# #Q9.
# name="1Achal1" #input("enter a string")
# vowel="aeiouAEIOU"
# count=0
# v=0
# c=0
# d=0
# sc=0
# for ch in name:
#     print(ch)
#     print(name.index(ch))
#     if name.index(ch)%2==0:
#         print("even position")
#     else:
#         print("odd position")
#     if ch in vowel:
#         print("chracter is a vowel")
#         v+=1
#     elif ch.isdigit():
#         print("ch is digit")
#         d+=1
#     elif ch.isalpha:
#         print("ch is a consonent")
#         c+=1
#     else:
#         print("ch is special")
#         sc+=1

# print("vowel",v)
# print("consonents",c)
# print("digit",d)
# print("special",sc)

# #Q10.
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j%3==0 and j%5==0:
#             print("z",end=" ")
#         elif j%3==0:
#             print("x",end=" ")
#         elif j%5==0:
#             print("Y",end=" ")
#         else:
#             print(j,end=" ")
#     print()

# #Q11.
# invalid=False
# for i in range(5):
#     username=input("enter your username...")
#     print("length=",len(username))
#     print("First character=",username[0])
#     countd=0
#     countu=0
#     for ch in username:
#         if ch.isdigit():
#             countd+=1
#         elif ch=="_":
#             countu+=1
#         else:
#             invalid=True
#     print("digit",countd)             
#     print("underscore",countu)

#     if invalid:
#         print("invalid")
#     elif not ch.isdigit() and not ch.isalpha:
#         print("need improvement")
#     else:
#         print("valid")


# for i in range(5):

#     username = input("Enter username: ")

#     digits = 0
#     underscores = 0
#     invalid = False


#     length = len(username)
#     first = username[0]

#     for ch in username:

#         if ch.isdigit():
#             digits += 1

#         elif ch == "_":
#             underscores += 1

#         elif ch.isalpha():
#             pass

#         else:
#             invalid = True


#     if invalid:
#         print("Invalid")

#     elif not first.isalpha():
#         print("Invalid")

#     elif length < 5:
#         print("Needs Improvement")

#     elif length >= 5:
#         print("Valid")

#     print("Length:", length)
#     print("First character:", first)
#     print("Digits:", digits)
#     print("Underscores:", underscores)

# #Q12.
# sen=input("type a sentence")
# words=sen.split()
# vowels="aeiouAEIOU"
# vowel=0
# con=0
# for word in words:
#     for ch in word:
#         if ch in vowels:
#             vowel+=1
#         else:
#             con+=1
# print("Vowels=",vowel)
# print("Consonents=",con)
# if vowel>con:
#     print("vowel wins")
# elif vowel==con:
#     print("Tei")
# else:
#     print("Con wins")

# #Q13.
# for i in range(6):
#     units=int(input("Enter the no. of units"))
#     bill=0
#     if units<=100:
#         bill=5*units
#     elif units<=200:
#         bill=(5*100)+7*(units-100)
#     elif units<=400:
#         bill=(5*100)+(7*100)+10*(units-100)
#     elif units>400:
#         bill=(5*100)+(7*100)+(10*units)+15*(units-100)

#     print(bill)
#     if bill<1000:
#         print("low")
#     elif bill<=3000 and bill>=1000:
#         print("medium")
#     else:
#         print("high")

# #Q14.
# sen=input("enter a sentence")
# words=sen.split()
# vowels="aeiouAEIOU"
# vowel=0
# con=0
# for word in words:
#     for  ch in word:
#         if ch in vowels:
#             vowel+=1
#         elif ch.isalpha():
#             con+=1
# print(vowel)
# print(con)
# if vowel>con:
#     print("vowel heavy")
# elif con>vowel:
#     print("con heavy")
# else:
#     print("balanced")

# #Q15.
# matrix = []
# even=0
# odd=0
# positive=0
# negative=0
# zero=0
# largest=0
# for i in range(3):
#     row = []
#     for j in range(3):
#         num = int(input("Enter number: "))
#         row.append(num)
#     matrix.append(row)
# print(matrix)

# for i in matrix:
#     for ch in i:
#         if ch%2==0:
#             print(ch,"=even")
#             even+=0
#         else:
#             print(ch,"=odd")
#             odd+=1
#         if ch>0:
#             print("Positive")
#             positive+=1
#         elif ch<0:
#             print("Negative")
#             negative+=1
#         else:
#             print("zero")
#             zero+=1
#         if ch>largest:
#             largest=ch

# print("even count=",even)
# print("odd count=",odd)
# print(positive)
# print(negative)
# print(zero)
# print(largest)

# #Q16.
# password=input("enter a password")
# lenth=len(password)
# upper=0
# lower=0
# digit=0
# special=0
# for ch in password:
#     if ch.isupper():
#         upper+=1
#     elif ch.islower():
#         lower+=1
#     elif ch.isdigit():
#         digit+=1
#     else:
#         special+=1
# total=len(password)
# print("upper count=",upper)
# print("%",upper/total*100)
# print("lower count=",lower)
# print("%",lower/total*100)
# print("digit count=", digit)
# print("%",digit/total*100)
# print("special count", special)
# print("%",special/total*100)


# # Q17
# best = -1
# best_name = ""
# for i in range(5):
#     name = input("Enter name: ")
#     m = int(input("Enter marks: "))
#     if m >= 90:
#         grade = "A+"
#     elif m >= 75:
#         grade = "A"
#     elif m >= 60:
#         grade = "B"
#     elif m >= 50:
#         grade = "C"
#     elif m >= 35:
#         grade = "D"
#     else:
#         grade = "F"
#     v = 0
#     c = 0
#     for ch in name:
#         if ch in "aeiouAEIOU":
#             v += 1
#         elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
#             c += 1
#     print("Grade:", grade)
#     print("Vowels:", v)
#     print("Characters:", len(name))
#     if v > c:
#         print("More vowels")
#     elif c > v:
#         print("More consonants")
#     else:
#         print("Equal")
#     if m > best:
#         best = m
#         best_name = name
# print("Highest marks:", best_name, best)


#q18
balance=10000
withdrawal=0
deposit=0
for i in range(7):
    trans=input("Select deposit/withdraw :")
    amount=int(input("Enter amount: "))
    if trans=="deposit":
        balance+=amount
        print("Your current balance : ",balance)
        deposit+=1
        if balance<1000:
                    print("low balance")
    elif trans=="withdraw":
        if balance<amount:
            print("Insufficient Balance:")
        else:
            balance-=amount
            print("Your current balance : ",balance)
            withdrawal+=1
            if balance<1000:
                        print("low balance")
print("Your total balance : ",balance)
print("Number of deposits : ",deposit)
print("Number of withdrawal : ",withdrawal)