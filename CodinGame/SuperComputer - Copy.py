import sys
import time
   
def jstart(j) :
    return j[0]
def jend(job) :
    return job[1]
    
startLookingAt = 0

def remainingRequests() :
    return requests[startLookingAt:]

def startAfter(job) : 
    return remainingRequests().index(job)
    
    
def findBestEndAfter(lastEnd, pos = 0) :
    candidate = None
    for job in remainingRequests()[pos:] : 
        if lastEnd < jstart(job) : 
            candidate = job
            break
    return candidate
    
def findBestEndWithOverlap(simpleStart,simpleEnd) :
    candidate = None    
    for job in remainingRequests() :
        if simpleEnd <= jend(job)  :
            # print ("lastStart="+str(lastStart),"lastEnd="+str(lastEnd),file=sys.stderr)
            break 
        if simpleStart < jstart(job) :
            candidate = job
            break
    return candidate

def testBestEnd(lastStart,lastEnd) :
    print("----------------------------------",file=sys.stderr)
    print("lastStart="+str(lastStart),"lastEnd="+str(lastEnd),file=sys.stderr)
    print("findBestEndAtfter()=",findBestEndAfter(lastEnd),file=sys.stderr)
    overlap = findBestEndWithOverlap(lastStart,lastEnd)
    print("findBestEndWithOverlap()=",findBestEndWithOverlap(lastStart,lastEnd),file=sys.stderr)
    if overlap :
        print("...and best after that=",findBestEndAfter(jend(overlap)),file=sys.stderr)

def findNextJob(startingFrom) :
        simple = findBestEndAfter(startingFrom)
        if simple is None :
            return None
        afterSimple = findBestEndAfter(jend(simple),startAfter(simple))
        
        overlap = findBestEndWithOverlap(jstart(simple),jend(simple))
        if overlap is None :
            return simple
        afterOverlap = findBestEndAfter(jend(overlap),startAfter(overlap))
      
        if jend(afterSimple) <= jend(afterOverlap) :
            return simple
        else :
            return overlap
    
n = int(input())

bestList = []
requests = []

print("requests read",file=sys.stderr)
for i in range(n) : 
    start, duration = [int(j) for j in input().split()]
    end = start + duration - 1
    requests.append((start,end))
print("requests done",file=sys.stderr)
    
print("sort start",file=sys.stderr)
requests.sort(key=jend)
print("sort end",file=sys.stderr)



nextJob = findNextJob(0)
while nextJob :
    bestList.append(nextJob)
    
    newJob = findNextJob(jend(nextJob))
    y = remainingRequests().index(nextJob)
   
    print(startLookingAt,y,file=sys.stderr)
    startLookingAt += y
    
    nextJob = newJob

# print(bestList,file=sys.stderr)    
print(len(bestList))











    
