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

