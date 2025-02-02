F=open("old.txt","r")
s=F.read()
L=s.split(" ")
for word in L:
    print(f"{word} : {len(word)}")
F.close()

'''
Output

hello : 5
how : 3
are : 3
you : 3
'''