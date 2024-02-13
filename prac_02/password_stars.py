"""
CP1404 - prac_02
Get a password with minimum length and display asterisks
"""
def get_password():
    password = input("Enter password: ")
    return password

def print_password_asterisks(password):
    print('*' * len(password))

def main():
    password = get_password()
    print_password_asterisks(password)


main()
