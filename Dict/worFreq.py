s = input("Enter a string : ")
s=s.replace(",","")
s=s.replace(".","")
L=s.split(" ")
D={}
for word in L:
    D[word]=D.get(word,0)+1
print(D)

'''
Output:

Enter a string : The dog ran and ran, its paws pounding the ground. It ran faster, eager to chase the ball. The ball bounced, and the dog ran again, its eyes locked on the prize. It ran with joy, never stopping.
{'The': 2, 'dog': 2, 'ran': 5, 'and': 2, 'its': 2, 'paws': 1, 'pounding': 1, 'the': 4, 'ground': 1, 'It': 2, 'faster': 1, 'eager': 1, 'to': 1, 'chase': 1, 'ball': 2, 'bounced': 1, 'again': 1, 'eyes': 1, 'locked': 1, 'on': 1, 'prize': 1, 'with': 1, 'joy': 1, 'never': 1, 'stopping': 1}
'''