"""
Cp1404 - prac_02
temperature conversion
"""
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Get user input and print output outside the functions
def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")


main()
