n = 5

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)

n = 5  # Total number of rows

for i in range(n, 0, -1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    
    # Print stars without extra space in between
    for k in range(i):
        print("*", end="")
    
    # Move to the next line
    print()

n = 5  # Total number of rows

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    
    for k in range(2 * i - 1):
        print("*", end="")
    
    print()