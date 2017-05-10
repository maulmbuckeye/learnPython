n=int(input())
s="123456789"
for i in range(n):print("+"*i+s[:n-i])
for i in range(n):print(s[:n-i].rjust(n,"+"))
