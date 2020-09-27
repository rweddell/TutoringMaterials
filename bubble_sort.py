import random

numlist = random.sample(range(1, 30),10)

print(numlist)

for i in range(0, len(numlist)-1):
    for j in range(i,len(numlist)):
        if numlist[i] > numlist[j]:
            temp = numlist[j]
            numlist[j] = numlist[i]
            numlist[i] = temp

print(numlist)