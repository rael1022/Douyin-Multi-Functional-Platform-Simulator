# main.py
from user_profile import get_user_profile
from learning_module import learning_recommendation


def show_menu():
    print("\n=== Main Menu ===")
    print("1. Learning Content")
    print("2. Entertainment Content")
    print("3. Shopping")
    print("4. View Risk Analysis")
    print("5. Generate Full Report")
    print("0. Exit")


def main():
    print("=== Welcome to SmartApp ===")

    # Step 1: Get user profile
    user = get_user_profile()

    # Containers to store results
    content = {}
    usage = None
    shopping_result = None

    # Step 2: Menu loop
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Learning Module ---")
            content["learning"] = learning_recommendation(user)
            usage = track_usage(user)
            print("Learning content displayed.")

        elif choice == "2":
            print("\n--- Entertainment Module ---")
            content["entertainment"] = entertainment_recommendation(user)
            usage = track_usage(user)
            print("Entertainment content displayed.")

        elif choice == "3":
            print("\n--- Shopping Module ---")
            shopping_result = shopping_recommendation(user)
            content["shopping"] = shopping_result
            usage = track_usage(user)

        elif choice == "4":
            print("\n--- Risk Analysis ---")
            if usage is None:
                print("Please use the app first before viewing risk analysis.")
            else:
                risk = analyze_risk(user, usage, shopping_result)
                print(risk)

        elif choice == "5":
            print("\n--- Final Report ---")
            if usage is None:
                print("Please use the app first before generating a report.")
            else:
                risk = analyze_risk(user, usage, shopping_result)
                generate_report(user, usage, content, risk)

        elif choice == "0":
            print("Thank you for using SmartApp. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
