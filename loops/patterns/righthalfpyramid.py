num=int(input("Enter a number:"))       #combination of downwardleftpyramid and leftpyramid

for i in range(num):
    for j in range(i+1,num):            #for spaces ->downwardleftpyramid (decreasing downward spaces )
        print(" ",end="")
    for j in range(i+1):                #for stars  ->leftpyramid         (increasing upward stars)
        print("*",end="")
    
    print()