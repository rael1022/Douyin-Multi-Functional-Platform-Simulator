def analyze_risk(user, usage, shopping_result):
    age = user["age"]
    total_time = usage["total_time"]
    entertainment_ratio = usage["entertainment_ratio"]

    # ---------- Addiction Risk ----------
    if total_time >= 180 or entertainment_ratio >= 0.7:
        addiction_risk = "High"
    elif total_time >= 90 or entertainment_ratio >= 0.5:
        addiction_risk = "Medium"
    else:
        addiction_risk = "Low"

    if age < 18 and addiction_risk == "Low":
        addiction_risk = "Medium"

    # ---------- Spending Risk ----------
    spending_risk = "Low"

    if shopping_result and shopping_result.get("recommendations"):
        for category in shopping_result["recommendations"]:
            if category["products"]:
                spending_risk = "Medium"

        if shopping_result.get("budget") is not None and shopping_result["budget"] < 50:
            spending_risk = "High"

    return {
        "addiction_risk": addiction_risk,
        "spending_risk": spending_risk
    }