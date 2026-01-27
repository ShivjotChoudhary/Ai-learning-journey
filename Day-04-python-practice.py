# **Range( ) Function:-**

#27/01/2026
#Q55)Range()Function:-
for el in range(5):
  print(el)

#Q56)Range()Function:-
for el in range(1,5):
  print(el)

#Q57)Range()Function:-
for el in range(1,6,2):
  print(el)

#Q58)Range()Function:-
for el in range(7,2):
  print(el)

#Q59 practice questions:-
# using for & Range():-
# print numbers from 1 to 100
for el in range(1,101):
  print(el)


#Q60 practice questions:-
# using for & Range():-
# print numbers from 100 to 1 :-
a = range(1,101)
b = a[::-1]
for el in b:
  print(el)

#Q61) print the multiplication table of a number n.
n = int(input("Enter the number:-"))   
for a in range(0,11): 
  print(a*n) 
