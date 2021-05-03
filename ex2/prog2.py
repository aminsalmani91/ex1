import random

a=int(input("enter a number -> a = "))
b=int(input("enter a number -> b = "))

if a%2==0:
    a+=1

d=[]
f=(b-a)/2
while len(d)<=f-1:
    i=random.randrange(a,b)
    if i%2==0 and i not in d:
        d.append(i)
        
print(d)


    
