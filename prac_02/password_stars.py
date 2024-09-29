"""
CP1404 - prac_02
Get a password with minimum length and display asterisks
"""
def get_password():
    password = input("Enter your password: ") # Get the password from user input
    return password

def print_password_asterisks(password):
    print('*' * len(password))

def main():
    """Main function to execute password input and display."""
    password = get_password()
    print_password_asterisks(password)


main()
