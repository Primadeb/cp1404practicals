"""
Hexadecimal Color Code Lookup
Estimate: 30 minutes
Actual:   45 minutes
"""

# Dictionary containing color names and their hexadecimal codes
COLOR_CODES = {
    "Aliceblue": "#F0F8FF",
    "Antiquewhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "Blanchedalmond": "#FFEBCD",
    "Blue": "#0000FF"
}

# Displaying available colors
print("Available Colors:")
for color in COLOR_CODES:
    print(color)

# Start the input loop
color_name = input("Enter color name (or blank to stop): ").capitalize()  # Capitalize input
while color_name != "":
    try:
        print(f"The hexadecimal code for {color_name} is {COLOR_CODES[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name (or blank to stop): ").capitalize()
