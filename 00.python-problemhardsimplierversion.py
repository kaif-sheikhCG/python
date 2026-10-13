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
if upper == big:
    same += 1
if lower == big:
    same += 1
if digit == big:
    same += 1
if space == big:
    same += 1
if special == big:
    same += 1
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Spaces:", space)
print("Special:", special)
if same > 1:
    print("Tie")
elif upper == big:
    print("Highest: Uppercase")
elif lower == big:
    print("Highest: Lowercase")
elif digit == big:
    print("Highest: Digits")
elif space == big:
    print("Highest: Spaces")
else:
    print("Highest: Special")

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

# Q3
text = input("Enter sentence: ")
word = ""
best = -1
best_word = ""
for i in range(len(text) + 1):
    if i < len(text) and text[i] != " ":
        word += text[i]
    else:
        if word != "":
            score = 0
            for ch in word:
                if ch in "aeiouAEIOU":
                    score += 2
                elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
                    score += 1
                elif ch >= "0" and ch <= "9":
                    score += 3
                else:
                    score += 4
            print(word, score)
            if score > best:
                best = score
                best_word = word
        word = ""
print("Highest score word:", best_word)

# Q4
for i in range(5):
    p = input("Enter password: ")
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
    count = up + low + num + sp
    if len(p) >= 8:
        count += 1
    if count == 5:
        print("Strong")
    elif count >= 3:
        print("Medium")
    else:
        print("Weak")

# Q5
text = input("Enter sentence: ")
word = ""
short = 0
medium = 0
long = 0
for i in range(len(text) + 1):
    if i < len(text) and text[i] != " ":
        word += text[i]
    else:
        if word != "":
            n = len(word)
            print(word, n)
            if n <= 3:
                print("Short")
                short += 1
            elif n <= 6:
                print("Medium")
                medium += 1
            else:
                print("Long")
                long += 1
        word = ""
print("Short:", short)
print("Medium:", medium)
print("Long:", long)

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

# Q7
s = input("Enter string: ")
for i in range(len(s)):
    seen = False
    for j in range(i):
        if s[j] == s[i]:
            seen = True
    if seen == False:
        c = 0
        for ch in s:
            if ch == s[i]:
                c += 1
        if c == 2:
            print(s[i], c, "Duplicate")
        elif c == 3 or c == 4:
            print(s[i], c, "Repeated")
        elif c > 4:
            print(s[i], c, "Highly Repeated")

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

# Q9
s = input("Enter string: ")
vowel = 0
cons = 0
digit = 0
special = 0
for i in range(len(s)):
    ch = s[i]
    if i % 2 == 0:
        pos = "even"
    else:
        pos = "odd"
    if ch in "aeiouAEIOU":
        kind = "vowel"
        vowel += 1
    elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
        kind = "consonant"
        cons += 1
    elif ch >= "0" and ch <= "9":
        kind = "digit"
        digit += 1
    else:
        kind = "special"
        special += 1
    print(ch, i, pos, kind)
print("Vowels:", vowel)
print("Consonants:", cons)
print("Digits:", digit)
print("Special:", special)

# Q10
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 15 == 0:
            print("Z", end=" ")
        elif j % 3 == 0:
            print("X", end=" ")
        elif j % 5 == 0:
            print("Y", end=" ")
        else:
            print(j, end=" ")
    print()

