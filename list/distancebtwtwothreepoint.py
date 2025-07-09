import math
my_list1 = [4,5,1]
my_list2 = [3,2,1]

distance=((my_list1[0]-my_list2[0])**2+
          (my_list1[1]-my_list2[1])**2+
          (my_list1[2]-my_list2[2])**2
          )

result=math.sqrt(distance)
print(result)