def generate_report(user, usage, content, risk):
    """
    Generate a final user behavior and risk assessment report.
    """

    print("\n========== SMARTAPP USER REPORT ==========\n")

    # ---------- User Profile ----------
    print("User Profile:")
    print(f"- Age: {user['age']}")
    print(f"- Primary Purpose: {user['purpose']}")

    # ---------- Usage Summary ----------
    print("\nUsage Analysis:")
    print(f"- Total Usage Time: {usage['total_time']} minutes")
    print(f"- Learning Time: {usage['learning_time']} minutes")
    print(f"- Entertainment Time: {usage['entertainment_time']} minutes")
    print(f"- Shopping Time: {usage['shopping_time']} minutes")

    # ---------- Content Summary ----------
    print("\nContent Engagement:")
    if "learning" in content:
        print("- Learning content was accessed.")
    if "entertainment" in content:
        print("- Entertainment content was accessed.")
    if "shopping" in content:
        print("- Shopping features were used.")

    # ---------- Risk Analysis ----------
    print("\nRisk Assessment:")
    print(f"- Addiction Risk Level: {risk['addiction_risk']}")
    print(f"- Spending Risk Level: {risk['spending_risk']}")

    # ---------- Social Impact Conclusion ----------
    print("\nConclusion:")
    if risk["addiction_risk"] == "Low":
        print(
            "The user demonstrates a healthy and balanced usage pattern, "
            "with positive engagement in learning-oriented content."
        )
    elif risk["addiction_risk"] == "Medium":
        print(
            "The user shows moderate usage behavior. While learning benefits are present, "
            "attention should be given to entertainment consumption habits."
        )
    else:
        print(
            "The user exhibits a high risk of digital addiction due to excessive usage time, "
            "particularly in entertainment-related activities."
        )

    if risk["spending_risk"] == "High":
        print(
            "Additionally, the user displays signs of impulsive spending behavior, "
            "which may lead to financial risks."
        )

    print("\n========== END OF REPORT ==========\n")