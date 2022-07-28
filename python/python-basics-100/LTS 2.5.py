# Make a frequency dictionary from the elements of the List
#l1 = ['a','a','b','c','a','b']
l2 = [1,2,3,4,3,2,1,2]
l3 = ['a','a','A',"B"]
freq_dict = {}
for elem in l3:
    if elem not in freq_dict:
        freq_dict[elem] = 1
    else:
        freq_dict[elem] += 1
print(freq_dict)