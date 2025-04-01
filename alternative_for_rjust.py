# Ask the user to input the string and the width
string = input("Please input ypur string here: ")
width = int(input("Please input the total width of the output here: "))

# Check if the length of the string is less than the width then add the spaces, no change if not
if len(string) < width:
    result = " " * (width - len(string)) + string

# Print the results
print(result)