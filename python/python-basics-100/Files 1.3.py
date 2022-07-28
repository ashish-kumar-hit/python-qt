# Find the longest word in a file
file_path = 'basic_file.txt'
with open(file_path) as file:
    lines = file.readlines()
    count = 0
    for i in range(len(lines)):
        if count < len(lines[i]):
            count = len(lines[i])
    for i in range(len(lines)):
        if count == len(lines[i]):
            print(lines[i])

# Just take a empty string and try to do it using only one for loop