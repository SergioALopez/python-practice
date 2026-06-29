import csv

def read_students(filename):
	students = []
	try:
		with open(filename) as f:
			reader = csv.DictReader(f)
			for row in reader:
				students.append(row)
	except:
		print(f"Error: {filename} not found.")
	return students

def print_summary(students):
	print(f"\n--- Student Summary ---")
	print(f"Total students: {len(students)}")

	grades = [s["grade"] for s in students]
	ages = [int(s["age"]) for s in students]

	print(f"Average age: {sum(ages) / len(ages):.1f}")
	print(f"Grade A students: {grades.count('A')}")
	print(f"Grade B students: {grades.count('B')}")
	print(f"Grade C students: {grades.count('C')}")

	print(f"\nFull list:")
	for s in students:
		print(f"{s['name']} - Age {s['age']} - Grade {s['grade']}")

students = read_students("students.csv")
if students:
	print_summary(students)
