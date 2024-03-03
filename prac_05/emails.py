"""
User Email Storage
Estimate: 25 minutes
Actual:   35 minutes
"""

def extract_name(email):
    """Extracts name from email address."""
    name_parts = email.split('@')[0].split('.')
    name = ' '.join(name_parts).title()
    return name

# Initialize dictionary to store emails and names
user_info = {}

# Input loop
email = input("Email: ")
while email != "":
    name_from_email = extract_name(email)
    user_name = input(f"Is your name {name_from_email}? (Y/n) ").strip().lower()
    if user_name == 'n':
        user_name = input("Name: ").strip().title()
    elif user_name != 'y':
        user_name = name_from_email
    user_info[email] = user_name
    email = input("Email: ")

# Print stored emails and names
for email, name in user_info.items():
    print(f"{name} ({email})")
