# Count Characteristics in the file
file_path = 'basic_file.txt'
character_count = 0
with open(file_path) as file:
    for line in file:
        character_count += len(line.replace(' ','').strip('\n'))
print(character_count)