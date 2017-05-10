import sys
import math

class netClass(object) :
    
    def __init__(self,numberOfNodes) :
        self.numberOfNodes = numberOfNodes
        self.neighbors=[ set() for i in range(self.numberOfNodes)]
        
    def addLink(self,x,y) :
        self.neighbors[x].add(y)
        self.neighbors[y].add(x)
        
    def deleteLink(self,x,y) :
        self.neighbors[x].remove(y)
        self.neighbors[y].remove(x)
    def hasPath(self, x,y) :
        return x in self.neighbors[y]
    def countlinksbetween(self,node,groupofnodes) :
        sum = 0
        for n in groupofnodes :
            if node in self.neighbors[n] :
                sum += 1
        return sum
    def findALinkTo(self,node,nodeGroup) :
        possible = self.neighbors[node] & set(nodeGroup)
        if possible :
            return (node, possible.pop())
            
    def nodesNextTo(self,nodeGroup) :
        res = set()
        for node in nodeGroup :
            res.update(self.neighbors[node])
            # print("nodesNextTo",self.neighbors[node],res,file=sys.stderr)
        return res
   
        
        
    def findDangerFor(self, nodeToCheck, nodeGroup) :
        nodesWithMultipleGates= set()
        for node in range(self.numberOfNodes) :
            if len(self.neighbors[node] & nodeGroup )> 1 :
                nodesWithMultipleGates.add(node)
        if nodesWithMultipleGates == {} :
            return
        nodesNextToGates = self.nodesNextTo(nodeGroup)
        nodesToExclude = nodeGroup | nodesWithMultipleGates 
        for nodeToTest in nodesWithMultipleGates :
            newNodes = {nodeToTest}
            while newNodes :
                nextWave = self.nodesNextTo(newNodes)
                if nodeToCheck in nextWave :
                    return self.findALinkTo(nodeToTest,nodeGroup)
                newNodes = (nextWave - nodesToExclude) & nodesNextToGates
                nodesToExclude |= nextWave
            
class gatesClass(object) :
    def __init__(self,n) :
        self.v=set()
        
    def list(self) :
        return self.v
        
    def add(self,n) :
        self.v.add(n) 
    
    def __str__(self) :
        return __class__.__name__ + ": " + str(self.v)

def findlink2(node) :
    max = 1
    candidate = None
    for gate in gates.list() :
        for midpoint in range(n) :
            if  skyNet.hasPath(node,midpoint) and skyNet.hasPath(midpoint,gate) : 
                number_to_gate = skyNet.countlinksbetween(midpoint,gates.list())
                if number_to_gate > max :
                    candidate = (gate,midpoint)
                    max = number_to_gate
    return candidate 

   
def findALinkToGateWithMostLinks() :
    max = 0
    candidate = None
    for gate in gates.list() :
        for j in range(n) :
            if skyNet.hasPath(gate,j) :
                number_to_gate = skyNet.countlinksbetween(j,gates.list())
                if number_to_gate > max :
                    candidate = (gate,j)
                    max = number_to_gate
    return candidate
    
def findANodeWithMostLinksToGates() :
    max = 0
    candidate = None
    for j in range(n) :
        for gate in gates.list() :
             if skyNet.hasPath(gate,j) :
                number_to_gate = skyNet.countlinksbetween(j,gates.list())
                if number_to_gate > max :
                    candidate = (gate,j)
                    max = number_to_gate
    return candidate
        
# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

skyNet = netClass(n)
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    skyNet.addLink(n1,n2)

gates = gatesClass(n)    
for i in range(e):
    gates.add(int(input())) 

# game loop
while 1:
    agend_node = int(input()) 

    link = skyNet.findALinkTo(agend_node,gates.list())
    if link is None :
        link = skyNet.findDangerFor(agend_node,gates.list())
        if link is None :
            link = findlink2(agend_node)
            if  link is None : 
                link = findANodeWithMostLinksToGates()
            
    print(link[0],link[1])
    skyNet.deleteLink(link[0],link[1])