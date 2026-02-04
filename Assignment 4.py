# Program to read a file and print each line with line numbers

try:
    with open("sample.txt", "r") as file:
        # Enumerate gives (index, line), starting index from 1
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line}", end='')  # end='' avoids extra newline
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Program to write, append, and read a file

# Step 1: Take user input and write it to output.txt
user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:  # 'w' mode overwrites if file exists
    file.write(user_input + "\n")  # Add newline after input

# Step 2: Append additional data
additional_data = input("Enter additional text to append: ")
with open("output.txt", "a") as file:  # 'a' mode appends to file
    file.write(additional_data + "\n")  # Add newline after appended text

# Step 3: Read and display the final content
print("\nFinal content of the file:")
try:
    with open("output.txt", "r") as file:
        for line in file:
            print(line, end='')  # Print as is, without extra blank lines
except FileNotFoundError:
    print("Error: The file 'output.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


