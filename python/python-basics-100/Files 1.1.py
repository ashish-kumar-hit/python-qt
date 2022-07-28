# Print the First n-lines of a file
file_path = 'basic_file.txt'
n = int(input("Enter How many lines you want to read: ? "))
with open(file_path) as file:
    lines = file.readlines()
    num_lines = len(lines)

    if n > num_lines:
        print(f"Please enter a valid input. The file has {num_lines} lines")
    else:
        for i in range(n):
            print(lines[i].strip("\n"))
