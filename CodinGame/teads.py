import sys
import math
import copy

def isDone(G): 
    for i in range(max_node+1) :
        if len(G[i]) == count_of_nodes :
            # print("IsDone Graph[%i] = %s, len=%i" % (i,G[i],len(G[i])), file = sys.stderr)
            return True
    return False
    
def printGraph(G):
    for i in range(max_node+1) :
        if G[i] : 
            print("Graph[%i] = %s" % (i,G[i]), file=sys.stderr)


n = int(input())  # the number of adjacency relations

Walk = [ set() for  i in range(n+1) ]

list_of_nodes = set()
max_node = 0 
e = []
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    x,y = [int(j) for j in input().split()]
    # print (e,file=sys.stderr)
    max_node = max(max_node, x,y)
    list_of_nodes.add(x)
    list_of_nodes.add(y)
    e.append((x,y))
    
count_of_nodes = len(list_of_nodes)

print( "edges = %i    max_node = %i" % (i,max_node),file=sys.stderr,  flush=True)
Graph = [ set() for  i in range(max_node+1) ]
# print(Graph,file=sys.stderr)
# print(e,file=sys.stderr)

for i in range(n) :
    Graph[e[i][0]].add(e[i][1])
    Graph[e[i][1]].add(e[i][0])

W = []
Diff = []
W = copy.deepcopy(Graph)
Diff =  copy.deepcopy(Graph)
# printGraph(W)   
steps = 1   

keep_checking = True
while keep_checking: 
    for i in range(max_node + 1) :
        if Diff[i] :
            new_row = W[i] 
            for j in Diff[i] :
                new_row = new_row.union(Graph[j])
            Diff[i] = new_row - W[i]
            if len(new_row) == count_of_nodes :
                keep_checking = False
                break 
            W[i] = new_row
    steps += 1
    # print("\nStep %i" % steps,file=sys.stderr)
    # printGraph(W)
    
print (steps)
