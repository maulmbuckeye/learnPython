fp = open("addRingOfMatric-20161025d.py")

sum = 0 
for line in fp :
    sum += len(line.strip())
print(sum)
