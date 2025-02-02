import random
D={}
div = random.randint(2,7)
for i in range(15):
    num=random.randint(0,1000)
    rem=num%div
    D[rem]=D.get(rem,0)+1
print(D)

'''
Output :

{2: 8, 0: 3, 1: 4}
'''