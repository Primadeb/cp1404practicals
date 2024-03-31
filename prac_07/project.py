"""
Estimated Time: 3 hours
"""
import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name}, {self.start_date.strftime('%d/%m/%Y')}, Priority: {self.priority}, Cost Estimate: {self.cost_estimate}, Completion Percentage: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority
