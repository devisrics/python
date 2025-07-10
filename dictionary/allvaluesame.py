my_dict={"a":4,"b":4,"c":4}

unique_values=len(set(my_dict.values()))

if unique_values==0:
    print("Empty")
elif unique_values==1:
    print("True")
else:
    print("False")