# Q1
def greet():
    print("Hello, Python!")

greet()


# Q2
def show_name():
    print("Kaif Sheikh")

show_name()
show_name()
show_name()


# Q3
def print_line():
    print("--------------------")

print_line()
print("Python Functions")
print_line()


# Q4
def show_rules():
    print("1. Be punctual.")
    print("2. Respect everyone.")
    print("3. Keep the classroom clean.")

show_rules()


# Q5
def show_square():
#     print("****")
#     print("****")
#     print("****")
#     print("****")
    for i in range(4):
        for j in range(4):
            print("*",end="")
        print()

show_square()


# Q6
def show_menu():
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

show_menu()
show_menu()


# Q7
def morning_message():
    print("Good Morning!")

def evening_message():
    print("Good Evening!")

evening_message()
morning_message()


# Q8
def show_student_card():
    print("Student Card")
    print("Name: Kaif Sheikh")
    print("Roll Number: 101")

show_student_card()


# Q9
def print_numbers():
    # print(1)
    # print(2)
    # print(3)
    # print(4)
    # print(5)
    for i in range(1,6):
        print(i)

print_numbers()
print_numbers()


# Q10
def show_pattern():
    # print("*")
    # print("**")
    # print("***")
    for i in range(1, 4):
        for j in range(i):
           print("*", end="")
        print()
show_pattern()

# Q11
def show_header():
    print("===== STUDENT REPORT =====")

def show_body():
    print("Name: Kaif Sheikh")
    print("Course: BTech CSE AI/ML")
    print("Semester: 1")

def show_footer():
    print("===== END OF REPORT =====")

show_header()
show_body()
show_footer()


# Q12
def show_separator():
    print("====================")

print("Student Details")
show_separator()
print("Name: Kaif Sheikh")
show_separator()
print("Course: BTech CSE AI/ML")
show_separator()


# Q13
def step_one():
    print("Step One")

def step_two():
    print("Step Two")

def step_three():
    print("Step Three")

step_three()
step_one()
step_two()


# Q14
def show_table_heading():
    print("Roll No.   Name       Marks")

show_table_heading()
print("101        Rahul      85")
print("102        Amit       90")


# Q15
def print_stars():
    print("*****")

print_stars()
print_stars()
print_stars()
print_stars()


# Q16
def show_welcome():
    print("Welcome to the program!")
    print("Course: Python Programming")

show_welcome()
print("Let's start learning.")


# Q17
def show_help():
    print("Calculator Instructions:")
    print("1. Select an operation.")
    print("2. Enter two numbers.")
    print("3. View the result.")

show_help()
print("Calculator Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


# Q18
def opening_line():
    print("========================")
    print("         RECEIPT")
    print("========================")

def closing_line():
    print("========================")
    print("       THANK YOU!")
    print("========================")

opening_line()
print("Item: Notebook")
print("Quantity: 2")
print("Price: Rs. 100")
closing_line()


# Q19
def print_box():
    print("+----------+")
    print("| Hello!   |")
    print("+----------+")

print_box()
print_box()


# Q20
def show_title():
    print("===== PYTHON PROGRAM =====")

def show_menu():
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

def show_closing():
    print("Thank you for using the program!")

show_title()
show_menu()
show_closing()

# Q21 - Fix the indentation error
def greet():
    print("Hello")

greet()


# Q22 - Fix the code so it prints Welcome
def welcome():
    print("Welcome")

welcome()


# Q23 - Fix the error
# The function must be defined before it is called.

def show():
    print("Hello")

show()


# Q24 - Fix the function naming problem
# Python is case-sensitive, so Print_Report and print_report are different names.

def print_report():
    print("Report")

print_report()


# Q25 - Predict the output
def a():
    print("A")

def b():
    print("B")

a()
b()
a()

# Output:
# A
# B
# A


# Q26 - How many times does the function body run?
def message():
    print("Python")

message()
message()
message()
message()

# Output:
# Python
# Python
# Python
# Python
# The function body runs 4 times.


# Q27 - Which lines belong to the function body?
def example():
    print("One")
    print("Two")

print("Three")

# Output:
# One
# Two
# Three

# print("One") and print("Two") belong to the function body.
# print("Three") is outside the function because it is not indented.


# Q28 - Rename functions using clear snake_case names

def show_information():
    print("Information")

def do_task():
    print("Task completed")

def show_student_details():
    print("Student details")

def show_menu():
    print("1. Start")
    print("2. Exit")

show_information()
do_task()
show_student_details()
show_menu()


# Q29 - Define two functions but call only one
def first_function():
    print("First function")

def second_function():
    print("Second function")

first_function()

# Output:
# First function
# The second function does not run because it is never called.


# Q30 - Print messages before and after a function call
def show_message():
    print("Inside the function")

print("Before the function call")
show_message()
print("After the function call")

# 1. What is a function?
#    A function is a block of code that performs a specific task.
# 2. Why do we use functions?
#    We use functions to organize code, avoid repetition, and make programs easier to understand.
# 3. What is code reuse?
#    Code reuse means using the same code multiple times instead of writing it again.
# 4. Does defining a function automatically execute its body?
#    No. The function body executes only when the function is called.
# 5. What does def do?
#    The def keyword defines a function in Python.
# 6. What is a function body?
#    The function body is the block of indented code that runs when the function is called.
# 7. Why is indentation important?
#    Indentation tells Python which statements belong to the function body.
# 8. What is the difference between defining and calling a function?
#    - Defining: Creating a function using def.
#    - Calling: Executing the function by using its name followed by parentheses.
# 9. How do you call a function named display_menu?
#    display_menu()
# 10. Why should function names describe their task?
#     Descriptive names make code easier to read, understand, and maintain.
# 11. What naming style is commonly used for Python functions?
#     snake_case, where words are lowercase and separated by underscores. Example: show_student_details().
# 12. What happens if a function is called before its definition has executed in a normal script?
#     Python raises a NameError if the function name has not been defined when the call is executed.
# 13. How many times does a function body run if it is called four times?
#     The function body runs four times.
# 14. Is Print_Total a valid Python function name? Is it the usual style?
#     Yes, Print_Total is a valid function name, but it is not the usual style. Python functions conventionally use snake_case, so print_total is preferred.
# 15. Why might a function make a program easier to maintain?
#     If a task needs to change, we can update the function in one place instead of changing the same code at multiple places. 