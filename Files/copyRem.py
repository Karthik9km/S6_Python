F=open("old.txt","r")
F1=open("new.txt","w")
L=F.readlines()
Lines = [line for line in L if line != "\n"]
F1.writelines(Lines)
F.close()
F1.close()