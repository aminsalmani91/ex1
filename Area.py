import math

def Area(a,b,c,d,e):
    if d and e==0:
        def P():
            return (a+b+c)/2
        p=P()
        def trianglearea():
            return math.sqrt(p*(p-a)*(p-b)*(p-c))
        s=trianglearea()
        return s
    elif d==0 and e>0:
        return None
    elif d>0 and e==0:
        return None
    else:
        s1=trianglearea(a,b,e)
        s2=trianglearea(c,d,e)
        return s1+s2

a=int(input("please enter first side of the foursquare -> "))
b=int(input("please enter second side of the foursquare -> "))
c=int(input("please enter third side of the foursquare -> "))
d=int(input("please enter fourth side of the foursquare -> "))
e=int(input("please enter the quadrilateral diameter 'ghotr' -> "))
print(Area(a,b,c,d,e))
