# Ask the user to input the string and the parameter to be found
string = input("Please input your string here: ")
find = input("Please input the parameter to be found here: ")

# Check all the characters in the sring from the left until the paramter is matched
index = -1
for i in range(len(string) - len(find) + 1):
    if string[i:i + len(find)] == find:
        index = i
        break

# Print the location of the parameter
print(f"Parameter {find} is in the {index} position")