29/01/2026

#Q63) wap to find the sum of first n numbers.(using while)
n = 2
b = 0
sum = 0
while b<=n:
  sum +=b
  b+=1
print(sum)

#Q64) wap to find the factorial of first n numbers(using for)
n = 5
b=1
for a in range(1,n+1):
  b*=a
print(b)

#Q65)Functions:-
def cal_sum(a,b):
  return a+b
cal_sum("shiv","jot")

#Q66) Factorial of (n):-(using function)
def func_tion(n):
  b=1
  for a in range(1,n+1):
    b*=a
  print(b)
func_tion(4)
/
#Q67) wap to convert USD to INR.(using function)
#1 USD. = 91.91
def con_vert(n):
  print(n,"USD =",n*91.91,"INR")

con_vert(int(input("Enter Currency: ")))
