# #Number data type
# from typing import runtime_checkable
#
# age=20
# x=type(age)
# print(age)
# print(x)
#
# no=0
# print(no)
# print(type(no))
#
# no1=-12
# print(no1)
# print(type(no1))
#
# #Float decimal point
# no2=0.987874
# print(no2)
# print(type(no2))
#
# #it will perform some mathematical opertation
# a=1+5j
# a=6j
# print(a)
# print(type(a))
#
# #denoted by either single quotes or double quotes
# message="welcome to python learning"
# print(message)
# print(type(message))
#
# name='sathishkumar'
# print(name)
# print(type(name))
#
# #Multi line string
# sathish="WELLCOME TO PYTHON LEARNING\n wellcome to java learning\n well come to chennai"
# print(sathish)
# print(type(sathish))
#
# kumar='''well come to dhubai
#          well come to singapoore
#          well come to chennai'''
# print(kumar)
# print(type(kumar))
#
# #Bool data type true or false
# ismarried=False
# ismarried=True
# print(ismarried)
# print(type(ismarried))
#
# #None data type
# a=None
# print(a)
# print(type(a))
#
# #Day (02)
#
# #declare variable in python
# #variable_name=variable_value
# name=("sathish")
# name=("sathishkumar")
# print(name)
# print(type(name))
#
# age=20
# print(age)
# print(type(age))
#
# name1,name2,name3="sathish","kumar","bala"
# print(name1)
# print(name2)
# print(name3)
#
# name1=name2=name3="sathish"
# print(name1)
# print(name2)
# print(name3)
#
# #to det data form user by using input function at runtime
# int()
# age=input("Enter your age")
# print(age)
# print(type(age))
#
# number=int(input("Enter your number:"))
# print(number)
# # print(type(number))--------value error invalid literal for int()


# # STRING AND STRING METHOD
# # STRING-COLLECTION OF CHARACTOR SINGLE OR DOUBLE OR TRIBLE QUOTES
# L="well come to Nirmala sitharaman"
# print(L)
#
# t="""
#     chrompet
#     pallavaram
#     thrisulam"""
# print(t)
#
# # STRING BASED TO WORD ON INDEX POSTION
# u="hello mister"
# print(u[1])
#
# # STRING FORMATING
# name="sathish"
# age=30
# print("My name is ",name," im ",age,"year old")
# print(f"My name is {name} i'm {age} years old")
#
# # STRING CONCATINATION
# firstname="sathish"
# lastname=("kumar")
# fullname=firstname+lastname
# print(fullname)
#
# # STRING METHODS
# # len(str)-return str overall length
# l="Hello sathish"
# print(len(l))
#
# # index (value)-return index position
# s="hello world"
# print(s.index("e"))
# print(s.index("r"))
# print(s.index("d",7))
#
# # r index(value)
# print(s.rindex("l"))
#
# # Find(value)-return index position
# T="hello world"
# print(T.find ("h"))
#
# # Start With
# t="man ager"
# print(t.startswith ("man"))
#
# # Ends with
# print(t.endswith ("ger"))

# Count(value)

# y="Hi everyone"
# print(y.count("o"))
# print(y.count("H"))
#
# # SLICING
# # slicing(double parameter)
# k=("sathishkumar")
# k1=k[0:5]
# print(k1)
# k2=k[6:15]
# print(k2)
#
# k3=k[5:]
# print(k3)
#
# k4=k[ :7]
# print(k4)

# NEGATIVE INDEX
# j="manufacturingcompany"
# j1=j[-6:-2]
# print(j1)
#
# j2=j[-6:len(j)]
# print(j2)
#
# j3=j[-6:]
# print(j3)

# j4=[4:0:-1]---------DOUPT
# print(j4)

# #CAPTALIZE
# s="I LOVE python"
# print(s.capitalize())
#
# # Upper()
# print(s.upper())
#
# # lower()
# print(s.lower())
#
# # isUpper()
# s="HELLO"
# print(s.isupper())
# print(s.islower())
#
# #
# s1="python"
# print(s1.isalpha())
# s2="pyhton1234"
# print(s2.isalpha())
#
# # s3=12345
# # print(s3.isnumeric())
#
# # strip()-remove unwanted space in str before and after
# s="hello world"
# print(s)
# s1=s.strip()
# print(s1)
# s2=s.rstrip()
# print(s2)
# s3=s.lstrip
# print(s3)
#
# # replace
# d="I love javascript"
# d1=d.replace("javascript","python")
# print(d1)
#
# x="i love soniya"
# x1=x.replace("soniya","sangeetha")
# print(x1)
#
# # split()-convert str to list
# q="I love python"
# q1=q.split()
# print(q1)
# q2=q.split(",")
# print(q2)
# print(type(q2))

# # in
# w="I Love python"
# print("Love" in w)
# print("love" in w)
#
# # not in
# print("Love" not in w)
# print("love" not in w)
#
# # contains
# print(w.__contains__("l"))
# print(w.__contains__("o"))

# indentaion error
# a=20
# print(a)
#
# # CONDTIONAL STATEMENT OR DECISION MAKING
#
# #  if else statement
# # if(condtion :true)
#
# # if true:
#   print("condition is true")
# # if false:
#   print("condition is true")
# # else:
#   print("condition is false")


