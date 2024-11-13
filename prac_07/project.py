import datetime

class Project:
    """Represent a project with relevant details."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less-than comparison based on project priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is complete (100% completion)."""
        return self.completion_percentage >= 100

    def update(self, new_completion_percentage=None, new_priority=None):
        """Update completion percentage and/or priority of the project."""
        if new_completion_percentage is not None:
            self.completion_percentage = int(new_completion_percentage)
        if new_priority is not None:
            self.priority = int(new_priority)

    def starts_after(self, date):
        """Return True if the project starts after the given date."""
        return self.start_date > date