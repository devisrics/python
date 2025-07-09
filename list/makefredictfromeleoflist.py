my_list=input("Enter a list of values:").split()

new_dict={}
for elem in my_list:
    if elem not in new_dict:
        new_dict[elem]=1
    else:
        new_dict[elem]+=1

print(new_dict)