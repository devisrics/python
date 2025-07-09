my_list=input("Enter a lis of tvalue:").split()
factor=int(input("Enter a factor:"))


#consider numbers only
#option 1
for i in range(len(my_list)):
   my_list[i]= int(my_list[i])*factor

print(my_list)


#option2 
for i,elem in enumerate(my_list):
   my_list[i]= int(elem) *factor

print(my_list)