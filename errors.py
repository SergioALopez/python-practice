# Without error handling - this CRASHES
# age = int(input("Your age: "))	# try typing "abc" and it breaks

# with error handling
def get_age():
	try:
		age = int(input("Your age: "))
		print(f"In 10 years you'll be {age + 10} years old.")
	except ValueError:
		print("That is not a valid number. Please try again.")

get_age()
