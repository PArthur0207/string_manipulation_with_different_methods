# Ask the user to input a string and the total width of the output
string = input("Please enter your string here: ")
width = int(input("Please enter your desired width here: "))

# Check if width is shorter than the string then print the string without changes
if len(string) >= width:
    print(string)

# If width is longer then ensure that width is equal to the characters + padding on the left + padding on the right
else:
    total_padding = width - len(string)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    # Print the output when centered
    print(' ' * left_padding + string + ' ' * right_padding)