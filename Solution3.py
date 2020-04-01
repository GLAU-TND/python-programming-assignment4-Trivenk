l=list(map(str,input().split()))
s=input()
d=len(s)
k=[]
for i in l:
    if i[0:d]==s:
        k.append(i)
print(k)
        
