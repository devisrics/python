my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}

new_list=[]
for elem in my_dict.values():
    new_list.append(sum(elem))

result=max(new_list)
print(result)