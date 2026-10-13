is_indian = input("Are you Indian? Yes or No: ")

if is_indian=="yes":
    age=int(input("Enter your age: "))

    if age>=18:
        has_id=input("Do you have an ID? Yes or No: ")

        if has_id=="yes":
            registered=input("Are you registered to vote? Yes or No: ")

            if registered=="yes":
                location=input("Are you currently in India? Yes or No: ")

                if location == "yes":
                    print("You are eligible to vote")

                if location == "no":
                    print("You are not currently in India")

            if registered == "no":
                print("You need to register first")

        if has_id == "no":
            print("You need an ID to vote")

    if age < 18:
        print("You are not eligible to vote")

if is_indian == "no":
    print("You must be Indian to vote")