# Asks the user to input the string and the parameter to find
string = input("Please enter a string here: ")
find = input("Please input the parameter to be found here: ")

# Look for the parameter within the string starting from the end
index = -1
for i in range(len(string) - len(find), -1, -1):
    if string[i:i + len(find)] == find:
        index = i
        break

# Print the location of the parameter starting from the end
print(f"The parameter: {find}, is in the {index} position")