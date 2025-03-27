# Ask the user to input a string with leading spaces
string = input("Please input a string with leading spaces: ")

# Count the leading spaces
space_count = 0
while string[space_count] == " ":
    space_count += 1

# Print the result starting from the first characer that is not a space
print(string[space_count:])