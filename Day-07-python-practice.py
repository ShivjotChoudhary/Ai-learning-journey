#30-01-2026
#Q68)Recursion:-
def show(n):
  if n<=0:
    return
  print(n)
  show(n-1)
show(10)
#Q69) factorial:-
def fac_to(n):
  if n==0 or n==1:
    return 1
  return fac_to(n-1)*n
  print(n)
fac_to(4)

#70) practicing recurton questions :-
#write a recursive function to calculate the sum of first n natural numbers.
def na_tural(n):
  if n==0:
    return 0
  return na_tural(n-1)+n
na_tural(5)

#Q71)write a recursive function to print all the element of the list.
# use list & index as a parameter.
def li_st(a,b=0):
  if b == len(a):
    return 
  print(a[b])
  return li_st(a,b+1)
d = [8,3,4,5,"shiv","rohit"]
li_st(d)
#Q72) File I/O  in python:-
f = open("/content/data.txt","r")
data = f.read()
print(data)
f.close()

#Q73) Reading only first few letters:-
f = open("/content/data.txt","r")
data = f.read(9)
print(data)
f.close()

#Q74) Read only Line :-
f = open("/content/data.txt","r")
bb = f.read()#once the file is readed once then can't be printed again.
print(bb)
bb = f.read()
print(bb)
data = f.readline()# uses /n at the end by implicit 
print(data)
data = f.readline()# prints 2nd line 
print(data)
f.close()
