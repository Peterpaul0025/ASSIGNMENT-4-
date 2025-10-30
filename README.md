# ASSIGNMENT-4-

TASK 1: Read a File and Handle Errors Gracefully
This Python program reads and displays the contents of a text file named sample.txt. It uses a try-except block to handle errors gracefully in case the file does not exist.
If the file is found, it prints each line with its corresponding line number.
If the file is missing, it displays a user-friendly error message indicating that the file could not be found.
This helps prevent the program from crashing and makes file operations more reliable.

Key Concepts Used:
File handling (open, read, with statement)
Error handling (try-except, FileNotFoundError)
Looping through file lines (enumerate)

TASK 2: Write, Append, and Read a File
This Python program demonstrates writing, appending, and reading data from a file named output.txt.
First, it takes input from the user and writes it to the file. Next, it asks for additional text and appends it to the same file without erasing the previous data. Finally, it opens the file in read mode and displays the complete content.
This program helps understand how to manage file data dynamically and efficiently using different file modes.

Key Concepts Used:
File modes:
"w" → Write (creates or overwrites file)
"a" → Append (adds data to end of file)
"r" → Read (reads file content)
User input handling
Reading and displaying file contents
