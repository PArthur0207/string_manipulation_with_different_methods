# Ask the user for an input with lowercases
string = input("Please input a string containing lowercase letters here: ")

# Check every character in the string
for character in string:
    print(character)
    
# If the character is within a-z convert it into capital letters using their respective ASCII values
# Print the result in all uppercase