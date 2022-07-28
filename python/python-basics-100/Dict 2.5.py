# Convert Dict into List of Lists
# Option-1
product_info = {'description': 'shoe','price': 4.56, 'colours':['gren','blue','red']}
my_list = []
for items in product_info.items():
    my_list.append(list(items))
print(my_list)

# Option-2
new_list =[]
for key,value in product_info.items():
    new_list.append([key,value])
print(new_list)