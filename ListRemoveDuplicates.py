import random

def remove_duplicates(l):
    return list(set(l))

aNum = int(input("Enter a size: "))
a = []
for i in range(aNum):
    a.append(int(input()))

print(remove_duplicates(a))