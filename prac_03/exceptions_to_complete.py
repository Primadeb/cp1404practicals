"""
CP1404 - Prac 03
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: Set is_finished to True to exit the loop
        is_finished = True
    except ValueError:  # TODO: Catch ValueError exception
        print("Please enter a valid integer.")
print("Valid result is:", result)
