my_list = input("Enter a list of values: ").split()
my_list = [int(i) for i in my_list]

#option 1
max_val = my_list[0]
min_val = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > max_val:
        max_val = my_list[i]
    if my_list[i] < min_val:
        min_val = my_list[i]
    else:
        None

print("Maximum:", max_val)
print("Minimum:", min_val)


#option 2
if my_list:
    print(max(my_list),min(my_list))
else:
    None