import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



r = int(input())
l =  int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
lookingFor = 0

lineToProcess= [r]
for i in range(l-1) :
    print(lineToProcess, file=sys.stderr)
    nextLine = []
    count = 0 
    for digit in lineToProcess :
        if count == 0 :
            lookingFor = digit
            count = 1
        elif digit == lookingFor :
            count += 1
        else :
            nextLine.append(count)
            nextLine.append(lookingFor)
            lookingFor = digit
            count = 1
    nextLine.append(count)
    nextLine.append(lookingFor)
    lineToProcess = nextLine
print(" ".join(map(str,lineToProcess)))

    
        

