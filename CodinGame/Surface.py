import sys
import math

debug = False

def isWater(x,y) : 
    if x < 0 or y < 0 or x >= l or y >= h :
        res = False
    else :
        res =  map[y][x]=="O"
    # if debug : print("isWater:",x,y,res,file=sys.stderr)
    return res
    
def waterNear(square) :
    x = square[0]
    y = square[1]
    res = set()
    if isWater(x+1,y) :
        res.add((x+1,y))
    if isWater(x-1,y) :
        res.add((x-1,y))  
    if isWater(x,y+1) :
        res.add((x,y+1) )  
    if isWater(x,y-1) :
        res.add((x,y-1))
    # if debug : print("waterNear:",x,y,res,file=sys.stderr)
    return res


l = int(input())
h = int(input())

map = [input() for i in range(h)]
resultsMap = [ [None] * l for i in range(h)]

numberOfTests = int(input())
    
for testNumber in range(numberOfTests):
    x, y = [int(j) for j in input().split()]
  
    if not isWater(x,y) : 
        print(0)
        continue
        
    if resultsMap[y][x] is not None :
        print(resultsMap[y][x])
        continue
    
    checkedSquares = set()
    newSquaresToTest = {(x,y)}
    while newSquaresToTest :
        to_test = newSquaresToTest.pop()
        checkedSquares.add(to_test)
        possibleNewSquares = waterNear(to_test)
        newSquaresToTest |= possibleNewSquares - checkedSquares
        
        if debug :
            print("--------------",file=sys.stderr)
            print("checkedSquares=  ",checkedSquares,file=sys.stderr)
            print("newSquaresToTest=",newSquaresToTest,file=sys.stderr)
    if debug :
        print("",file=sys.stderr)
        print("*********************",file=sys.stderr)
    size = len(checkedSquares)
    print( size )
    while checkedSquares :
        (x,y) = checkedSquares.pop() 
        resultsMap[y][x] = size
    if debug :
        print("*********************",file=sys.stderr)
        print("",file=sys.stderr)