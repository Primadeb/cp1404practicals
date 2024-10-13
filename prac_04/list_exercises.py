"""
CP1404 - prac04
Data file -> lists program
"""
# Define the main function to handle input and display results
def main():
    numbers = []

    for i in range(5):
        number = float(input("Number: ")) ## Get a number and convert it to float
        numbers.append(number) # # Add the number to the list.

    # Display the first and last numbers from the list.
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

main()
