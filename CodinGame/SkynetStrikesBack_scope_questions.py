import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def mprint() :
    for i in range(len(m)) :
        row = ""
        for j in range(len(m[i])) :
            row += str(m[i][j])
        print(row,file=sys.stderr)

def link_add(x,y) :
	link_update(x,y,1)
	
def link_delete(x,y) :
	link_update(x,y,0) 
	
def link_update(x,y,value) :
    m[x][y] = value
    m[y][x] = value
	


        
        
def findlink(r,dist_m) :
    res = n
    for gate in gates() :
        if dist_m[r][gate] == 1 :
            res = gate
            break 
    return res
 
v=[]
def gates() :
	res = []
	for node in range(n) :
		if v[node] == 1 :
			res.append(node)
	return res
def gates_init(n) : 
	v=[ 0 for i in range(n)] 
	print(n,v[0],v[1],file=sys.stderr)
	
def gates_add(n) :
	v[n] = 1


	
def findlink2(agent) :
	max = 0
	candidate = (n,n)
	for gate in gates() :
		for midpoint in range(n) :
			if m[agent][midpoint] == 1 and m[midpoint][gate] == 1:
				number_to_gate = linktogate(midpoint)
				if number_to_gate > max :
					candidate = (gate,midpoint)
					max = number_to_gate
	return candidate

def linktogate(node) :
    sum = 0
    for gate in gates() :
        sum += m[node][gate]
    return sum
    
def findanylink() :
	max = 0
	candidate = (n,n)
	for gate in gates() :
		for j in range(n) :
			if m[gate][j] == 1 :
				number_to_gate = linktogate(j)
				if number_to_gate > max :
					candidate = (gate,j)
					max = number_to_gate
	return candidate
        
# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
#print(n,l,e,file=sys.stderr)
gates_init(n)
print(n,file=sys.stderr)


m=[ [0]*n for i in range(n)]

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    link_add(n1,n2)
    
for i in range(e):
    gates_add(int(input()))  # the index of a gateway node

# game loop
while 1:
    agend_node = int(input())  # The index of the node on which the Skynet agent is poagend_nodetioned this turn

    sj = findlink(agend_node,m)
    print("after findlink",sj,n,file=sys.stderr)
    # mprint()
    if sj < n :
        link = (agend_node,sj)
    else :
        link = findlink2(agend_node)
        if  link[0] == n :
            link = findanylink()
        
    print(link[0],link[1])
    link_delete(link[0],link[1])