device = input("Choose your device (PC / Laptop / Console): ")

if device == "PC":

    budget = input("Choose your budget (Low / Medium / High): ")

    if budget == "Low":

        game = input("Choose a game (Minecraft / Roblox / Valorant): ")

        if game == "Minecraft":
            storage = input("Do you have 10GB free storage? Yes / No: ")

            if storage == "Yes":
                print("Minecraft can be installed.")

                internet = input("Do you have internet? Yes / No: ")

                if internet == "Yes":
                    print("You can play Minecraft online.")

                    multiplayer = input("Do you want multiplayer? Yes / No: ")

                    if multiplayer == "Yes":
                        print("Join a Minecraft multiplayer server.")

            if storage == "No":
                print("Free some storage before installing Minecraft.")

        if game == "Roblox":
            print("Roblox is a good choice for a low-budget PC.")

        if game == "Valorant":
            ram = int(input("Enter your RAM in GB: "))

            if ram >= 8:
                print("Your PC can run Valorant.")

            if ram < 8:
                print("You may need more RAM.")

    if budget == "Medium":

        graphics = input("Choose graphics card (Basic / Good / Powerful): ")

        if graphics == "Basic":
            print("Try games with medium graphics.")

        if graphics == "Good":
            game = input("Choose game (GTA / FIFA / Minecraft): ")

            if game == "GTA":
                print("GTA is selected.")

            if game == "FIFA":
                print("FIFA is selected.")

            if game == "Minecraft":
                print("Minecraft is selected.")

        if graphics == "Powerful":
            print("You can play high-end games.")

            raytracing = input("Do you want Ray Tracing? Yes / No: ")

            if raytracing == "Yes":
                print("Enable Ray Tracing in supported games.")

            if raytracing == "No":
                print("Use normal graphics settings.")

    if budget == "High":

        monitor = input("Choose monitor (1080p / 1440p / 4K): ")

        if monitor == "1080p":
            print("Great for high FPS gaming.")

        if monitor == "1440p":
            print("Great balance between quality and performance.")

        if monitor == "4K":
            print("Excellent visual quality.")

            refresh_rate = int(input("Enter monitor refresh rate: "))

            if refresh_rate >= 120:
                print("Excellent for gaming.")

                gpu = input("Do you have a powerful GPU? Yes / No: ")

                if gpu == "Yes":
                    print("Your setup is ready for 4K gaming.")

                if gpu == "No":
                    print("Consider upgrading your GPU.")


if device == "Laptop":

    type = input("Choose laptop type (Student / Gaming / Professional): ")

    if type == "Student":
        battery = input("Is long battery life important? Yes / No: ")

        if battery == "Yes":
            print("Choose a laptop with a large battery.")

        if battery == "No":
            print("You can focus more on performance.")

    if type == "Gaming":
        cooling = input("Choose cooling (Normal / Advanced): ")

        if cooling == "Normal":
            print("Use a cooling pad for long gaming sessions.")

        if cooling == "Advanced":
            print("Your laptop should handle longer gaming sessions.")

            gpu = input("Choose GPU (RTX / GTX / Integrated): ")

            if gpu == "RTX":
                print("Good choice for modern games.")

            if gpu == "GTX":
                print("Good for many older and lighter games.")

            if gpu == "Integrated":
                print("Best for lightweight games.")

    if type == "Professional":
        storage = input("Choose storage (256GB / 512GB / 1TB): ")

        if storage == "256GB":
            print("Suitable for basic work.")

        if storage == "512GB":
            print("Good amount of storage.")

        if storage == "1TB":
            print("Excellent storage for large projects.")


if device == "Console":

    console = input("Choose console (PlayStation / Xbox / Nintendo): ")

    if console == "PlayStation":

        game = input("Choose game type (Action / Racing / Sports): ")

        if game == "Action":
            print("Try an action game.")

        if game == "Racing":
            print("Try a racing game.")

        if game == "Sports":
            print("Try a sports game.")

    if console == "Xbox":

        subscription = input("Do you have Game Pass? Yes / No: ")

        if subscription == "Yes":
            print("You have access to many games.")

            online = input("Do you want to play online? Yes / No: ")

            if online == "Yes":
                print("Start an online multiplayer game.")

            if online == "No":
                print("Choose a single-player game.")

        if subscription == "No":
            print("You can purchase individual games.")

    if console == "Nintendo":

        mode = input("Choose mode (Handheld / TV): ")

        if mode == "Handheld":
            print("Play Nintendo games on the go.")

        if mode == "TV":
            print("Connect the console to your TV.")

            players = int(input("How many players? "))

            if players == 1:
                print("Single-player mode selected.")

            if players == 2:
                print("Two-player mode selected.")

            if players > 2:
                print("Multiplayer mode selected.")