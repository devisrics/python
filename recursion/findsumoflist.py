num=[1,2,3,4,5]

def sum_list(s):
    if len(s)==0:
        return 0
    else:
        return s[0] + sum_list(s[1:])
    
print(sum_list(num))