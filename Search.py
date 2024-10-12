Z=input("Please enter the word")
C=input("please enter the charcter you want to search")
i=0
count=0
while i<len(Z):
    if Z[i]==C:
        count+=1
    i=i+1
print(" the number of times",C,"Character has appered is count",count) 