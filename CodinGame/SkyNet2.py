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
        
def make_m2():
    return

    for row in range(n) :
        for col in range(n) :
            if row==col or col > row :
                continue 
            # print("m2 loop:",row,col,file=sys.stderr)
            if m[col][row] == 1 :
                m2[col][row] = 1 
                m2[row][col] = 1
                continue
            # fill in lower triangle
            for step2 in range(col) :
                if step2 == row :
                    continue
                for col2 in range(col-1) :
                    if m[step2][col2] == 1 :
                        m2[row][col] = 1
                        m2[col][row] = 1
    for row in range(n) :
        pass # print(m2[row],file=sys.stderr)
        
def findlink(r,dist_m) :
    res = n
    for i in range(n) :
        if v[i] * dist_m[r][i] == 1 :
            res = i
            break 
    return res
    
def findlink2(agent) :
    max = 0 
    candidate = (n,n)
    for gate in range(n) :
        if v[gate] == 1 :
            for midpoint in range(n) :
                if m[agent][midpoint] == 1 and m[midpoint][gate] == 1:
                    number_to_gate = linktogate(midpoint)
                    if number_to_gate > max :
                        candidate = (gate,midpoint)
                        max = number_to_gate
    return candidate

def linktogate(node) :
    sum = 0
    for i in range(n) :
        sum += v[i] * m[node][i]
    return sum
    
def findanylink() :
    max = 0
    candidate = (n,n)
    for i in range(n) :
        if v[i]==1 :
            for j in range(n) :
                if m[i][j] == 1 :
                    number_to_gate = linktogate(j)
                    if number_to_gate > max :
                        candidate = (i,j)
                        max = number_to_gate
    return candidate
        
# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
#print(n,l,e,file=sys.stderr)
v=[]
for i in range(n) :
    v.append(0)
m=[]
for i in range(n) :
    m.append([])
    m[i].extend(v)
# mprint()



for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    m[n1][n2] = 1
    m[n2][n1] = 1
    
# mprint()

m2 = [[0] * n for i in range(n) ]
make_m2()

for i in range(e):
    ei = int(input())  # the index of a gateway node
    v[ei]=1

# game loop
while 1:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    sj = findlink(si,m)
    print("after findlink",sj,n,file=sys.stderr)
    # mprint()
    if sj < n :
        link = (si,sj)
    else :
        link = findlink2(si)
        if  link[0] == n :
            link = findanylink()
        
    print(link[0],link[1])
    m[link[0]][link[1]] = 0
    m[link[1]][link[0]] = 0
    make_m2()