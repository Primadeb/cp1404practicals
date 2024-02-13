"""
CP1404 - prac_02
Program to determine score statue
"""
import random

def determine_score_status(score):
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
    user_result = determine_score_status(user_score)
    print("User score result:", user_result)

    random_score = random.randint(0, 100)
    random_result = determine_score_status(random_score)
    print("Random score result:", random_result)


main()
