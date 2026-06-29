def greet(name, age):
	years_left = 100 - int(age)
	print(f"Hello, {name}!")
	print(f"You have {years_left} years until you turn 100.")

greet("Sergio", 29)
greet("Maria", 45)
greet("Carlos", 17)

def calculate_years(age):
	return 100 - age

years = calculate_years(29)
print(f"Years until 100: {years}")
print(f"Double that: {years * 2}")
