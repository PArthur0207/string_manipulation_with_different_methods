# Ask the user to input a string
string = input("Please input the string here: ")

# Capitalize the 0th character and turn the rest into lowercase
output = string[0].upper() + string[1:].lower()

# Print the result
print(output)