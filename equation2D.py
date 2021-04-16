import math
#y=ax**2+bx+c

def equation2D(a,b,c):
  def Deltaformula():
    return b**2-4*a*c
  delta=Deltaformula()
  if delta<0
  return none
elif delta==0
x1=-b/(2*a)
return x1
else:
  x1=(-b+math.sqrt(delta))/(2*a)
  x2=(-b-math.sqrt(delta))/(2*a)
  return (x1,x2)

a=int(input("please enter the first constant of equation -> a = "))
b=int(input("please enter the second constant of equation -> b = "))
c=int(input("please enter the third constant of equation -> c = "))
print(equation2D(a,b,c))
