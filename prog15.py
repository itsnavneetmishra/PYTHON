#compund interest formula
p=float(input("Enter principal amount"))
r=float(input("Enter rate of interest"))
t=float(input("Enter time"))

ci=p*(1+(r/100))**t
print("Compound interest = ",ci)