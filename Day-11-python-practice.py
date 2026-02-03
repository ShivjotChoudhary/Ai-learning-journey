#03/03/2026
# use of reshape(1-row,2-column)
import numpy as np
x.reshape(3,3)


# use of np.sqrt(x)
np.sqrt(x)

# changing and printing the values:-
x[1,1] = 16
x

#  use of np.where(x>5)
np.where(x>5)

# use of np.count_nonzero(x)
np.count_nonzero(x)

# use of np.nonzero(x)
np.nonzero(x)

#checking the size : in memory and total size
print("Size in Memory:-",x.itemsize)
print("Actual Size:-",x.size)

# **Questions of date = 30/01/2026**

#1. Write a Python program to print "Hello World"
print("Hello World")

#2. Write a Python program to do arithmetical operations addition and division.
a=10
b=20
print("addition =",a+b)
print("Division =",a/b)

#3. Write a Python program to find the area of a triangle.
a=base = 10
b=height = 20
print("Area of triangle =",1/2*a*b)

#4. Write a Python program to swap two variables. without temp
var1=10
var2=20
print(var1,var2)
var1,var2=var2,var1
print(var1,var2)

#5. Write a Python program to generate a random number.
import random
print(random.randint(0,1000))

#6. Write a Python program to convert kilometers to miles.
a=float(input("Enter distance in km = "))
mile1val = 0.6213712
print("your distance in miles =",a*mile1val)

#7. Write a Python program to convert Celsius to Fahrenheit.
#formula = f = (c*9/5)+32
c = float(input("Enter the temp = "))
f = (c*9/5)+32
d = str(f)
print(d+"f")

#8. Write a Python program to display calendar.
import calendar 
year = int(input("enter the year "))
month =int(input("enter the month "))
print(calendar.month(year,month))


#9. Write a Python program to swap two variables  variable. with temp
a =10
b =20
print(a,b)
temp = a
a=b
b=temp
print(a,b)

#10. Write a Python Program to Check if a Number is Positive, Negative or Zero.
a = int(input("enter the number = "))
if a<0:
  print("Negative")
elif a==0:
  print("Zero")
else:
  print("Positive")


#11. Write a Python Program to Check if a Number is Odd or Even.
a = int(input("enter the number = "))
if a%2==0:
  print("Even")
else:
  print("Odd")

#12. Write a Python Program to Check Leap Year.
a = int(input("enter the number = "))
if (a%4==0 and a%100!=0)or a%400==0:
  print("leap")
else:
  print("no")
