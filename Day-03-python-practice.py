#26/1/2026
#Loops 
#Q41) Loops :-
while True:
  print("shivjot")
  break

#loops practice:-
# Q42) loops 
i = 8
while i<=33:
  print("shivjot",i)
  i*=2

#practice questions Loops:-
#Q43! Print numbers from 1 to 100.
a =1 
while a<=100:
  print(a)
  a+=1

#Q44) print numbers from 100 to 1 :-
a =100 
while a>=1:
  print(a)
  a-=1

#Q45) print a multiplication table of a number n.
n = int(input("Enter the number: "))
a = 0
while a<=10:
  print(n*a)
  a+=1


#Q46) Print the element of the following list using loop
#[1,4,9,16,25,36,49,64,81,100]
lt = [1,4,9,16,25,36,49,64,81,100]
b=0
while b<len(lt):
  print(lt[b])
  b+=1

#Q47) Search for a number X in this tuple using loop:
tup = (1,4,9,16,25,36,49,64,81,100)
x = 4
a=0
while a<len(tup)-1:
  if x==tup[a]:
    print("Found it ")
  a+=1


#Q48) Break :-
i = 1 
while i<10:
  print(i)
  if i==6:
    break
  i+=1

#Q49) Continue:-
i = 1 
while i<=10:
  if i%2==0:
     i+=1
     continue
  print(i)
  i+=1

#50 for loop on list :-
list = ["avenger", "pokemon","dark","light"]
for li in list:
  print(li)

#Q51 for loop  on string:-
#50 for loop
list = "avenger"
for li in list:
  print(li)

#Q52 for loop - if -else :-
str = "shivjot"
for sl in str:
  if sl=="o":
    print("O Found")
    break
  print(sl)
else:
  print("END")

#Q53 practice questions for loop :-
#print the elements of the following list using a (for)loop:-[1,4,9,16,25,36,49,64,81,100]
a = [1,4,9,16,25,36,49,64,81,100]
for b in a:
  print(b)

#Q54 Search  for the number X in this tuple using (for) loop:-
#(1,4,9,16,25,36,49,64,81,100)
a = (1,4,9,16,25,36,49,64,81,100)
print(type(a))
c = 25 
for b in a:
  if b == c:
    print("Found it:-",c,)
