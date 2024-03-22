# Indexing and slicing
my_list = [1, 2, 3, 4, 5]
first_element = my_list[0]
last_three_elements = my_list[-3:]
subset = my_list[1:4]

# Appending, extending, inserting, removing, and popping elements
my_list.append(6)
my_list.extend([7, 8])
my_list.insert(3, 10)
my_list.remove(4)
popped_element = my_list.pop()

# List comprehension
squared_numbers = [x ** 2 for x in my_list]

# Common list methods
index_of_3 = my_list.index(3)
count_of_2 = my_list.count(2)

print("First Element:", first_element)
print("Last Three Elements:", last_three_elements)
print("Subset:", subset)
print("Appended List:", my_list)
print("Popped Element:", popped_element)
print("Squared Numbers:", squared_numbers)
print("Index of 3:", index_of_3)
print("Count of 2:", count_of_2)
