names = []
grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    names.append(name)
    grades.append(grade)
    print(f"{name} added.")


def update_grade():
    name = input("Enter name to update: ")
    if name in names:
        index = names.index(name)
        new_grade = float(input("Enter new grade: "))
        grades[index] = new_grade
        print(f"{name}'s grade updated.")
    else:
        print("Student not found.")


def remove_student():
    name = input("Enter name to remove: ")
    if name in names:
        index = names.index(name)
        names.pop(index)
        grades.pop(index)
        print(f"{name} removed.")
    else:
        print("Student not found.")


def show_average():
    if grades:
        avg = sum(grades) / len(grades)
        print(f"Average grade: {avg:.2f}")
    else:
        print("No students yet.")


def show_high_low():
    if grades:
        print(f"Highest grade: {max(grades)}")
        print(f"Lowest grade: {min(grades)}")
    else:
        print("No students yet.")


def show_all():
    if names:
        print("\nStudents and Grades:")
        for n, g in zip(names, grades):
            print(f"{n}: {g}")
    else:
        print("No students yet.")


while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. Update grade")
    print("3. Remove student")
    print("4. Show average")
    print("5. Show highest & lowest")
    print("6. Show all students")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_grade()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        show_average()
    elif choice == '5':
        show_high_low()
    elif choice == '6':
        show_all()
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")