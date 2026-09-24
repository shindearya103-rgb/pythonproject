a=int(input("enter first no"))
b=int(input("enter second no"))
c=int(input("enter third no"))

if a>=b and a>=c:
    print("greatest=",a)
elif b>=a and b>=c:
    print("greatest=",b)
else:
    print("greatest=",c)
