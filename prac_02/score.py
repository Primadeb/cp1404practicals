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
