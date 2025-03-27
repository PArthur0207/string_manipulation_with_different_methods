# Ask the user to input a string
string = input("Input your string here: ")

# Split the string into words
words = string.split()

output = "" # Initialized output as spaceholder

# Capitalize the first letter of each word
for i in words:
    output += i.capitalize() + " "

# Print the result of each word
print(output)