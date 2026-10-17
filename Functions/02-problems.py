# 1
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()

# 2
def greet(name):
    print("Hello,", name)

greet("Asha")

# 3
def show_number(number):
    print(number)

show_number(42)

# 4
def add(a, b):
    return a + b

print(add(3, 4))

# 5
def square(number):
    return number * number

print(square(6))

# 6
def is_even(number):
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False

# 7
def get_full_name(first_name, last_name):
    return first_name + " " + last_name

print(get_full_name("Asha", "Patel"))

# 8
def introduce(name, city="Pune"):
    print(name, "is from", city)

introduce("Asha")
introduce("Rahul", "Mumbai")

# 9
def subtract(a, b):
    return a - b

print(subtract(10, 3))   # 7
print(subtract(3, 10))   # -7

# 10
def get_min_max(a, b):
    if a < b:
        return a, b
    return b, a

smallest, largest = get_min_max(9, 4)
print(smallest, largest)   # 4 9


# ---------- Intermediate ----------

# 11
def calculate(a, b):
    return a + b, a - b, a * b, a / b

total, difference, product, quotient = calculate(12, 4)
print(total, difference, product, quotient)   # 16 8 48 3.0

# 12
def count_digits(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        number = number // 10
        count += 1
    return count

print(count_digits(0))     # 1
print(count_digits(4096))  # 4

# 13
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"

print(classify_number(-5))   # Negative

# 14
def calculate_total(price, quantity=1):
    return price * quantity

print(calculate_total(50))      # 50
print(calculate_total(50, 3))   # 150

# 15
def create_email(username, domain="example.com"):
    return username + "@" + domain

print(create_email("asha"))               # asha@example.com
print(create_email("rahul", "mail.com"))  # rahul@mail.com

# 16
def format_name(first, last, uppercase=False):
    full_name = first + " " + last
    if uppercase:
        return full_name.upper()
    return full_name

print(format_name("Asha", "Patel"))                  # Asha Patel
print(format_name("Asha", "Patel", uppercase=True))  # ASHA PATEL

# 17
def percentage(marks, total=100):
    return marks / total * 100

print(percentage(45))        # 45.0
print(percentage(45, 50))    # 90.0

# 18
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute

print(convert_minutes(5))    # 300

# 19
def student_details(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student_details(city="Pune", name="Asha", age=21)

# 20
def bill(item, quantity=1, price=100):
    return quantity * price

print(bill("Notebook"))                 # 100
print(bill("Notebook", 3))              # 300
print(bill("Notebook", price=50))       # 50
print(bill(item="Pen", quantity=2, price=10))  # 20


# ---------- Challenging ----------

# 21
def analyze_number(number):
    if number < 0:
        absolute_value = -number
    else:
        absolute_value = number

    is_even_number = absolute_value % 2 == 0

    digit_count = 0
    temp = absolute_value
    if temp == 0:
        digit_count = 1
    while temp > 0:
        temp = temp // 10
        digit_count += 1

    return absolute_value, is_even_number, digit_count

print(analyze_number(-246))   # (246, True, 3)

# 22
def calculate_stats(a, b, c):
    smallest = a
    largest = a
    for value in (b, c):
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
    return smallest, largest, a + b + c

print(calculate_stats(4, 9, 1))   # (1, 9, 14)

# 23
def make_sentence(subject, verb, object):
    return subject + " " + verb + " " + object

print(make_sentence(object="a book", verb="reads", subject="Asha"))
# Asha reads a book

# 24
def apply_discount(price, discount=0):
    return price - price * discount / 100

print(apply_discount(500))              # 500.0
print(apply_discount(500, discount=10)) # 450.0

# 25
def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus

print(calculate_pay(8))                  # 1600
print(calculate_pay(8, bonus=300))       # 1900
print(calculate_pay(8, 250, 100))        # 2100

# 26
def get_coordinates(x=0, y=0):
    return x, y

print(get_coordinates())       # (0, 0)
print(get_coordinates(y=5))    # (0, 5)
print(get_coordinates(3))      # (3, 0)

# 27
def compare(a, b):
    if a > b:
        message = "A is greater"
        difference = a - b
    elif b > a:
        message = "B is greater"
        difference = b - a
    else:
        message = "Equal"
        difference = 0
    return message, difference

print(compare(7, 12))   # ('B is greater', 5)

# 28
def convert_temperature(value, scale="C"):
    if scale == "C":
        return value * 9 / 5 + 32   # Celsius to Fahrenheit
    return (value - 32) * 5 / 9     # Fahrenheit to Celsius

print(convert_temperature(100))             # 212.0
print(convert_temperature(212, scale="F"))  # 100.0

# 29
def calculate_result(marks, passing_marks=35):
    if marks >= passing_marks:
        return "Pass"
    return "Fail"

print(calculate_result(40))   # Pass
print(calculate_result(20))   # Fail

# 30
def order_summary(item, quantity=1, price=100, delivery_fee=40):
    return quantity * price + delivery_fee

print(order_summary("Notebook"))                     # 140
print(order_summary("Notebook", 2, delivery_fee=0))  # 200