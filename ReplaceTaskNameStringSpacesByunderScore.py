def replace_spaces_with_underscore(string):
    return string.replace(" ", "_")

# Ask the user to enter a string
input_string = input("Enter a string: ")

# Replace spaces with "_\"
result = replace_spaces_with_underscore(input_string)

# Print the result
print("Modified string:", result)