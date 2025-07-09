my_list=input("Enter a list of values:").split()
new_list=[int(i) for i in my_list]

for i in range(len(my_list)):
    if (new_list[i]>3):
        print(new_list[i])

