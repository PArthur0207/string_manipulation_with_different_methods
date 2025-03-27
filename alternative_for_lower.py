# Ask the user to input a string with capital letters
string = input("Please enter a string with capital letters: ")

output = "" # Initialized placeholder for the printed output

# Check every character in the string if it is a capital letter
for character in string:
    if 'A' <= character <= 'Z':
        output += chr(ord(character) + 32) # Convert to lowercase using the ASCII
    else:
        output += character

# Print the result with all lowercase
print(output)