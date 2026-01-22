# user_profile.py
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
PURPLE = "\033[95m"
RESET = "\033[0m"

def get_user_profile():
    user = {}

    print(f"\n{PURPLE}--- User Profile Setup ---{RESET}")

    # 1. Age
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                user["age"] = age
                break
            else:
                print(f"{RED}Age must be greater than 0.{RESET}")
        except ValueError:
            print(f"{RED}Please enter a valid number.{RESET}")

    # 2. Purpose
    print(f"\n{PURPLE}Select your main purpose:{RESET}")
    print("1. Learning")
    print("2. Entertainment")
    print("3. Mixed")
    print("4. Shopping")

    while True:
        purpose_choice = input(f"{BLUE}Enter your choice (1-4): {RESET}")
        if purpose_choice == "1":
            user["purpose"] = "Learning"
            break
        elif purpose_choice == "2":
            user["purpose"] = "Entertainment"
            break
        elif purpose_choice == "3":
            user["purpose"] = "Mixed"
            break
        elif purpose_choice == "4":
            user["purpose"] = "Shopping"
            break
        else:
            print(f"{RED}Invalid choice. Please select 1-4.{RESET}")

    # Initialize interests
    user["learning_interest"] = []
    user["entertainment_interest"] = []
    user["shopping_interest"] = []
    user["budget"] = None

    # 3. Learning interests
    if user["purpose"] in ["Learning", "Mixed"]:
        print(f"\n{PURPLE}Select learning interests (comma-separated):{RESET}")
        print("1. Music")
        print("2. Cooking")
        print("3. Fitness")
        print("4. Art")
        print("5. Science")

        while True:
            choices = input(f"{BLUE}Enter choices (e.g. 1,3): {RESET}")
            selected = choices.split(",")

            valid = True
            for c in selected:
                if c.strip() not in ["1", "2", "3","4","5"]:
                    valid = False

            if valid:
                mapping = {
                    "1": "Music",
                    "2": "Cooking",
                    "3": "Fitness",
                    "4": "Art",
                    "5": "Science"
                }
                user["learning_interest"] = [mapping[c.strip()] for c in selected]
                break
            else:
                print(f"{RED}Invalid input. Please select from 1, 2, 3.{RESET}")

    # 4. Entertainment interests
    if user["purpose"] in ["Entertainment", "Mixed"]:
        print(f"\n{PURPLE}Select entertainment interests (comma-separated):{RESET}")
        print("1. Anime")
        print("2. Travel")
        print("3. Variety Shows")
        print("4. Documentaries")

        while True:
            choices = input(f"{BLUE}Enter choices (e.g. 1,2): {RESET}")
            selected = choices.split(",")

            valid = True
            for c in selected:
                if c.strip() not in ["1", "2", "3", "4"]:
                    valid = False

            if valid:
                mapping = {
                    "1": "Anime",
                    "2": "Travel",
                    "3": "Variety Shows",
                    "4": "Documentaries"
                }
                user["entertainment_interest"] = [mapping[c.strip()] for c in selected]
                break
            else:
                print(f"{RED}Invalid input. Please select from 1, 2, 3.{RESET}")

    # 5. Shopping interests & budget
    if user["purpose"] in ["Shopping", "Mixed"]:
        print(f"\n{PURPLE}Select shopping interests (comma-separated):{RESET}")
        print("1. Electronics")
        print("2. Fashion")
        print("3. Sports")

        while True:
            choices = input(f"{BLUE}Enter choices (e.g. 1,3): {RESET}")
            selected = choices.split(",")

            valid = True
            for c in selected:
                if c.strip() not in ["1", "2", "3"]:
                    valid = False

            if valid:
                mapping = {
                    "1": "Electronics",
                    "2": "Fashion",
                    "3": "Sports"
                }
                user["shopping_interest"] = [mapping[c.strip()] for c in selected]
                break
            else:
                print(f"{RED}Invalid input. Please select from 1, 2, 3.{RESET}")

        # Budget
        while True:
            try:
                budget = float(input(f"{BLUE}Enter your shopping budget: {RESET}"))
                if budget >= 0:
                    user["budget"] = budget
                    break
                else:
                    print(f"{RED}Budget must be 0 or more.{RESET}")
            except ValueError:
                print(f"{RED}Please enter a valid number.{RESET}")

    print(f"\n{GREEN}User profile completed!{RESET}")
    return user