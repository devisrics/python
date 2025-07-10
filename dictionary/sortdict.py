my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}

for key,value in my_dict.items():
    my_dict[key]=sorted(value)           #return new sorted list

print(my_dict)





#option2 
my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}

for value in my_dict.values():
    value.sort()

print(my_dict)
