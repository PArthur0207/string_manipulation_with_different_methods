# Ask the user to input a string with capital letters
string = input("Please enter a string with capital letters: ")
# Check every character in the string if it is a capital letter
for character in string:
    if 'A' <= character <= 'Z':
        character = chr(ord(character) + 32) # Convert to lowercase using the ASCII
        print(character)

# Print the result with all lowercase