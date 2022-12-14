# Make a frequency dictionary of the words in the file
file_path = "basic_file.txt"
freq_dict = {}
with open(file_path) as file:
    for word in file:
        word = word.strip('\n')
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
print(freq_dict)
