print("hello  my name is shivjot choudhary")

# Date = 14/1/2026 Questions:-

# Q1 SimpleInterest
p= float(input("Enter. principal amount:"))
r =float(input("Enter rate:"))
t=float(input("Enter time: "))

si = (p*r*t)/100
print("Simple Interest is:",si)

# Q2 CompoundInterest
p = float(input("Enter principal amount:"))
r=float(input("Enter rate:"))
t= float(input("Enter time: "))

ci = p*(1+r/100)**t
print("Compound Interest:", ci)



# Q 3) Area of Circle
r=float(input("Enter  radius: "))

area = 3.14*r*r
print("Area of circle:", area)



#Q4 Area ofTriangle
b=float(input("Enter base: "))
h=float(input("Enter height: "))

area = 0.5*b*h
print("Area :", area)



#Q5 Area of Rectangle
l=float(input("length:"))
w=float(input("width"))

area = l*w
print("Area:", area)


#Q6 Distance calculation
speed =float(input("speed: "))
time=float(input("Enter time: "))

distance=speed * time
print("Distance:", distance)





#Q7 Speedcalculation
d=float(input("distance: "))
t=float(input("Enter time: "))

speed = d/t
print("Speed:", speed)



# Q8--BMI calculation
weight=float(input("weight in kg:"))
height=float(input("height in meters:"))

bmi=weight/(height * height)
print("BMI:", bmi)



# Q9-Celsius to  Fahrenheit))
c=float(input("Enter temperature in celsius:"))
f=(c * 9/5) +32
print("Temperature:", f)



# Q10 Perimeter of Rectangle:----
l=float(input("Enterlength:"))
w=float(input("Enter width:"))

perimeter = 2 * (l + w)
print("Perimeter:", perimeter)

# Q11)write a program to input two int number a and b , print true if a is greater than or eqaul to b . if not print false.
a=int(input("1st number:"))
b=int(input(" 2nd number:"))
print(a>b)

"""q11 ) checking the modulo / remainder
operator """
#it gives the value -ve when  -ve/-ve and +ve/-ve :)
a,b=-9,-6
print(a%b)

# **Function practice :-**

#Q12)--concatenation of  two strings :-
str1 = "shivjot "
str2 = "Choudhary"
final=str1+str2
print("result:",final)

#Q13 basic functions :(len())

a = "shivjot"
print(len(a))

#Q14 indexing
a = "shivjot"
print("->",a[4],"\n",a[0:4])

#15 checking the first letter of the sentence is vowel or consonant
a = str(input("Enter the sentence : "))
b = "aeiou"
if a[0]== b[0] or  a[0]== b[1] or a[0]==b[2] or a[0]==b[3] or a[0]== b[4]: #Also we can simply use (a[0] in b)<----
  print("First letter is : Vowel")
else :
  print("First letter is : Consonant")

# q16 minus indexing :-
a= "apple"
print(a[-2:])

#Q17 using .endswith("")#returns boolean value
str="shivjot"
print(str.endswith("ot"))  #str.endswith("") returns true if string ends with substr

#q18 using capitalize () function #it capitalizes the first  index.
a="shivjot"
print(a.capitalize())

#q19 using replace("")
a="clock"
print(a.replace("loc","oo"))

#Q20 wap to input user's first name and print its length. #length() function
a = input("enter your first Name: ")
print(len(a))
a.count("i")

#Q21) list exp :-
a = ["shivjot",99,98.7,"python"]
a[3]="java"
print(a[-3:-1])

#Q22) print all prime no. between 1to n
n = int(input("Enter no:"))
for num in range(2, n+1):
   prime = True
for i in range(2, num):
  if num%i == 0:
    prime = False
    break
    if prime:
      print(num)


#Q23 WAP to ask the user to enter names of 3 fav movies and store them in a list.
a = input("enter movie 1 name:")
b = input("enter movie 2 name:")
c = input("enter movie 3 name:")
d =[a,b,c]
e=[]
e.append(d)
print(e)

#Q24 WAP to check the list contains a palindrome of elements.[1221,1111,2332] or take input
a = []
a.append(input("enter the element 1:"))
a.append(input("enter the element 2:"))
a.append(input("enter the element 3:"))
a.append(input("enter the element 4:"))

if a[0]==a[0][::-1] and a[1]==a[1][::-1]  and a[2]==a[2][::-1]  and a[3]==a[3][::-1] :
  print("Palindrome")
else:
  print("Not palindrome")



#Q25 wap to count the number of students with grade 'A' in the following tuple.
A = ("A","C","B","D","A","C","A")
print(A.count("A"))

#Q26 wap store the above value in a list & sort them from 'A to D'
A = ("A","C","B","D","A","C","A")
b = list(A)
print(b,b.sort())

print(b.sort())

#Q27 Dictionary
info ={
    "key":"value",
    "name":"shivjot",
    1:5.6,
    "list":[3,"shivjot"],
    "tuple":("shivjot",3,4,),
    9.4:"shivjot",
    ("shivjot",55):"tuple"
}
print(info)

print(info["list"])

#Q28 change  and new value of name in the above :-
info["aaa"]="choudhary"
info["name"]="niki"
print(info["aaa"])

print(info)

#Q29 Nested Dictionary
dict={
    "name":"shivjot",
    "subject":{
        "ai/ml":"python",
        "project":"OCR APP"
    }
}
print(dict["subject"]["project"])

print(dict.keys())

#Q30tuple inside a list and list inside a tuple :- list=mutable and tuple = immutable
a=[2,3,(4,5,4)]
a[2]
print(a[-1][0])
type(a)

#Q31 Different functions on sets:-
a = {
    "name":"rahul",
    "subject": "AI/ML"
}
# a.clear()
# a.get("name")
# a.items()
# a.keys()
# a.values()
#a.update({"Name":"shivjot"})
a.update({"name":"goku"})
print(a)

#Q32 Sets:-
a = {"shivjot","rrr","pokemon"}
# type(a)
a.add("shiv")
a.remove("rrr")
print(a)

# **Small project:-**

#Q34) Number guessing game using python :)
import random
print ("AI Number Guessing Game ")
print ("I am thinking of a number between 1 to 100")
numb = random.randint(1,100)
attem = 0
while True:
  guess = int(input("Enter your Guess:-"))
  attem = attem+1
  if guess < numb:
    print("Too low! Try again.")
  elif guess > numb:
    print("Too high! Try again.")
  else:
    print(f"Correct! The number was {numb}")
    print(f"You Guessed it in {attem} attempts.")
    break
