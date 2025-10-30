# Program to read a file and handle errors

filename = "sample.txt"

try:
    with open(filename, "r") as file:
        print("Reading file content:\n")
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
