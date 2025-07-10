my_list=[["a", 1], ["b", 2], ["c", 3], ["d", 4]]
new_dict={}

for elem in my_list:
    key=elem[0]
    value=elem[1]
    new_dict[key]=value
    
print(new_dict)