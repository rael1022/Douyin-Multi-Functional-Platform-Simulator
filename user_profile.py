# user_profile.py

def get_user_profile():
    user = {}

    print("\n--- User Profile Setup ---")

    # 1. Age
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                user["age"] = age
                break
            else:
                print("Age must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    # 2. Purpose
    print("\nSelect your main purpose:")
    print("1. Learning")
    print("2. Entertainment")
    print("3. Mixed")
    print("4. Shopping")

    while True:
        purpose_choice = input("Enter your choice (1-4): ")
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
            print("Invalid choice. Please select 1-4.")

    # Initialize interests
    user["learning_interest"] = []
    user["entertainment_interest"] = []
    user["shopping_interest"] = []
    user["budget"] = None

    # 3. Learning interests
    if user["purpose"] in ["Learning", "Mixed"]:
        print("\nSelect learning interests (comma-separated):")
        print("1. Music")
        print("2. Cooking")
        print("3. Fitness")

        while True:
            choices = input("Enter choices (e.g. 1,3): ")
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
                print("Invalid input. Please select from 1, 2, 3.")

    # 4. Entertainment interests
    if user["purpose"] in ["Entertainment", "Mixed"]:
        print("\nSelect entertainment interests (comma-separated):")
        print("1. Anime")
        print("2. Travel")
        print("3. Variety Shows")

        while True:
            choices = input("Enter choices (e.g. 1,2): ")
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
                print("Invalid input. Please select from 1, 2, 3.")

    # 5. Shopping interests & budget
    if user["purpose"] in ["Shopping", "Mixed"]:
        print("\nSelect shopping interests (comma-separated):")
        print("1. Electronics")
        print("2. Fashion")
        print("3. Sports")

        while True:
            choices = input("Enter choices (e.g. 1,3): ")
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
                print("Invalid input. Please select from 1, 2, 3.")

        # Budget
        while True:
            try:
                budget = float(input("Enter your shopping budget: "))
                if budget >= 0:
                    user["budget"] = budget
                    break
                else:
                    print("Budget must be 0 or more.")
            except ValueError:
                print("Please enter a valid number.")

    print("\nUser profile completed!")
    return user
