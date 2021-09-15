B="bus"
R="ring"
S="star"
UKN="unkown"

pairs = []
nodes, edges = map(int, input().split(" "))
for i in range(nodes):
    pairs.append(map(int, input().split(" ")))
print(pairs)