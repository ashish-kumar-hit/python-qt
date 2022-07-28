# Print the last n-lines of the files
file_path = 'basic_file.txt'
n = int(input("How many lines you want print: ? "))
with open(file_path) as file:
    lines = file.readlines()
    num_line = len(lines)

    if n > num_line:
        print(f"Please enter a valid value. The file have {num_line} lines")
    else:
        for i in range(-n, 0):
            print(lines[i].strip('\n'))