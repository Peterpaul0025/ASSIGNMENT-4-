# Program: Write, Append, and Read from a File

filename = "output.txt"

# Step 1: Write user input to the file
text_to_write = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(text_to_write + "\n")
print(f"Data successfully written to {filename}.\n")

# Step 2: Append additional text
text_to_append = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.\n")

# Step 3: Read and display the final content
print(f"Final content of {filename}:")
with open(filename, "r") as file:
    content = file.read()
    print(content)
