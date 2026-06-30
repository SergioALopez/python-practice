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

def print_old_young(students):
	oldest = 0
	youngest = 100
	ages = [int(s["age"]) for s in students]
	for age in ages:
		if age > oldest:
			oldest = age
		if age < youngest:
			youngest = age
	print(f"Oldest age -> {oldest}")
	print(f"Youngest age -> {youngest}")
	for s in students:
		if s['age'] == str(oldest):
			print(f"\noldest student -> {s['name']}, age: {s['age']}")
		if s['age'] == str(youngest):
			print(f"youngest student -> {s['name']}, age: {s['age']}")

students = read_students("students.csv")
if students:
	print_summary(students)
	print_old_young(students)
