# Accessing, inserting, updating, and deleting key-value pairs
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Accessing
name = my_dict["name"]

# Inserting
my_dict["job"] = "Engineer"

# Updating
my_dict["age"] = 35

# Deleting
del my_dict["city"]

# Iterating through keys, values, or items
for key in my_dict.keys():
    print("Key:", key)

for value in my_dict.values():
    print("Value:", value)

for key, value in my_dict.items():
    print(key, ":", value)

# Dictionary comprehension
squared_values = {key: value ** 2 for key, value in my_dict.items()}

# Common dictionary methods
job = my_dict.get("job")
keys = my_dict.keys()
values = my_dict.values()

print("Name:", name)
print("Updated Dictionary:", my_dict)
print("Job:", job)
print("Keys:", keys)
print("Values:", values)
print("Squared Values:", squared_values)
