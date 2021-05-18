def swap(x,y):
    replace=x
    x=y
    y=replace
    return x,y

a=int(input("please enter the first number = "))
b=int(input("please enter the second number = "))

print(swap(a,b))
