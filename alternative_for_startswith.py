# Ask the user to input a string and the prefix to be checked
string = input("Please input a string here: ")
prefix = input("Please input the prefix to be checked: ")

# Check if the end of the string matches the prefix
if string[:len(prefix)] == prefix:
    starts_with = True
else:
    starts_with = False

# Print True or False
print(f"starts_with = {starts_with}")