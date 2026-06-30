
students = [
    {"name": "Maria", "age": "22", "grade": "B"},
    {"name": "Carlos", "age": "35", "grade": "A"},
    {"name": "Ana", "age": "28", "grade": "C"},
    {"name": "Sergio", "age": "29", "grade": "A"},
]

# Your turn: use min() with a lambda to find the student
# with the best grade (alphabetically first)
best_student = min(students, key=lambda s: s["grade"])

print(f"Best grade: {best_student['name']} with grade {best_student['grade']}")
