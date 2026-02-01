#1/02/2026
#Q79)WAFunction that replaces all occurrences of "java" with "python" in above file.
def re_p():
  with open("/content/practice.txt","r+") as a:
    aa=a.read()
    bb=aa.replace("java","python")
    print(bb)
  with open("/content/practice.txt","w") as a:
    a.write(bb)
re_p()

#Q80) search if the word learning is exist in a file 
with open("/content/practice.txt","r") as f:
  a = f.read()
  if "learning" in a:  
    print("exist")
  else:
    print("not exist")

#Q81)wafunction to find which line of file does the word "learning" occur first
#print -1 if word not found.
def fi_nd():
  data = True 
  ab = ""
  line_no = 1
  with open("/content/practice.txt","r") as f:
    while data:
      data = f.readline()
      if ab in data:
        print(line_no)
        return
      line_no+=1
  return -1
fi_nd()


#Q82)From a file conataining numbers separated by comma, print the count of even numbers:-
with open("num.txt","r") as a:
  bb = a.read()
  nn=""
  for i in range(len(bb)):
    if bb[i] == ",":
      print(int(nn))
      nn=""
    else:
      nn+=bb[i]

#Q83)From a file conataining numbers separated by comma, print the count of even numbers:- method-2
with open("num.txt","r") as a:
  count = 0
  bb = a.read()
  inn = bb.split(",")
  for aa in inn:
    if int(aa)%2==0:
      count+=1
      print(aa)
print(count)


### **Starting NUMPY :-**

#Q84) installing numpy:-
!pip install numpy

import numpy as np 
print(np.__version__)

#Q85) Creating list 
import numpy as np

arrayy = np.array([1,2,3,4,5])
print(arrayy)

#Q86) creating multi-dimentional array:-
import numpy as np

arrayy = np.array([[[1,2,3,4,5]]])
                    
print(arrayy.shape)
print(type(arrayy))

#Q87) arrray:- numpy type reference :-
aa = np.array([[1,2,3,4,5,7]],np.int32)
print(aa[0,2])# showing the 0 row , 2 column element = 3.
print(aa.shape)#used for checking  how many rows and cloumn are there.
print(aa.dtype)# checking type like int,float,or strings. also  tells storage?
print(aa.ndim)# to check dimentions

#Q88) changing the value in a array.
aa[0,2] = 4
print(aa)
