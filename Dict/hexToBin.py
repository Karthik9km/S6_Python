D={'1':"0001",'2':"0010",'3':"0011",'4':"0100",'5':"0101",'6':"0110",'7':"0111",'8':"1000",'9':"1001",'A':"1010",'B':"1011",'C':"1100",'D':"1101",'E':"1110",'F':"1111"}
hex = input ("Enter a Hexadesimal number :")
bin = ""
for h in hex:
    bin = bin + D[h]
print(f"Binary Equivalent of Hex is : {bin}")

'''
Output

Enter a Hexadesimal number :F78
Binary Equivalent of Hex is : 111101111000
'''