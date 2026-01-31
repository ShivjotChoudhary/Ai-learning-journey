#31/01/2026
#Q76)appending a file:-
f = open("/content/2ndexp.txt","a")
a = f.write("\nshivyyy")
f.close()

#Q77) opening in "r+" mode:-
f = open("/content/sample.txt","w+")
a = f.write("shivyy")
print(f.read())
f.close()

#Q78) create a new file "practice.txt" using python. Add the following data in it :-
with open("practice.txt","w") as a:
  b = a.write(" Hi everyone \n we are learning file I/O \n using java \n I like programming in java")


