# Ask the user to input a string and the parameter to find
string = input("Please input your string here: ")
parameter = input("Please input the parameters to be found in the string here: ")

count = 0 # Initializd count

# Loop accross the string to find the parameter
for i in range(len(string) - len(parameter) + 1):
    # Count the number of times it is found in the string
    if string[i:i + len(parameter)] == parameter:
        count += 1

# Print the results