# Ask the user for an input with lowercases
string = input("Please input a string containing lowercase letters here: ")

# Check every character in the string
for character in string:   
    # If the character is within a-z convert it into capital letters using their respective ASCII values
    if 'a' <= character <= 'z':
        print(chr(ord(character) - 32))

# Print the result in all uppercase