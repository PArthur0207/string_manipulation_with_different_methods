# Ask the user to input a string
string = input("Please input a string with spaces in the end: ")

# Remove the spaces at the end of the string
while string and string[-1] == " ":
    string = string[:-1]
    
# Print the result  
print(string + ' end') # Add 'end' at the end to see that the spaces are goone at the end