# Check if a file exists or not
import os.path
my_file = 'basic_file_copy.txt'

if os.path.isfile(my_file):
    print(f'The given file {my_file} exists')
else:
    print(f'The given file {my_file} does"not exists')
