my_list=[4,[1,2,3],[7,5,6],[8,9,0]]
nested_list=[]

for elem in my_list:
    if isinstance(elem,list):
        for nested_elem in elem:
            nested_list.append(nested_elem)

    else:
        nested_list.append(elem)

print(nested_list)