import random

def first_last (l):
    return [l[0], l[-1]]

aNum = random.randint(1, 9)
a = random.sample(range(1, 10), aNum)
print(a)

print(first_last(a))