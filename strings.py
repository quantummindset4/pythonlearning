# Concatenation with +
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2

# String formatting
formatted_string = f"{string1.upper()} {string2.lower()}!"

# Indexing and slicing
first_character = concatenated_string[0]
last_three_characters = concatenated_string[-3:]
substring = concatenated_string[6:11]

# Common string methods
stripped_string = "   Python is awesome!   ".strip()
split_string = concatenated_string.split()
replaced_string = concatenated_string.replace("World", "Python")

print("Concatenated String:", concatenated_string)
print("Formatted String:", formatted_string)
print("First Character:", first_character)
print("Last Three Characters:", last_three_characters)
print("Substring:", substring)
print("Stripped String:", stripped_string)
print("Split String:", split_string)
print("Replaced String:", replaced_string)
