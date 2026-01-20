# learning_module.py

def learning_recommendation(user):
    print("\n--- Learning Recommendations ---")

    interests = user.get("learning_interest", [])
    recommendations = []

    if not interests:
        print("No learning interests selected.")
        return {
            "interests": [],
            "recommendations": []
        }

    for interest in interests:
        if interest == "Music":
            print("\n[Music Learning]")
            print("- Beginner Music Theory Course")
            print("- Piano Basics for Self-Learners")
            print("- Ear Training Exercises")

            recommendations.append({
                "category": "Music",
                "content": [
                    "Beginner Music Theory Course",
                    "Piano Basics for Self-Learners",
                    "Ear Training Exercises"
                ],
                "learning_goal": "Understand basic music structure and rhythm"
            })

        elif interest == "Cooking":
            print("\n[Cooking Learning]")
            print("- Home Cooking for Beginners")
            print("- Healthy Meal Preparation")
            print("- Basic Knife Skills Tutorial")

            recommendations.append({
                "category": "Cooking",
                "content": [
                    "Home Cooking for Beginners",
                    "Healthy Meal Preparation",
                    "Basic Knife Skills Tutorial"
                ],
                "learning_goal": "Prepare simple and healthy meals independently"
            })

        elif interest == "Fitness":
            print("\n[Fitness Learning]")
            print("- 20-Minute Daily Home Workout")
            print("- Beginner Strength Training Guide")
            print("- Stretching and Flexibility Routine")

            recommendations.append({
                "category": "Fitness",
                "content": [
                    "20-Minute Daily Home Workout",
                    "Beginner Strength Training Guide",
                    "Stretching and Flexibility Routine"
                ],
                "learning_goal": "Improve physical fitness and daily activity level"
            })

        elif interest == "Art":
            print("\n[Art Learning]")
            print("- Introduction to Digital Drawing")
            print("- Color Theory Basics")
            print("- Simple Illustration Practice")

            recommendations.append({
                "category": "Art",
                "content": [
                    "Introduction to Digital Drawing",
                    "Color Theory Basics",
                    "Simple Illustration Practice"
                ],
                "learning_goal": "Develop basic visual creativity skills"
            })

        elif interest == "Science":
            print("\n[Science Learning]")
            print("- Popular Science Video Series")
            print("- Everyday Physics Explained")
            print("- Science Experiments at Home")

            recommendations.append({
                "category": "Science",
                "content": [
                    "Popular Science Video Series",
                    "Everyday Physics Explained",
                    "Science Experiments at Home"
                ],
                "learning_goal": "Increase curiosity and understanding of science concepts"
            })

    return {
        "interests": interests,
        "recommendations": recommendations
    }
