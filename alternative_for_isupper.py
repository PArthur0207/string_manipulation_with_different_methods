# Ask the user to input a string to check if all is uppercase
string = input("Please input a string to check if all is uppercase: ")

# Check for lowercase in every character, false if found, true if not found
for character in string:
    if 'a' <= character <= 'z':
        all_upper = False
        break
    else:
        all_upper = True

# Print the results