my_list=input("Enter a list of values:").split()
remove_ele=input("Enter a value to remove:")

if(len(my_list)==0):
    print("List is empty")
elif my_list.count(remove_ele)==0:
    print("Not Found")
else:
    for i in range(my_list.count(remove_ele)):
        my_list.remove(remove_ele)

print(my_list)

