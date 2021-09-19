B="bus"
R="ring"
S="star"
UKN="unkown"

n = []
e = []
nodes, edges = map(int, input().split(" "))
for i in range(edges):
    a,b= map(int,input().split(" "))
print(str(n+e) + " this is n: {n} and e: {e}")