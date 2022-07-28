# Reverse Words in a String
s = 'Python IS awesome'
new_s = ''
words_list = s.split(' ')
for word in words_list:
    reversed_word = word[::-1] # ''.join(reversed(word))
    swapped_case = reversed_word.swapcase()
    new_s += swapped_case + ' '
    #print(reversed_word)
    #print(swapped_case)
new_s = new_s.rstrip()
print(new_s)