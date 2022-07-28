# Copy the content of the file to another file
file_path = "basic_file.txt"
copy_path = 'basic_file_copy1.txt'
with open('basic_file.txt') as file, open('basic_file_copy1.txt','w') as copy:
    for line in file:
        copy.write(line)
