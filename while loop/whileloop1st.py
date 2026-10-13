# pallindrome = input("Enter a pallindrome :")
# while pallindrome!=pallindrome[::-1]:
#     print("Enter a valid pallindrome!")
#     pallindrome=input("Enter again: ")
# print(pallindrome,"is a pallindrome")

# s = input("Enter a string: ")

# while True:
#     i = 0
#     j = len(s) - 1
#     count = 0

#     while i < j:
#         if s[i] == s[j]:
#             count += 1
#         i += 1
#         j -= 1

#     if count == len(s) // 2:
#         print("Palindrome")
#         break
#     else:
#         print("Not Palindrome")
#         s = input("Enter again: ")

# let s = prompt("Enter a string:");

# while (true) {
#     let i = 0;
#     let j = s.length - 1;
#     let count = 0;

#     while (i < j) {
#         if (s[i] === s[j]) {
#             count++;
#         }
#         i++;
#         j--;
#     }
#     if (count === Math.floor(s.length / 2)) {
#         console.log("Palindrome");
#         break;
#     } else {
#         console.log("Not Palindrome");
#         s = prompt("Enter again:");
#     }
# }

# n = int(input("Enter number: "))

# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10

# print(reverse)

# n = int(input("Enter number: "))

# while n > 0:
#     digit = n % 10
#     print(digit)
#     n //= 10

n = input("Enter number: ")

if n.startswith("-"):
    n = n[1:]

if n == "":
    print("Invalid input")
else:
    i = len(n) - 1

    while i >= 0:
        print(n[i])
        i -= 1