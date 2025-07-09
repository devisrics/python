my_list = input("Enter a list of values: ").split()
new_list=[]

if(len(my_list)==0):
    print("list is empty")
else:
    for i in range(len(my_list)):
        new_list.append(my_list[i])
 
print(new_list)