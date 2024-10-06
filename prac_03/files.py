"""CP1404
prac03"""
# task 1
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# task 2
with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Your name is {name}")

# task 3
with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
    total = num1 + num2
print(f"The sum of the first two numbers is: {total}")

# task 4
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print(f"The sum of all numbers in numbers.txt is: {total}")
