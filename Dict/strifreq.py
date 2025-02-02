s = input("Enter a string : ")
D={}
for c in s:
    D[c] = D.get(c,0) + 1
print(D)
"""
Output : 

Enter a string : Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
{'L': 1, 'o': 29, 'r': 22, 'e': 37, 'm': 17, ' ': 68, 'i': 42, 'p': 11, 's': 18, 'u': 28, 'd': 18, 'l': 21, 't': 32, 'a': 29, ',': 4, 'c': 16, 'n': 24, 'g': 3, 'b': 3, 'q': 5, '.': 4, 'U': 1, 'v': 3, 'x': 3, 'D': 1, 'h': 1, 'f': 3, 'E': 1}
"""