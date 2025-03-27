# Ask the user to input a string and the prefix to remove
string = input("Please input your string here: ")
prefix = input("Please input the prfix to be removed from the string: ")

# Check if the start of the string matches with the prefix
if string[:len(prefix)] == prefix:
    print(string[len(prefix):]) # Print the string with the prefix removed if it matches
else:
    print(string) # Print the string without change if it does not