B="bus"
R="ring"
S="star"
UKN="unkown"

adj=[]
nodes, edges = map(int, input().split(" "))

for i in range(nodes+1):
    adj.append([])
for i in range(edges):
    a,b= map(int,input().split(" "))
    adj[a].append(b)
    adj[b].append(a)
print(adj)

