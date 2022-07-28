# check if String contains All letters in Alphabet
# Logic-1
import string
s = input("Enter String: ")
set_s = set(s.lower()) # Set removes all the duplicate values
if ' ' in set_s:
    set_s.remove(" ")
print(set_s == set(string.ascii_lowercase))

# Logic-2
import string
s = input("Enter String:  ")
is_pangram = True
for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False
print(is_pangram)

