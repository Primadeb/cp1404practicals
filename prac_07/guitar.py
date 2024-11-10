class Guitar:
    """Represent a Guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance.

        name: str, the name of the guitar (default "")
        year: int, the year the guitar was made (default 0)
        cost: float, the cost of the guitar (default 0)
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
