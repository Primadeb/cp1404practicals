from datetime import datetime

from project import Project


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
                projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    except FileNotFoundError:
        print("File not found. Creating a new file.")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    complete_projects = [project for project in projects if project.completion_percentage == 100]

    print("\nIncomplete Projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(project)

    print("\nComplete Projects:")
    for project in sorted(complete_projects, key=lambda x: x.priority):
        print(project)


def filter_projects_by_date(projects):
    while True:
        try:
            date_input = input("Enter a date (dd/mm/yyyy): ")
            filter_date = datetime.strptime(date_input, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the format dd/mm/yyyy.")
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(project)


def add_new_project(projects):
    name = input("Enter project name: ")
    start_date = input("Enter start date (dd/mm/yyyy): ")
    priority = int(input("Enter priority: "))
    cost_estimate = float(input("Enter cost estimate: "))
    completion_percentage = int(input("Enter completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    project_name = input("Enter the name of the project to update: ")
    for project in projects:
        if project.name == project_name:
            new_completion_percentage = input(
                f"Current completion percentage: {project.completion_percentage}. Enter new completion percentage (or leave blank to retain existing value): ")
            if new_completion_percentage:
                project.completion_percentage = int(new_completion_percentage)
            new_priority = input(
                f"Current priority: {project.priority}. Enter new priority (or leave blank to retain existing value): ")
            if new_priority:
                project.priority = int(new_priority)
            print("Project updated successfully.")
            return
    print("Project not found.")


def main():
    filename = 'projects.txt'
    projects = load_projects(filename)

    while True:
        print("\nMenu:")
        print("L. Load projects")
        print("S. Save projects")
        print("D. Display projects")
        print("F. Filter projects by date")
        print("A. Add new project")
        print("U. Update project")
        print("Q. Quit")

        choice = input("Enter your choice: ")

        if choice == 'L':
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter the filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save_option = input("Do you want to save changes? (yes/no): ")
            if save_option.lower() == 'yes':
                save_projects(filename, projects)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")



main()
