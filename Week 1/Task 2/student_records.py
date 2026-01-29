# Database: Dictionary with Student ID as key
students = {}

def add_student(student_id, name, grade):
    if student_id in students:
        print("Student ID already exists.")
    else:
        students[student_id] = {'name': name, 'grade': grade}
        print(f"Student {name} added.")

def update_grade(student_id, new_grade):
    if student_id in students:
        students[student_id]['grade'] = new_grade
        print(f"Grade updated for {students[student_id]['name']}.")
    else:
        print("Student ID not found.")

def display_students():
    print("\n--- Student Records ---")
    for s_id, data in students.items():
        print(f"ID: {s_id} | Name: {data['name']} | Grade: {data['grade']}")
    print("-----------------------\n")

if __name__ == "__main__":
    add_student("001", "Ali", "A")
    add_student("002", "Zara", "B")
    update_grade("001", "A+")
    display_students()