# Q11
for i in range(5):
    u = input("Enter username: ")
    digits = 0
    under = 0
    bad = 0
    for ch in u:
        if ch >= "0" and ch <= "9":
            digits += 1
        elif ch == "_":
            under += 1
        elif not ((ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z")):
            bad += 1
    first_ch = u[0]
    if bad > 0 or len(u) < 4 or (first_ch >= "0" and first_ch <= "9"):
        print("Invalid")
    elif len(u) > 15 or digits > 3 or under > 2:
        print("Needs Improvement")
    else:
        print("Valid")

# Q12
s = input("Enter sentence: ")
v = 0
c = 0
for ch in s:
    if ch in "aeiouAEIOU":
        v += 1
    elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
        c += 1
if v > c:
    print("Vowels Win")
elif c > v:
    print("Consonants Win")
else:
    print("Draw")
for x in "aeiou":
    n = 0
    for ch in s:
        if ch == x or ch == chr(ord(x) - 32):
            n += 1
    print(x, n)

# Q13
total = 0
for i in range(6):
    u = int(input("Enter units: "))
    if u <= 100:
        bill = u * 5
    elif u <= 200:
        bill = 500 + (u - 100) * 7
    elif u <= 400:
        bill = 1200 + (u - 200) * 10
    else:
        bill = 3200 + (u - 400) * 15
    if bill < 1000:
        print(bill, "Low")
    elif bill <= 3000:
        print(bill, "Medium")
    else:
        print(bill, "High")
    total += bill
print("Total revenue:", total)

# Q14
text = input("Enter sentence: ")
word = ""
for i in range(len(text) + 1):
    if i < len(text) and text[i] != " ":
        word += text[i]
    else:
        if word != "":
            v = 0
            c = 0
            for ch in word:
                if ch in "aeiouAEIOU":
                    v += 1
                elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
                    c += 1
            if v > c:
                print(word, "Vowel Heavy")
            elif c > v:
                print(word, "Consonant Heavy")
            else:
                print(word, "Balanced")
        word = ""

# Q15
even = 0
odd = 0
pos = 0
neg = 0
zero = 0
big = 0
for i in range(3):
    for j in range(3):
        x = int(input("Enter number: "))
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1
        if i == 0 and j == 0:
            big = x
        elif x > big:
            big = x
print("Even:", even)
print("Odd:", odd)
print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)
print("Largest:", big)

# Q16
p = input("Enter password: ")
up = 0
low = 0
num = 0
sp = 0
for ch in p:
    if ch >= "A" and ch <= "Z":
        up += 1
    elif ch >= "a" and ch <= "z":
        low += 1
    elif ch >= "0" and ch <= "9":
        num += 1
    else:
        sp += 1
n = len(p)
if n > 0:
    print("Uppercase %:", up * 100 / n)
    print("Lowercase %:", low * 100 / n)
    print("Digits %:", num * 100 / n)
    print("Special %:", sp * 100 / n)
big = up
if low > big:
    big = low
if num > big:
    big = num
if sp > big:
    big = sp
if up == big:
    print("Dominant: Uppercase")
elif low == big:
    print("Dominant: Lowercase")
elif num == big:
    print("Dominant: Digits")
else:
    print("Dominant: Special")

# Q17
best = -1
best_name = ""
for i in range(5):
    name = input("Enter name: ")
    m = int(input("Enter marks: "))
    if m >= 90:
        grade = "A+"
    elif m >= 75:
        grade = "A"
    elif m >= 60:
        grade = "B"
    elif m >= 50:
        grade = "C"
    elif m >= 35:
        grade = "D"
    else:
        grade = "F"
    v = 0
    c = 0
    for ch in name:
        if ch in "aeiouAEIOU":
            v += 1
        elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
            c += 1
    print("Grade:", grade)
    print("Vowels:", v)
    print("Characters:", len(name))
    if v > c:
        print("More vowels")
    elif c > v:
        print("More consonants")
    else:
        print("Equal")
    if m > best:
        best = m
        best_name = name
print("Highest marks:", best_name, best)

# Q18
balance = float(input("Enter starting balance: "))
deposits = 0
withdrawals = 0
rejected = 0
for i in range(7):
    t = input("Deposit or Withdrawal: ")
    amount = float(input("Enter amount: "))
    if t == "Deposit" or t == "deposit":
        balance += amount
        deposits += 1
    elif t == "Withdrawal" or t == "withdrawal":
        if amount > balance:
            print("Not enough balance")
            rejected += 1
        else:
            balance -= amount
            withdrawals += 1
    else:
        print("Wrong input")
    if balance < 1000:
        print("Low Balance")
    print("Balance:", balance)
print("Final balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Rejected:", rejected)

# Q19
s = input("Enter sentence: ")
flags = 0
has_digit = False
for ch in s:
    if ch >= "0" and ch <= "9":
        has_digit = True
if has_digit:
    flags += 1
if "." in s:
    flags += 1
if "@" in s:
    flags += 1
if "password" in s or "Password" in s or "pwd" in s:
    flags += 1
repeat = False
for i in range(len(s) - 1):
    a = s[i]
    is_letter_digit = (a >= "a" and a <= "z") or (a >= "A" and a <= "Z") or (a >= "0" and a <= "9")
    if not is_letter_digit and a != " " and s[i] == s[i + 1]:
        repeat = True
if repeat:
    flags += 1
if flags == 0:
    print("Safe")
elif flags <= 2:
    print("Review")
else:
    print("Suspicious")

# Q20
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        r = i * j
        if r % 2 == 0:
            print("E", end="")
        else:
            print("O", end="")
        if r % 5 == 0:
            print("F", end="")
        print(end="\t")
    print()

# Q21
total = 0
d20 = 0
d15 = 0
d10 = 0
d0 = 0
for i in range(10):
    p = float(input("Enter price: "))
    if p >= 5000:
        d = p * 20 / 100
        d20 += 1
    elif p >= 3000:
        d = p * 15 / 100
        d15 += 1
    elif p >= 1000:
        d = p * 10 / 100
        d10 += 1
    else:
        d = 0
        d0 += 1
    print("Final price:", p - d)
    total += d
print("20% discount:", d20)
print("15% discount:", d15)
print("10% discount:", d10)
print("No discount:", d0)
print("Total discount:", total)

# Q22
s = input("Enter string: ")
result = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result = result + s[i - 1] + str(count)
        count = 1
if len(s) > 0:
    result = result + s[len(s) - 1] + str(count)
print(result)

# Q23
junior = 0
mid = 0
senior = 0
executive = 0
total = 0
for i in range(8):
    sal = float(input("Enter salary: "))
    total += sal
    if sal < 25000:
        junior += 1
    elif sal <= 50000:
        mid += 1
    elif sal <= 100000:
        senior += 1
    else:
        executive += 1
print("Junior:", junior)
print("Mid:", mid)
print("Senior:", senior)
print("Executive:", executive)
print("Average salary:", total / 8)

# Q24
s = input("Enter sentence: ")
w = input("Enter secret word: ")
first = -1
count = 0
for i in range(len(s) - len(w) + 1):
    match = True
    for k in range(len(w)):
        if s[i + k] != w[k]:
            match = False
    if match:
        count += 1
        if first == -1:
            first = i
if count == 0:
    print("Secret word not found")
else:
    print("Starting position:", first)
    print("Times:", count)

# Q25
n = int(input("Enter n: "))
num = 1
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        if num % 15 == 0:
            print("F", end=" ")
        elif num % 3 == 0:
            print("T", end=" ")
        elif num % 2 == 0:
            print("E", end=" ")
        else:
            print("O", end=" ")
        num += 1
    print()