#Write a program to Calculate Sum of 5 Subjects and Find Percentage.
n=int(input("Enter number of subjects "))
sum=0
for i in range(n):
  a=int(input("enter marks"))
  sum+=a
print("sum of 5 subject marks = ",sum)

avg=sum/n

print("average =",avg)
  