# if a>b:
#     print("A is greater than B")
# elif a==b:
#     print("Both A and B are equal")
# else:
#     print("B is greater than A")

# Logical and or not

# a=int(input("enterNumber:"))
# b=int(input("enternumber:"))
# c=int(input("enternumber:"))
#
# # and operator
# if a>b and a>c:
#     print("if all the condition is true-return will be true")
#
# else:
#     print("if any condition is false-return will be false")

# or
# if a>b or a>c:
#     print("if any condition is true-return will be true")
# else:
#     print("if any condition is false-return will be false")


# nested if else
# mark= int (input("enter your mark:"))
# if mark>=90 and mark<=100:
#     print("s grade")
# elif mark>=80 and mark<=89:
#     print("A grade")
# elif mark>=70 and mark<=79:
#     print("B grade")
# elif mark>=60 and mark<=69:
#     print("C grade")
# elif mark>=50 and mark<=59:
#     print("D grade")
# elif mark>=40 and mark<=49:
#     print("E grade")
# elif mark>=0 and mark<=39:
#     print("fail")
# else:
#     print("Invalid mark")

# login validation

# Username = input("Enter username:")
# password = int (input("Enter password:"))
# if(Username == "greens" and password == 12345):
#     print("Login success")
#
# elif(Username != "greens" and password == 12345):
#     print("Invalid username")
#
# elif(Username == "greens" and password !=12345):
#     print("Invalid password")
#
# else:
#     print("Both values are invalid")

# username = input ("Enter username:")
# password = int(input("Enter Password:"))
#
# if(username == "greens"):
#     password =int(input("Enter Password:"))
# if password == 12345:
#     print("Login success")
# else:
#     print("Invalid Password")

# A=int (input("enter number:"))
# B=int (input("enter number:"))
# C=int (input("enter number:"))
# 
# if A>B and A>C:
#     print("A is first greater B is second greater C is third greater")
# 
# else:
#     print("A is first greater C is second greater B is third greater")
# 
# if B>A and B>C:
#     if A>C:
#         print("B is first greater A is second greater C is third greater")
# 
#     else:
#         print("B is first greater C is second greater A is third greater")
# 
# if C>A and C>B:
#     if B>A:
#         print("C is first greater B is second greater A is third greater")
# 
#     else:
#         print("C is first greater B is second greater A is third greater")

# 24/02/2025
# python list
# List is create by using square bracket

# StudentName=["apple","ball","cat","dog",]
# print(StudentName)

# Access list item
# studentname=["Arun","Bala","Css","Dravid"]
# print(studentname[0])
# print(studentname[1])
# print(studentname[2])
# print(studentname[3])

# Modify list item

# StudentName=["Arun","Bala","Chandru","Dravid"]
# StudentName[0]="Arun"
# print(StudentName)
#
# mark=[7,8,9,10]
# mark[0]=70
# mark[1]=80
# mark[2]=90
# mark[3]=100
# print(mark)

# List method

# mark=[10,20,30,40,50,60,70,80,90,100]
# print(mark[0])
# print(mark[1])
# print(mark[2])
# print(mark[3])

# Range of items
# mark=[10,20,30,40,50,60,70,80,90,100]
# print(mark[3:6])
# print(mark[-4:-1])
# print(mark[-3:-1])
# print(mark[4:])
# print(mark[:4])
# change list item

# mark=[10,20,30,40,50,60,70,80,90,100]
# mark[8]=95
# print(mark)

# Insert methods
# mark=[10,20,30,40,50,60,70,80,90,100]
# mark.insert(4,500)
# print(mark)

# Append-adding values in last index positions
# mark=[10,20,30,40,50,60,70,80,90,100]
# mark.append(110)
# mark.append([110,120])
# print(mark)

# Extends
# mark1=[10,20,30,40,50]
# mark2=[60,70,80,90]
# mark1.extend(mark2)
# print(mark1)
# print(mark2)

# del methods
# remove items

# names=["Arun","Bala","Chandru","Dravid","Elizil"]
# names.remove("Dravid")
# print(names)
#
# Pop(remove index item)
# names=["Arun","Bala","Chandru","Dravid","Elizil"]
# names.pop(0)
# print(names)

# Using del to delete method
# names=["Arun","Bala","Chandru","Dravid","Elizil"]
# del names[4]
# print(names)

# Clear
# names=["Arun","Bala","Chandru","Dravid","Elizil"]
# names.clear()
# print(names)

# reverse
# names=["Arun","Bala","Chandru","Dravid","Elizil"]
# names.reverse()
# print(names)

#sort
# names=["Arun","Bala","Chandru","Dravid","Elizil"]
# names.sort
# descending sort
# print(names)

# join
# mark1=[10,20,30,40,50,]
# mark2=[60,70,80,90,100]
# mark3=[110,120,130,140]
# marks=mark1+mark2+mark3
# print(marks)

# Index(value)
# names=["sathish","kumar","Kavi","mani"]
# print(names.index("sathish"))
# print(names.index("Sathish"))

mark=[10,20,30,40,50,60,70,80,90,100]
print(mark.Count[20])


