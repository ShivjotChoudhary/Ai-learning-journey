# 25/01/2026
#Q35 use of set functions :-
set = { "shivjot","python","coding"}
#print(set.pop())
#set.remove("python")
# set.clear()
#set.add("pokemon1")
print(set)

#Q36 use of mathematical functions on sets :-
#UNION and INTERSECTION:-
set ={'python', 'coding', 'shivjot',"pokemon","rahul"}
set2 ={'python', 'coding', 'shivjot',"school","university"}
#print(set.union(set2))
#print(set.intersection(set2))
print(set.intersection_update(set2))#updates the orignal set 
print(set)

"""Q37)- Store following word meaning in a python dictionary:-
table: "a piece of furniture","list of facts & figures"
cat:"a small animal" """
dict = {
    "Table":["a piece of furniture","list of facts & figures"],
    "cat":"A small animal"
}
# print(dict["Table"])
# print(dict["cat"])
print(dict)


""" Q38:- you are given a list of subejcts for students. Assume one classroom is required for 1 subject.
How many classrooms are needed by All students. sub -["python","java","c++","python","javascript","java","python","java","c++","C"]"""

subjects = {"python","java","c++","python","javascript","java","python","java","c++","C"}
print("So",len(subjects),"classrooms needed by All students")

"""#Q39:- WAP to enter marks of 3 students from the user nd store them in a dictionary. 
Start with an empty dictionary & add one by one. Use subject name as key & marks as value. """
dic = {}
dic.update({"physics":int(input("Enter the marks of Student 1:"))})
dic.update({"Chemistry":int(input("Enter the marks of Student 2:"))})
dic.update({"Math": int(input("Enter the marks of Student 3:"))})
print(dic)
# Q40) Figure out a way to store 9 & 9.0 as seperate values in the set.
 #(you can take help of built-in data types)
set = {(9,9.0)}
print(set)
