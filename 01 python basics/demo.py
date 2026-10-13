# s = input("Enter a string: ")

# result = ""

# for ch in s:
#     if not ('0' <= ch <= '9'):
#         result += ch

# print(result)

s = input("Enter a string: ")
lower=0
for ch in s:
    if ch.islower():
        lower+=1
print("Lower = ",lower)