ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

def init_usage():
    """
    Initialize usage data for one user session
    """
    return {
        "total_time": 0,
        "learning_time": 0,
        "entertainment_time": 0,
        "shopping_time": 0,
        "learning_ratio": 0.0,
        "entertainment_ratio": 0.0,
        "shopping_ratio": 0.0
    }


def track_usage(usage, activity):
    """
    Track usage based on actual user activity
    activity: 'learning' | 'entertainment' | 'shopping'
    """

    time_spent = int(input(f"{ORANGE}\nHow many minutes did you spend? {RESET}"))

    usage["total_time"] += time_spent

    if activity == "learning":
        usage["learning_time"] += time_spent
    elif activity == "entertainment":
        usage["entertainment_time"] += time_spent
    elif activity == "shopping":
        usage["shopping_time"] += time_spent

    # Update ratios
    if usage["total_time"] > 0:
        usage["learning_ratio"] = usage["learning_time"] / usage["total_time"]
        usage["entertainment_ratio"] = usage["entertainment_time"] / usage["total_time"]
        usage["shopping_ratio"] = usage["shopping_time"] / usage["total_time"]

    return usage