# Ask the user to input a string and the suffix to be checked
string = input("Please input the string: ")
suffix = input("Please input the suffix to be checked: ")

# Check if the end of the string matches the suffix
if string[-len(suffix):] == suffix:
    ends_with = True
else:
    ends_with = False

# Print True or False
print(ends_with)