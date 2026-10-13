a=int(input("Enter time in seconds: "))
hours=a//3600
minutes=(a%3600)//60
seconds=(a%3600)%60
print(f"The time is {hours} hours, {minutes} minutes, and {seconds} seconds.")