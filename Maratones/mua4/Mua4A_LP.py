t = int(input("number of tests: "))
ins= []
tar=[]
res=[]
if t>0 and t<1000:
    for i in range(t):
        a, b=input("vals: ").split(" ")
        ins.append(int(a))
        tar.append(int(b))
        a=0
        b=0
for i in range(t):
    movsF=0
    for j in range(t):
        op=ins[i]
        movs=0
        if op == tar[i]:
            res.append(movs)
            break
        if op > tar[i] and op%8==0:
            op=ins[i]/8
            movs+=1
        if op > tar[i] and op%4==0:
            op=ins[i]/4
            movs+=1
        if op > tar[i] and op%2==0:
            op=ins[i]/2
            movs+=1
        if op*2 != tar[i] and op%8!=0 and op%4!=0 and op%2!=0:
            movs=-1
    print(movsF)
print(op)