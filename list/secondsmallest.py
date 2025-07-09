my_list=input("Enter a list of values:").split()
new_list=[int(i) for i in my_list]

res=sorted(set(new_list))
if len(res) >= 2:
    print("Second smallest is:", res[1])
else:
    print("Second smallest does not exist.")

