"""CP1404 Prac - 05
State names in a dictionary
File needs reformatting
"""
# Dictionary containing state abbreviations and names
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

# Printing al  states and names
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

# Asking user for input and displaying corresponding state name
state_code = input("Enter short state: ").upper()

while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
