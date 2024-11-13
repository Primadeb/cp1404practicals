import datetime
import csv
from project import Project

FILENAME = "projects.txt"

def main():
    """Main function to manage projects."""
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            if input("Would you like to save to projects.txt? (y/n): ").lower() == "y":
                save_projects(FILENAME, projects)
            print("Thank you for using the project management software.")
            break
        else:
            print("Invalid choice")

def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)  # Skip header
            for row in reader:
                projects.append(Project(*row))
    except FileNotFoundError:
        print(f"Warning: {filename} not found.")
    return projects

def save_projects(filename, projects):
    """Save all projects to a file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime("%d/%m/%Y"),
                             project.priority, project.cost_estimate, project.completion_percentage])

def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = [project for project in projects if not project.is_complete()]
    completed = [project for project in projects if project.is_complete()]

    print("\nIncomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(completed):
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Filter and display projects that start after a specified date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = [project for project in projects if project.starts_after(filter_date)]

    print("\nFiltered projects:")
    for project in sorted(filtered, key=lambda x: x.start_date):
        print(f"  {project}")

def add_new_project(projects):
    """Add a new project based on user input."""
    print("\nLet's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))

def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    if 0 <= choice < len(projects):
        project = projects[choice]
        print(project)
        new_percentage = input("New Percentage: ")
        new_priority = input("New Priority: ")
        project.update(new_completion_percentage=new_percentage if new_percentage else None,
                       new_priority=new_priority if new_priority else None)
    else:
        print("Invalid project choice")


main()