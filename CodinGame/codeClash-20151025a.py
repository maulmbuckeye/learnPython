n=int(input())
s="123456789"
for i in range(n) :
   pass #  s+= str(i+1)
for i in range(n) : 
    print("+" * i + s[0:n-i])
