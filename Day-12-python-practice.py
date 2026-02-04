# **04/02/2026**

# 13. Write a Python Program to Check Prime Number. method 2
a = int(input("Enter the number: "))
if a<=1:
  print("not prime")
else:
  for aa in range(2,a):
    if a%aa==0:
      print("not prime")
      break
  else:
    print("prime")


#14. Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
for a in range(1,11):
  if a>1:
    is_true = True
    for b in range(2,a):
      if a%b==0:
        is_true = False
        break
  if is_true:
    print(a)


#15. Write a Python Program to Find the Factorial of a Number.
num = 5 
b=1
for a in range(1,num+1):
  b*=a
print(b)

#16. Write a Python Program to Display the multiplication Table.
a=0
b=int(input("Enter the number =  "))
while a<=10:
  print(a*b)
  a+=1



#17. Write a Python Program to Find Armstrong Number in an Interval.
start = int(input("Enter start of interval: "))
end = int(input("Enter end of interval: "))

for num in range(start, end + 1):
    order = len(str(num))   # number of digits
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num, "is an Armstrong number")
