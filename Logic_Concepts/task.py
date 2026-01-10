class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.student_grades = {}  # Dictionary to store {Student_Name: Grade}

    def assign_grade(self, student_name, grade):
        """Adds or updates a grade for a specific student."""
        self.student_grades[student_name] = grade
        print(f"[Success] {self.name} assigned a grade of {grade} to {student_name}.")

    def get_report_card(self):
        """Prints all students and their assigned grades."""
        print(f"\n--- {self.subject} Report Card (Instructor: {self.name}) ---")
        if not self.student_grades:
            print("No grades assigned yet.")
        else:
            for student, grade in self.student_grades.items():
                print(f"Student: {student:10} | Grade: {grade}")

# --- Execution ---
# 1. Create a Teacher object
math_teacher = Teacher("Mr. Smith", "Mathematics")

# 2. Assign grades
math_teacher.assign_grade("Alice", "A")
math_teacher.assign_grade("Bob", "B+")
math_teacher.assign_grade("Charlie", "A-")

# 3. View the results
math_teacher.get_report_card()