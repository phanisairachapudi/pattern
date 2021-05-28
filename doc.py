pyramid pattern


n = int(input("enter the value: ", ))
for row in range(1,n+1):
    for spaces in range(n,row,-1):
        print(" ", end="")
    for c in range(1, row+1):
        a = chr(c+64)
        print(a,end="")
    for c in range(c-1,0,-1):
        a = chr(c+64)
        print(a,end="")
    print()
    
    
    
    
remove repeated letters from the string


s = input("enter the string: ", )
non_repeated =""

for i in s:
    if i not in non_repeated:
        non_repeated = non_repeated + i
print(non_repeated)
