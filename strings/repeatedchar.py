value=input("Enter a String:")

repeated_count=0
repeated_words=[]

for char in value:
    if(value.count(char)>1) and (char not in repeated_words):
        repeated_count +=1
        repeated_words.append(char)

print(repeated_count)


if(len(repeated_words)>0):
    for c in repeated_words:
        print(c, end=" ")
    
else:
    print(None)