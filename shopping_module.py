# shopping_module.py

def shopping_recommendation(user):
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print(f"\n{YELLOW}--- Shopping Recommendations ---{RESET}")


    interests = user.get("shopping_interest", [])
    budget = user.get("budget", None)
    recommendations = []

    if not interests:
        print("No shopping interests selected.")
        return {
            "interests": [],
            "recommendations": [],
            "budget": budget,
            "status": "Viewed Only"
        }

    # Modified product catalog with prices
    product_catalog = {
        "Electronics": [("Wireless Earbuds", 50), ("Smart Watch", 120), ("Portable Charger", 30)],
        "Fashion": [("T-shirt", 20), ("Jeans", 40), ("Sneakers", 60)],
        "Sports Goods": [("Yoga Mat", 25), ("Dumbbell Set", 70), ("Running Shoes", 80)]
    }

    for interest in interests:
        print(f"\n[{interest} Products]")

        products = product_catalog.get(interest, [])
        affordable_products = []

        for product, price in products:
            if budget is None or price <= budget:
                print(f"- {product} (${price})")
                affordable_products.append({"name": product, "price": price})
            else:
                print(f"- {product} (${price}) - Over budget")

        recommendations.append({
            "category": interest,
            "products": affordable_products
        })


    status = "Viewed Only"
    if budget is not None:
        for r in recommendations:
            if r["products"]:
                status = "Purchased"
                break

    return {
        "interests": interests,
        "recommendations": recommendations,
        "budget": budget,
        "status": status
    }