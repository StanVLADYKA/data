import random

print(random.choice([0,2]))

null = 0
two = 0
for i in range(10000):
    res = random.choice([0, 2])
    if res == 0:
        null += 1
    else:
        two += 1

print(("0",null))
print(("2",two))




