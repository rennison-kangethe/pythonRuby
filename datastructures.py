#list structure, ordered, index, mutable

fruits = ["mangoes", "apples", "bananas", "pineapples"]
fruits[1] = "Watermelon"
num = [1,2,-3,24,5,6,77,8,9,10]

print(fruits)
print(f"I love eating {fruits[1]}")

for i in fruits:
    print(i)
print(num)

#tuples datastructures, ordered, index, immutable
cars = ("subaru", "mercedes", "volkswagen", "nissan")
print(cars)
print(f"I love {cars[1]} cars")

#set data structures, unordered, not indexed
colors = {"black", "white", "yellow","green", "orange", "blue"}
print(colors)

#dictionaries data structures, mutable, key value pairs
staff = {"name": "Rennison", "email": "rennie@gmail.com", "age": 18, "salary":800000}
print(staff)
print(staff['name'])

# Creating a list
fruits = ["apple", "banana", "mango"]

# Adding an element
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'mango', 'orange']

# Inserting at a specific position
fruits.insert(1, "grape")
print(fruits)  # Output: ['apple', 'grape', 'banana', 'mango', 'orange']

# Removing an element
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'grape', 'mango', 'orange']

# Slicing a list
print(fruits[1:3])  # Output: ['grape', 'mango']

# List comprehension example
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Creating a tuple
coordinates = (10, 20)

# Accessing elements
print(coordinates[0])  # Output: 10

# Tuple unpacking
x, y = coordinates
print(x, y)  # Output: 10 20

# Creating a single-element tuple
single = (5,)
print(type(single))  # Output: <class 'tuple'>

# Tuple concatenation
new_tuple = coordinates + (30, 40)
print(new_tuple)  # Output: (10, 20, 30, 40)


# Creating a set
numbers = {1, 2, 3, 2}  # Duplicate 2 will be removed
print(numbers)  # Output: {1, 2, 3}

# Adding an element
numbers.add(4)
print(numbers)  # Output: {1, 2, 3, 4}

# Removing an element
numbers.discard(3)  # Removes if present, else does nothing
print(numbers)  # Output: {1, 2, 4}

# Set operations
even = {2, 4, 6}
print(numbers.union(even))  # Output: {1, 2, 4, 6}
print(numbers.intersection(even))  # Output: {2, 4}

# Checking membership
print(2 in numbers)  # Output: True


# Creating a dictionary
person = {"name": "Alice", "age": 25}

# Accessing a value by key
print(person["name"])  # Output: Alice

# Adding a new key-value pair
person["city"] = "Nairobi"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Nairobi'}

# Modifying a value
person["age"] = 26
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'Nairobi'}

# Removing a key-value pair
person.pop("city")
print(person)  # Output: {'name': 'Alice', 'age': 26}

# Looping through keys and values
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 26

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 4)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9}
