"""
CP1404 - prac_02
Program to determine score statue
"""
import random

def determine_score_status(score):
    """Determine the status of the score based on defined thresholds."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    user_score = float(input("Enter score: "))
    # Determine the result based on the user's score
    user_result = determine_score_status(user_score)
    print("User score result:", user_result)

    # Generate a random score between 0 and 100
    random_score = random.randint(0, 100)
    random_result = determine_score_status(random_score)
    print("Random score result:", random_result)


main()
