# entertainment_module.py

def entertainment_recommendation(user):
    print("\n--- Entertainment Recommendations ---")

    interests = user.get("entertainment_interest", [])
    recommendations = []

    if not interests:
        print("No entertainment interests selected.")
        return {
            "interests": [],
            "recommendations": []
        }

    for interest in interests:
        if interest == "Anime":
            print("\n[Anime Content]")
            print("- Popular Action Anime Series")
            print("- Slice of Life Anime Collection")
            print("- Top Rated Anime Movies")

            recommendations.append({
                "category": "Anime",
                "content": [
                    "Popular Action Anime Series",
                    "Slice of Life Anime Collection",
                    "Top Rated Anime Movies"
                ],
                "entertainment_value": "Relaxation and immersive storytelling"
            })

        elif interest == "Travel":
            print("\n[Travel Content]")
            print("- Travel Vlogs Around the World")
            print("- Budget Travel Tips")
            print("- Cultural Exploration Videos")

            recommendations.append({
                "category": "Travel",
                "content": [
                    "Travel Vlogs Around the World",
                    "Budget Travel Tips",
                    "Cultural Exploration Videos"
                ],
                "entertainment_value": "Inspiration and cultural exposure"
            })

        elif interest == "Variety Shows":
            print("\n[Variety Shows Content]")
            print("- Popular Game Shows")
            print("- Celebrity Interview Programs")
            print("- Reality Entertainment Series")

            recommendations.append({
                "category": "Variety Shows",
                "content": [
                    "Popular Game Shows",
                    "Celebrity Interview Programs",
                    "Reality Entertainment Series"
                ],
                "entertainment_value": "Light-hearted fun and social engagement"
            })

        elif interest == "Comedy":
            print("\n[Comedy Content]")
            print("- Stand-up Comedy Specials")
            print("- Short Comedy Skits")
            print("- Sitcom Highlights")

            recommendations.append({
                "category": "Comedy",
                "content": [
                    "Stand-up Comedy Specials",
                    "Short Comedy Skits",
                    "Sitcom Highlights"
                ],
                "entertainment_value": "Stress relief and mood enhancement"
            })

    return {
        "interests": interests,
        "recommendations": recommendations
    }
