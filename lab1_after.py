"""Student Record Management System (refactored version)."""

students = []  # each student is a dictionary: {"id", "name", "gpa"}


def show_menu():
    """Print the menu options."""
    print("\n--- Student Record Management ---")
    print("1. Add student")
    print("2. Show all students")
    print("3. Find student")
    print("4. Delete student")
    print("5. Exit")


def add_student():
    """Read student details from the user and store them."""
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    gpa = float(input("Enter GPA: "))
    students.append({"id": student_id, "name": name, "gpa": gpa})
    print("Student added.")


def display_student(student):
    """Print one student record."""
    print(f"ID: {student['id']} | Name: {student['name']} | GPA: {student['gpa']}")


def show_all_students():
    """Print every stored record."""
    if not students:
        print("No records found.")
    for student in students:
        display_student(student)


def find_student(student_id):
    """Return the student with the given ID, or None."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def search_student():
    """Ask for an ID and display the matching record."""
    student = find_student(input("Enter student ID: "))
    if student:
        display_student(student)
    else:
        print("Student not found.")


def delete_student():
    """Ask for an ID and remove the matching record."""
    student = find_student(input("Enter student ID: "))
    if student:
        students.remove(student)
        print("Student deleted.")
    else:
        print("Student not found.")


def main():
    """Run the menu loop until the user exits."""
    actions = {"1": add_student, "2": show_all_students,
               "3": search_student, "4": delete_student}
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
