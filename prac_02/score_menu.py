"""
Cp1404 - prac_02
Score menu Program
"""
def main():
    """Main function to execute the score menu."""
    score = get_valid_score() # Get the initial valid score from the user

    choice = display_menu()  # Display the menu and get the user's choice
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option.Please try again.")

        choice = display_menu()

    print("Farewell! Thanks for using the Score Menu.")

