a=int(input("Enter first side : "))
b=int(input("Enter second side : "))
c=int(input("Enter third side : "))


s=(a+b+c)/2

s1=(s*((s-a)*(s-b)*(s-c)))**(1/2)
print(s1)