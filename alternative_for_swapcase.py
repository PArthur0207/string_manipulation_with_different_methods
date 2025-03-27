# Ask the user for an input of combined lower case and upper case letters
string = input("Please input your string with upper and lower case letters here: ")

output = "" # Initialized placeholder for the output

# For every character in the string check if capital letter and then change it to lowercase using their respective ASCII values
for character in string:
    if 'A' <= character <= 'Z':
        output += chr(ord(character) + 32)
    # Do the same for every lowercase letters turn into uppercase
    elif 'a' <= character <= 'z':
        output += chr(ord(character) - 32)
    # Non alphabetical characters should remain unchanged
    else:
        output += character

# Print the output
print(output)