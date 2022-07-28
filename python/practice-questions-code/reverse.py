# Write a Python script to reverse the order of the words in a sentence.
# An input of "This is a Python challenge" should output "challenge Python a is This"

s = "This is a Python challenge"
reversed_string = ''.join(reversed(s))
print(reversed_string)
new_list = reversed_string.split(' ')
for i in new_list:
    print(i[::-1],end = ' ')