class Guitar:
    """Represent a guitar with name, year, and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return the age of the guitar in years."""
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 years or older, False otherwise."""
        return self.get_age(2024) >= 50  # Assuming the current year is 2024

    def __lt__(self, other):
        """Less-than comparison based on year for sorting."""
        return self.year < other.year