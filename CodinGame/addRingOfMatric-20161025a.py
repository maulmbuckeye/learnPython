
fp = open("matrixTest.txt","r")

n = int(fp.readline())

m=[]
sum = 0
for i in range(n) :
    listOfNumbers =  [int(j) for j in fp.readline().split()]
    print (listOfNumbers)
    m.append([j] for j in listOfNumbers)
    if i==0 or i==n-1 :
        for j in listOfNumbers :
            sum += j
    else :
        sum += listOfNumbers[0] + listOfNumbers[n-1]

print(m)
print(sum)
    

