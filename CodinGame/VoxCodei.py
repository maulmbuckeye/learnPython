import sys
import math

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)
DIRECTIONS = [UP,DOWN,LEFT,RIGHT]

class location_class(object) :
    def place_bomb(self) :
        print(str(self.col) + " " + str(self.row))
    def set_by_tuple(self,loc) : 
        if loc is None :
            self.is_good = False
            return 
        self.row = loc[0]
        self.col = loc[1]
        self.is_good = True
    def __init__(self,r=None,c=None) :
        if r is None or c is None :
            self.is_good = False
        else :
            self.set_by_tuple((r,c))
    def get_tuple(self) :
        if self.is_good :
            return (self.row,self.col)
        else :
            return None
    def move(self,direction) : 
        return location_class(self.row + direction[0], self.col + direction[1])
    def __bool__(self) :
        return self.is_good

class map_class() :
    def value(self,loc) :
        return map[loc.row][loc.col]
    def set_value(self,loc,value) : 
        map[loc.row][loc.col] = value
    def on_map(self,loc) :
        return 0 <= loc.col < width and 0 <= loc.row < height 
    def debug_print(self):
        for row in range(height) :
            map_row = "".join(str(symbol) for symbol in map[row])
            opportunity_row = "".join(str(symbol) for symbol in opportunityMap[row])
            print(str(row).rjust(2)+":",map_row,opportunity_row,file=sys.stderr)   


            
def blastAreaOneDirection(loc,direction) : 
    blastOneDirection = []
    test_loc = loc
    for i in range(3) :
        test_loc = test_loc.move(direction)
        if m.on_map(test_loc) :
            if m.value(test_loc) == "#" :
                break 
            blastOneDirection.append((test_loc))
    return blastOneDirection

def blastAreaAllDirections(loc) :
    blastArea = []
    for direction in DIRECTIONS :
        blastArea.extend(blastAreaOneDirection(loc,direction))
    # print("("+str(row)+","+str(col)+"): ",blast,file=sys.stderr)
    return blastArea
    
def countOpportunitiesInBlastArea(loc) :
    if m.value(loc) in "#@X" :
        return 0
    count = 0
    for test_loc in blastAreaAllDirections(loc) :
        if m.value(test_loc) == "@" :
            count += 1
    return count
    
    
def updateMapForFutureBlast(bomb_loc) :
    for blastLoc in blastAreaAllDirections(bomb_loc) :
        if m.value(blastLoc) == "@" :
           m.set_value(blastLoc,"3")           

    
def maxImpactThatIsReady() :
    maxImpact = -1
    maxLocIsNotReady = False
    for loc in locList :
        value = opportunityMap[loc.row][loc.col]
        # print(row,col,value,maxImpact,file=sys.stderr)
        if value > maxImpact or (value == maxImpact and maxLocIsNotReady) :
            maxImpact = value
            maxLoc = loc
            maxLocIsNotReady = (m.value(maxLoc) != ".")
    if maxLocIsNotReady :
        return None
    return maxLoc
                     
       
def updateNodesInBlastMap() :
    for loc in locList :
        # print("updateNodesInBlastMap():loc=",loc,file=sys.stderr)
        opportunityMap[loc.row][loc.col] = countOpportunitiesInBlastArea(loc)

    
def countDownToExplosion() :
    for loc in locList :
        value = m.value(loc)
        if value in "123" :
            if value == "1" :
                new_value = "."
            elif value == "2" :
                new_value = "1"
            else :
                new_value = "2"
            m.set_value(loc,new_value)
                
def get_turn_info() : 
    rounds_left, bombs_left = [int(i) for i in input().split()]
    print(rounds_left,bombs_left,file=sys.stderr)
    return rounds_left, bombs_left
    
m = map_class()  
map = []
opportunityMap = []
locList = []
width, height = [int(i) for i in input().split()]
for row in range(height):
    map_row = list(input())  
    map.append(map_row)
    opportunityMap.append([ 1 for col in range(width)])
    locList.extend( [location_class(row, col) for col in range(width)])

loc_for_bomb = location_class()
while 1:
    rounds_left, bombs_left = get_turn_info()

    updateNodesInBlastMap()
    m.debug_print()
    countDownToExplosion()

    loc_for_bomb = maxImpactThatIsReady()
    if bombs_left > 0 and loc_for_bomb :
        updateMapForFutureBlast(loc_for_bomb)
        loc_for_bomb.place_bomb()
    else :
        print("WAIT")
