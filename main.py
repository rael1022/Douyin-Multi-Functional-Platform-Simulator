from user_profile import get_user_profile
from learning_module import learning_recommendation
from entertainment_module import entertainment_recommendation
from shopping_module import shopping_recommendation
from usage_analysis import init_usage, track_usage
from risk_analysis import analyze_risk
from report_generator import generate_report

BLUE = "\033[94m"
PINK = "\033[38;5;205m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
PURPLE = "\033[38;5;141m"
CYAN = "\033[96m"
INDIGO = "\033[38;5;57m"
RESET = "\033[0m"

MENU_ORDER = [
    ("Learning Content", "learning"),
    ("Entertainment Content", "entertainment"),
    ("Shopping", "shopping"),
    ("View Usage Analysis", "usage"),
    ("View Risk Analysis", "risk"),
    ("Generate Full Report", "report"),
    ("Exit", "exit")
]


def build_menu(user):
    menu = []

    for label, action in MENU_ORDER:
        if action in ["usage", "risk", "report", "exit"]:
            menu.append((label, action))
        elif action == "learning" and user["purpose"] in ["Learning", "Mixed"]:
            menu.append((label, action))
        elif action == "entertainment" and user["purpose"] in ["Entertainment", "Mixed"]:
            menu.append((label, action))
        elif action == "shopping" and user["purpose"] in ["Shopping", "Mixed"]:
            menu.append((label, action))

    return menu


def show_menu(menu):
    print(f"{PINK}\n=== Main Menu ==={RESET}")
    for idx, (label, _) in enumerate(menu):
        if idx == len(menu) - 1:
            print(f"0. {label}")
        else:
            print(f"{idx + 1}. {label}")


def wait_back_to_menu():
    while True:
        back = input(f"{BLUE}\nEnter 0 to back to menu: {RESET}").strip()
        if back == "0":
            break
        else:
            print(f"{RED}Invalid input. Please enter 0.{RESET}")


def main():
    print(f"{INDIGO}=== Welcome to SmartApp ==={RESET}")

    user = get_user_profile()
    content = {}
    usage = init_usage()
    shopping_result = None

    while True:
        menu = build_menu(user)
        show_menu(menu)

        choice = input(f"{BLUE}Enter your choice: {RESET}").strip()

        if choice == "0":
            action = "exit"
        elif choice.isdigit() and 1 <= int(choice) <= len(menu) - 1:
            action = menu[int(choice) - 1][1]
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")
            continue

        # ---------- Exit ----------
        if action == "exit":
            print(f"{YELLOW}\nThank you for using SmartApp. Goodbye!{RESET}")
            break

        # ---------- Learning ----------
        elif action == "learning":
            content["learning"] = learning_recommendation(user)
            usage = track_usage(usage, "learning")

        # ---------- Entertainment ----------
        elif action == "entertainment":
            content["entertainment"] = entertainment_recommendation(user)
            usage = track_usage(usage, "entertainment")

        # ---------- Shopping ----------
        elif action == "shopping":
            shopping_result = shopping_recommendation(user)
            content["shopping"] = shopping_result
            usage = track_usage(usage, "shopping")

        # ---------- Usage ----------
        elif action == "usage":
            print("\n--- Usage Analysis ---")
            if usage["total_time"] == 0:
                print("Please use the app first.")
            else:
                print(f"Total Time: {usage['total_time']} minutes")
                print(f"Learning Time: {usage['learning_time']} minutes")
                print(f"Entertainment Time: {usage['entertainment_time']} minutes")
                print(f"Shopping Time: {usage['shopping_time']} minutes")

            wait_back_to_menu()

        # ---------- Risk ----------
        elif action == "risk":
            print("\n--- Risk Analysis ---")
            if usage["total_time"] == 0:
                print("Please use the app first.")
            else:
                risk = analyze_risk(user, usage, shopping_result)
                print(f"Addiction Risk Level: {risk['addiction_risk']}")
                print(f"Spending Risk Level: {risk['spending_risk']}")

            wait_back_to_menu()

        # ---------- Report ----------
        elif action == "report":
            if usage["total_time"] == 0:
                print("Please use the app first.")
            else:
                risk = analyze_risk(user, usage, shopping_result)
                generate_report(user, usage, content, risk)

            wait_back_to_menu()


if __name__ == "__main__":
    main()