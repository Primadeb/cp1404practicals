"""
CP1404 - prac04
total income
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))  # Renamed months to num_months for better clarity

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Changed to f-string for better readability
        incomes.append(income)

    print("\nIncome Report\n-------------")
    print_report(num_months, incomes)


def print_report(num_months, incomes):
    """Print income report with cumulative totals."""
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
