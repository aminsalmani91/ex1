
a=int(input("enter a number -> a = "))
b=int(input("enter a number -> b = "))

c=[]

for i in range(a+1,b):
    if i%2==0:
        c.append(i)
print(c)

