# Day(02)(22/11/2024)
# age=20
# print(age)
# print(type(age))

# name1,name2,name3="kavi","sathish","sangeetha"
# print(name1)
# print(name2)
# print(name3)

# name1=name2=name3="sathish"
# print(name1)
# print(name2)
# print(name3)

# name=input("enter your name:")
# print(name)
# print(type(name))

# age=input("enter your age:")
# print(age)
# print(type(age))

# int()
# age=(input("enter your age:"))
# print(age)
# print(type(age))

# number=int(input("enter your aadar number: "))
# print(number)
# print(type(number))

# print(int(100.25))
# print(type(int("1000")))

# float()
# print(float(100))
# print(float("100"))

# str()
# print(type(str(100)))
# print(type(str(100.25)))

# bool()
# a=1
# print(bool(a))
#
# b=0
# print(bool(b))
#
# c=-12
# print(bool(c))

#

# List method
# access list item
# mark=[10,20,30,40,50,60,70,80,90,100]
# print(mark[0])
# print(mark[1])
# print(mark[3])

# range of item-slicing(start index,end index-1)
# print(mark[3:6])
# print(mark[-4:-1])
# print(mark[4:])
# print(mark[:4])

# change list item
# mark[4]=55
# print(mark)

# Insert methods

# change range of items slice(start index, end index-1,new element)
# mark[4:7]=[55,65,76]
# mark[7:9]=[85,95,96,97,98,99]
# mark[4:0]=[55,56,57,58,59]
# print(mark)

# insert(item index,value)

# mark.insert(4,500)
# print(mark)

# append()-adding values in last index position
# mark.append(110)
# mark.append([110,120])
# print(mark)

# extends()
# mark1=[10,20,30,40]
# mark2=[50,60,70,80]
# mark1.extend(mark2)
# print(mark1)
# print(mark2)

# del methods

# remove("items")

# names=["Arun","Bala","Charu","Dilip","Ezhil"]
# names.remove("Dilip")
# print(names)

# pop(remove index item)
# names.pop(0)
# names.pop(0)
# print(names)

# using del to delete item
# del names[1]
# del names[4]
# print(names)

# clear()

# names.clear()
# print(names)

# reverse()

# names.reverse()
# print(names)

# sort()
#
# ascending sort
# names.sort(reverse=True)
# print(names)


# join(+)

# mark1=[10,20,30,40]
# mark2=[50,60,70,80]
# mark3=[90,100,110,120]
# marks=mark1+mark2+mark3
# print(marks)

# index(value)

# names=["Ezhil","Charu","Dilip","Arun","Bala"]
# print(names.index("Arun"))
# print(names.index("arun"))

# count
# mark=[10,20,30,10,20,30,10,20,30,20,30]
# print(mark.count(10))
# print(mark.count(20))
# print(mark.count(30))

# copy()
# name1=["Ezhil","Charu","Dilip","Arun","Bala"]
# name2=name1
# # print(name1)
# # print(name2)
# name1.append("Fahad")
# name2.append("Jai")
# print(name1)
# print(name2)
# print(id(name1))
# print(id(name2))

# name1=["Ezhil","Charu","Dilip","Arun","Bala"]
# name2=name1.copy()
# name1=["Ezhil","Charu","Dilip","Arun","Bala"]
# name2=list(name1)
# name1.append("Jai")
# print(name1)
# print(name2)

# names=("sathish","maari","nirmal","bala")
# print(names)
# print(type(names))

# ames = ("Arun")
# print(names)
# print(type(names))
# names = ("Arun")
# print(names)
# print(type(names))

# mark=(10,20,30,40,50,20,40)
# print(mark)
# print(type(mark))

# mark=(50,60,70,80,90,100)
# print(mark[0])
# print(mark[1])
# print(mark[-1])
# print(mark[-2])

# mark=(50,60,70,80,90,100,110,120)
# print(mark[2:4])
# print(mark[5:len(mark)])
# print(mark[3:])
# print(mark[:2])

# print(mark[-3:len(mark)])

mark=(10,20,30,40,50)
mark1=list(mark)
mark1.append(60)
print(mark1)
print(type(mark1))
mark=tuple(mark1)
print(mark)
print(type(mark))
