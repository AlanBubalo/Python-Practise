import random

aNum = random.randint(1, 9)
bNum = random.randint(1, 9)
a = random.sample(range(1, 10), aNum)
b = random.sample(range(1, 10), bNum)
print(str(a) + "\n" + str(b))

print([i for i in a if i in b])