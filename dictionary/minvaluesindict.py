import math
my_dict={"a":4,"b":3,"c":6}

if len((my_dict))==0:
    print("Dict is Empty")

else:
    new_dict=set(my_dict.values())
    print(min(new_dict))