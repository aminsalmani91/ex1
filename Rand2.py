import random

x=int(input("please enter the first number = "))
y=int(input("please enter the second number = "))

while True:
  a=random.randrange(x,y)
  if a%2==0:
    print(a)
    break
