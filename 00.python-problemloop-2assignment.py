# Q1
s = input("Enter string: ")
upper = 0
lower = 0
digit = 0
space = 0
special = 0
for ch in s:
    if ch >= "A" and ch <= "Z":
        upper += 1
    elif ch >= "a" and ch <= "z":
        lower += 1
    elif ch >= "0" and ch <= "9":
        digit += 1
    elif ch == " ":
        space += 1
    else:
        special += 1
big = upper
if lower > big:
    big = lower
if digit > big:
    big = digit
if space > big:
    big = space
if special > big:
    big = special
same = 0
name = ""
if upper == big:
    same += 1
    name = "Uppercase"
if lower == big:
    same += 1
    name = "Lowercase"
if digit == big:
    same += 1
    name = "Digits"
if space == big:
    same += 1
    name = "Spaces"
if special == big:
    same += 1
    name = "Special"
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Spaces:", space)
print("Special:", special)
if same > 1:
    print("Tie")
else:
    print("Highest:", name)

# Q2
fail = 0
ok = 0
good = 0
great = 0
for i in range(10):
    m = int(input("Enter marks: "))
    if m < 35:
        print("Fail")
        fail += 1
    elif m < 50:
        print("Pass")
        ok += 1
    elif m < 75:
        print("Good")
        good += 1
    else:
        print("Excellent")
        great += 1
print("Fail:", fail)
print("Pass:", ok)
print("Good:", good)
print("Excellent:", great)

# Q4
for i in range(1,6):
    p = input("Enter password: ")
    count = 0
    up = 0
    low = 0
    num = 0
    sp = 0
    for ch in p:
        if ch >= "A" and ch <= "Z":
            up = 1
        elif ch >= "a" and ch <= "z":
            low = 1
        elif ch >= "0" and ch <= "9":
            num = 1
        else:
            sp = 1
    if len(p) >= 8:
        count += 1
    count = count + up + low + num + sp
    if count == 5:
        print("Strong")
    elif count >= 3:
        print("Medium")
    else:
        print("Weak")


# Q6
for i in range(5):
    n = int(input("Enter number: "))
    t = str(n)
    even = 0
    odd = 0
    for ch in t:
        if ch >= "0" and ch <= "9":
            d = int(ch)
            if d % 2 == 0:
                even += 1
            else:
                odd += 1
    if even > odd:
        print("Even digits more")
    elif odd > even:
        print("Odd digits more")
    else:
        print("Equal")

# Q8
total = 0
budget = 0
regular = 0
premium = 0
luxury = 0
for i in range(8):
    p = float(input("Enter price: "))
    total += p
    if p < 500:
        budget += 1
    elif p < 2000:
        regular += 1
    elif p < 5000:
        premium += 1
    else:
        luxury += 1
print("Total:", total)
print("Budget:", budget)
print("Regular:", regular)
print("Premium:", premium)
print("Luxury:", luxury)
print("Average:", total / 8)
