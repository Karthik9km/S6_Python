import random
D={}
for i in range (10):
    num = random.randint(0,100)
    D[num] = num**2
print(D)

"""
Output : 

{57: 3249, 20: 400, 55: 3025, 27: 729, 28: 784, 52: 2704, 91: 8281, 90: 8100, 22: 484, 53: 2809}
"""