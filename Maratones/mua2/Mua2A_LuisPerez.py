n= int(input())
m=input().split(" ")
if(len(m)==n):
    for i in range(len(m)):
        m[i]= int(m[i])
max=1
local=1
for i in range(len(m)-1):
    prev=m[i]
    if  prev <= m[i+1]:
        local=local+1
    if local>max:
        max=local
    if prev > m[i+1]:
        local=1
print(max)
    
