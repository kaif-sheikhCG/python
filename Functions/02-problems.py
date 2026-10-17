# ===== Beginner =====

# Q1. welcome
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()

# Q2. greet
def greet(name):
    print(f"Hello {name}")

greet("Asha")

# Q3. show_number
def show_number(number):
    print(number)

show_number(42)

# Q4. add
def add(a, b):
    return a + b

print(add(3, 4))

# Q5. square
def square(number):
    return number * number

print(square(5))

# Q6. is_even
def is_even(number):
    return number % 2 == 0

print(is_even(10))

# Q7. get_full_name
def get_full_name(first_name, last_name):
    return first_name + " " + last_name

print(get_full_name("Ravi", "Patel"))

# Q8. introduce
def introduce(name, city="Pune"):
    print(f"My name is {name} and I live in {city}")

introduce("Meera")
introduce("Meera", "Surat")

# Q9. subtract
def subtract(a, b):
    return a - b

print(subtract(10, 3))   # 7
print(subtract(3, 10))   # -7 (order matters)

# Q10. get_min_max
def get_min_max(a, b):
    if a < b:
        return a, b
    return b, a

print(get_min_max(9, 2))

# ===== Intermediate =====

# Q11. calculate
def calculate(a, b):
    return a + b, a - b, a * b, a / b

print(calculate(10, 2))

# Q12. count_digits
def count_digits(number):
    return len(str(number))   # 0 gives "0", so 1 digit

print(count_digits(0), count_digits(12345))

# Q13. classify_number
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"

print(classify_number(-5), classify_number(0))

# Q14. calculate_total
def calculate_total(price, quantity=1):
    return price * quantity

print(calculate_total(50), calculate_total(50, 3))

# Q15. create_email
def create_email(username, domain="example.com"):
    return f"{username}@{domain}"

print(create_email("asha"), create_email("asha", "mail.com"))

# Q16. format_name
def format_name(first, last, uppercase=False):
    full = first + " " + last
    if uppercase:
        return full.upper()
    return full

print(format_name("Ravi", "Patel"), format_name("Ravi", "Patel", uppercase=True))

# Q17. percentage
def percentage(marks, total=100):
    return marks / total * 100

print(percentage(45))

# Q18. convert_minutes
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute

print(convert_minutes(3))

# Q19. student_details
def student_details(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

student_details(city="Pune", name="Asha", age=20)

# Q20. bill
def bill(item, quantity=1, price=100):
    print(f"Item: {item}")
    return quantity * price

print(bill("Pen"), bill("Pen", 2), bill("Pen", price=50, quantity=4))

# ===== Challenging =====

# Q21. analyze_number
def analyze_number(number):
    if number >= 0:
        absolute = number
    else:
        absolute = -number
    is_even_flag = number % 2 == 0
    digits = len(str(absolute))
    return absolute, is_even_flag, digits

print(analyze_number(-7))

# Q22. calculate_stats
def calculate_stats(a, b, c):
    smallest = min(a, b, c)
    largest = max(a, b, c)
    total = a + b + c
    return smallest, largest, total

print(calculate_stats(4, 9, 2))

# Q23. make_sentence
def make_sentence(subject, verb, object):
    return f"{subject} {verb} {object}"

print(make_sentence(verb="reads", object="a book", subject="Asha"))

# Q24. apply_discount
def apply_discount(price, discount=0):
    return price - price * discount / 100

print(apply_discount(200, 10))

# Q25. calculate_pay
def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus

print(calculate_pay(10), calculate_pay(10, 150), calculate_pay(hours=10, bonus=500))

# Q26. get_coordinates
def get_coordinates(x=0, y=0):
    return x, y

print(get_coordinates(), get_coordinates(y=5))

# Q27. compare
def compare(a, b):
    if a > b:
        result = "A is greater"
        difference = a - b
    elif b > a:
        result = "B is greater"
        difference = b - a
    else:
        result = "Equal"
        difference = 0
    return result, difference

print(compare(3, 8))

# Q28. convert_temperature
def convert_temperature(value, scale="C"):
    if scale == "C":
        return value * 9 / 5 + 32
    return (value - 32) * 5 / 9

print(convert_temperature(100), convert_temperature(212, "F"))

# Q29. calculate_result
def calculate_result(marks, passing_marks=35):
    if marks >= passing_marks:
        return "Pass"
    return "Fail"

print(calculate_result(30), calculate_result(40))

# Q30. order_summary
def order_summary(item, quantity=1, price=100, delivery_fee=40):
    return quantity * price + delivery_fee

print(order_summary("Book", delivery_fee=0))