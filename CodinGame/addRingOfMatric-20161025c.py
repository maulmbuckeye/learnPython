
fp = open("matrixTest.txt","r")

n = int(fp.readline())

s = 0
for i in range(n) :
    l =  [int(j) for j in fp.readline().split()]
    if i in [0,n-1] :
        for j in l :
            s += j
    else :
        s += l[0] + l[n-1]

print(s)
    

