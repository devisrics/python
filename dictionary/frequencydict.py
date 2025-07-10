my_dict = {
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 }

new_dict={}

for elem in my_dict.values():
    if elem in new_dict:
        new_dict[elem] +=1
    else:
        new_dict[elem]=1

print(new_dict)