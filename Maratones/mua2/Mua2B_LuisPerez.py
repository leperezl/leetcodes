##Luis Perez 201714355
t= input()
t=int(t)
a, b, c, d =0,0,0,0
tests=[t]
vals=[]
for i in range(t):
    a,b,c,d = input().split(" ")
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    vals=[a,b,c,d]
    tests.append(vals)
    vals=[0,0,0,0]

for i in range(len(tests)):
    
    if (c<d):
        print(-1)
        break
    toSleep=a-b
    total=b
    while toSleep > 0:
        toSleep= toSleep-(c-d)
        total=total+c
    print(total)
        

