n = int(input())
s = 0
for i in range(n) :
    l =  [int(j) for j in input().split()]
    if i in [0,n-1] :
        for j in l :
            s += j
    else :
        s += l[0] + l[n-1]
print(s)
    

