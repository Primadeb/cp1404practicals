"""
CP1404 - prac04
subject reader
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []  # Initialize an empty list to store the data
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_data.append(parts)  # Append the parts to the subject_data list
    input_file.close()
    return subject_data  # Return the list of lists
