import sys
import math

def m_print() :
    for node in neighbor
         print(neighbor[node],file=sys.stderr)
		
def m_clear(link) :
	m_assign(link,0)
	
def m_set(link) :
     (x,y) = link
	 neighbor[x].add(y)
	 neighbor[y].add(x)
	 
def m_assign(link,value) :
	m[link[0]][link[1]] = value
	m[link[1]][link[0]] = value
	 
def link_print(link):
    print(link[0],link[1])

        
def findlink(r) :
    res = n
    for node in range(n) :
        if v[node] * m[r][node] == 1 :
            res = node
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
    
def findlinks2(node) :
    candidates = []
    for gate in range(n) :
        if v[gate] == 1 :
            for midpoint in range(n) :
                if m[node][midpoint] == 1 and m[midpoint][gate] == 1:
                    candidates.append((gate,midpoint))
    return candidates
    
def busiest(possible_links) : 
    max = 0
    candidate = (n,n)
    
    print(possible_links,file=sys.stderr)
    for link in possible_links :
        number_to_gate = linktogate(link[1])
        if number_to_gate > max :
            candidate = link
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


neighbor=[ set() n for i in range(n)]
for i in range(l):
    m_set(int(j) for j in input().split())

v = [ 0 for i in range(n)]
for node in range(e):
    v[int(input())] = 1 

# game loop
while 1:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    if 1 == 1 and si == 2 :
        link = (17,18)
    else :
        sj = findlink(si)
        print("after findlink",sj,n,file=sys.stderr)
        if sj < n :
            link = (si,sj)
        else :
            possible_links = findlinks2(si)
            if len(possible_links) > 0 :
                link = busiest(possible_links)
            else :
                link = findanylink()
        
    link_print(link)
    m_clear(link)