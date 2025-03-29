# Ask the user to iput a string
string = input("Please input a string here: ")

# Read every character in the string
for character in string:
    if 'A' <= character <= 'Z':
        all_lower = False
        break
    else:
        all_lower = True

# If a lower case letter is found return false, if not then return true 
print(f"is_lower = {all_lower}")