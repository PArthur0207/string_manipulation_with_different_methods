# Ask the user to input a string and their desired width for the output
string = input("Please enter the string here: ")
width = int(input("Please input your desired width here: "))

# Ask the user what to fill the padding with, space if none is entered
filler = input("Please enter what you want to pad it with: ") or " "

# Check if the width is shorter than the string then make no changes to the string
if len(string) > width:
    print(string)

# If the width is longer then pad the spaces on the right using the inputted fill (Reads only the 0th index)
else:
    print(string + (filler[0] * (width - len(string))))