import random
stud = {}
stud[48]="Karthik Manoj"
stud[49]="Lakshmi R Menon"
stud[50]="Lakshmi Sreekumar"
stud[51]="Nandana Biju"
stud[52]="Nandana K"
L=list(stud.items())
print(f"Sorted Student Details based on roll no : \n {L} \n")
L.sort(key = lambda v : [v])
print(f"Sorted Student Details based on name : \n {L} \n")
stud1={}
for roll in stud:
    stud1[roll] = [stud[roll],random.randint(0,100)]
max = -1
for roll in stud1:
    if stud1[roll][1]>max:
        highRoll = roll 
        max = stud1[roll][1]
print(f"Details of student with highest mark : {highRoll} {stud1[highRoll][0]} {stud1[highRoll][1]} \n")
delRoll = int(input("Enter a roll no to delete : "))
stud.pop(delRoll)
stud1.pop(delRoll)
print(f"\n Details of passed students : \n")
for roll in stud1:
    if stud1[roll][1]>50:
        print(f"{roll} {stud1[roll][0]} {stud1[roll][1]}")

'''
Output : 

Sorted Student Details based on roll no : 
 [(48, 'Karthik Manoj'), (49, 'Lakshmi R Menon'), (50, 'Lakshmi Sreekumar'), (51, 'Nandana Biju'), (52, 'Nandana K')] 

Sorted Student Details based on name : 
 [(48, 'Karthik Manoj'), (49, 'Lakshmi R Menon'), (50, 'Lakshmi Sreekumar'), (51, 'Nandana Biju'), (52, 'Nandana K')] 

Details of student with highest mark : 51 Nandana Biju 82 

Enter a roll no to delete : 51

 Details of passed students : 

48 Karthik Manoj 64
49 Lakshmi R Menon 75
'''
