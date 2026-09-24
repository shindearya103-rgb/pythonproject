a=float(input("enter first number"))
b=float(input("enter seconf number"))
op=input("enter operator (=,-,*,/)")

if op =="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print("invalidoperator")
