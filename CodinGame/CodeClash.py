import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

line=[]
n = int(input())
for i in range(n):
    line[i] = [int(j)] for j in input().split)
sum = (line[0][j] +line[n-1][j] for j in range(n))
for j in range(n-2) :
    sum += line[1+j][0] + line[1+j][n-1] 

print(sum)
