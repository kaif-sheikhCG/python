# ---------- Basic Level ----------

# 1
def greet():
    print("Hello, Python!")

greet()

# 2
def show_name():
    print("Asha")

show_name()
show_name()
show_name()

# 3
def print_line():
    print("-" * 20)   # same as typing 20 hyphens

print_line()
print("Student Report")
print_line()

# 4
def show_rules():
    print("1. Be on time.")
    print("2. Respect classmates.")
    print("3. Keep the lab clean.")

show_rules()

# 5
def show_square():
    print("****")
    print("****")
    print("****")
    print("****")

show_square()

# 6
def show_menu():
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

show_menu()
show_menu()

# 7
def morning_message():
    print("Good morning!")

def evening_message():
    print("Good evening!")

evening_message()   # reverse order of definitions
morning_message()

# 8
def show_student_card():
    print("STUDENT CARD")
    print("Name: Asha")
    print("Roll number: 12")

show_student_card()

# 9
def print_numbers():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)

print_numbers()
print_numbers()

# 10
def show_pattern():
    print("*")
    print("**")
    print("***")

show_pattern()
show_pattern()


# ---------- Intermediate Level ----------

# 11
def show_header():
    print("MONTHLY REPORT")

def show_body():
    print("Sales increased by 10%.")

def show_footer():
    print("End of report")

show_header()
show_body()
show_footer()

# 12
def show_separator():
    print("====================")

show_separator()
print("Section 1: Overview")
show_separator()
print("Section 2: Details")
show_separator()

# 13
def step_one():
    print("Step one")

def step_two():
    print("Step two")

def step_three():
    print("Step three")

step_three()
step_one()
step_two()

# 14
def show_table_heading():
    print("Roll   Name     Marks")

show_table_heading()
print("12     Asha     85")
print("13     Ravi     78")

# 15
def show_five_stars():
    print("*****")

show_five_stars()
show_five_stars()
show_five_stars()
show_five_stars()

# 16
def show_welcome():
    print("Welcome to the Python Course!")

show_welcome()

# 17
def show_help():
    print("Enter two numbers, then choose an operation.")

show_help()
print("1. Add")
print("2. Subtract")

# 18
def receipt_open():
    print("===== RECEIPT =====")

def receipt_close():
    print("Thank you for shopping!")
    print("===================")

receipt_open()
print("Item: Notebook   Price: 50")
print("Item: Pen        Price: 10")
receipt_close()

# 19
def print_box():
    print("+--------------+")
    print("|  Hello Box   |")
    print("+--------------+")

print_box()
print_box()

# 20
def show_title():
    print("CALCULATOR APP")

def show_menu():
    print("1. Add")
    print("2. Subtract")

def show_closing():
    print("Goodbye!")

show_title()
show_menu()
show_closing()


# ---------- Debugging and Reasoning ----------

# 21 Fixed indentation: the body must be indented.
def greet():
    print("Hello")

# 22 Already correct: prints "Welcome".
def welcome():
    print("Welcome")

welcome()

# 23 Error: show() is called before the definition runs (NameError).
# Fix: move the definition above the call.
def show():
    print("Hello")

show()

# 24 Error: Print_Report is not the same name as print_report (case-sensitive).
# Fix: use the correct name.
def print_report():
    print("Report")

print_report()

# 25 Output:
#   A
#   B
#   A
# Each call runs its own body in the order the calls appear.
def a():
    print("A")

def b():
    print("B")

a()
b()
a()

# 26 The body runs 4 times, once per call. Output: Python printed 4 times.
def message():
    print("Python")

message()
message()
message()
message()

# 27 Lines "One" and "Two" belong to the function.
# "Three" is outside it because it is not indented under def.
def example():
    print("One")
    print("Two")

print("Three")

# 28 Suggested snake_case names:
#   f          -> run_task
#   DoTask     -> do_task
#   studentdetails -> show_student_details
#   x1 (menu)  -> show_menu
def run_task():
    print("Running task")

def do_task():
    print("Doing task")

def show_student_details():
    print("Student details")

def show_menu():
    print("Menu")

# 29 Only one function is called, so only its body runs.
def first_task():
    print("First task")

def second_task():
    print("Second task")

second_task()    # Output: Second task
# first_task() is never called, so "First task" is not printed.

# 30
def display_info():
    print("Information inside the function")

print("Before the call")
display_info()
print("After the call")