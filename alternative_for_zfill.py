# Ask the user to input the string and the width to be filled
string = input("Please enter your string here: ")
width = int(input("Please enter the total width of the output here: "))

# Print the 0s in the beggining of the string if the width is greater than the length of the string
if width > len(string):
    print("0" * (width - len(string)) + string)

# No changes in the string if the width is less than the length of the string
else:
    print(string)