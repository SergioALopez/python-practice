# LISTS - ordered collections of items
fruits = ["apple", "banana", "mango", "orange"]

print(fruits[0])	#first item (starts at 0)
print(fruits[-1])	#last item
print(len(fruits))	#how amny items

for fruit in fruits:
	print(f"I like {fruit}")

# DICTIONARIES - key/value pairs
person = {
	"name": "Sergio",
	"age": 29,
	"city": "Tlaquepaque" 
}

print(person["name"])
print(f"{person['name']} is {person['age']} years old.")

# Add a new key
person["job"] = "developer"
print(person)

# LIST COMPREHENSIONS - build lists in one line
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Old way
evens = []
for n in numbers:
	if n % 2 == 0:
		evens.append(n)

# Python way - same result in one line
evens_faster = [n for n in numbers if n % 2 == 0]

print(evens)
print(evens_faster)
