"""CP1404 - Prac-03
"""
import random

# What did you see on line 1?
# Answer: A random integer between 5 and 20 .

# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 5, and the largest is 20.

# What did you see on line 2?
# Answer: A random odd number between 3 and 9.

# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 3, and the largest is 9.
# Line 2 could not have produced a 4 because the step is 2, so it only generates odd numbers.

# What did you see on line 3?
# Answer: A random floating-point number between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 2.5, and the largest is 5.5.

# Write code to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
