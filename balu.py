# Functions:
""" create a sum() it can take 2 arguments to do sum """
'''def sum(num1,num2):
    print(num1+num2)
num1=int(input("enter your no."))
num2=int(input("enter your num:"))
sum(num1,num2)'''

# write a python function to summ all the numbers in a list
'''def sum(numbers):
    total=0
    for x in numbers:
        total=total+x
    print(total)
numbers=[4,5,6,7,8,10]
sum(numbers)'''

# _____________________________________________

"""def num(a1):
    sum=1
    for i in a1:
        sum=sum*i
        print(sum)
a1=[10,20,30]
num(a1)


def a(num):
    total=0
    for i in num:
        total=total+int(i)
    print(total)
num=int(input("enter the list:-"))
a(num)"""

# ====================================

# write a python program to print even numbers in the list

'''def evn(num):
    #even=0
    for i in range(1,len(num)):
        if i%2==0:
            print(i,end=" ")
num=[1,2,3,4,5,6,7,8,9]
evn(num)'''

# write a function that converts a decimal number into a binary number

# def dectob(num):
#     if num>1:
#       dectob(num//2)
#     print(num%2,end="")
# dectob(10)

"""Return"""
"""return :- a special key word that you can use inside a function or method to send the function results back to the caller"""

#what is the purpose of return>
""" when you return the value you can decide what you gonna do with value"""
# x= len(input("enter the string:"))
# print(x**2)

# def f1(x):
#     print(x)
# print(f1(10))

# output:= 10
# None
""" when i use print(x) and give the argument f1(10) the 10 will gets to the f1(x) place and first print the 10"""

# def f1(x):
#     return x
# print(f1(10))

# sum = 10
# def ac(x):
#     return x+sum
# print(ac(10))

"""sum = 5
def fun(x):
a=x+xum"""



# def sum(x):
#     a=0
#     for i in range(0,x+1):
#         a=a+i
#     print(a)
# sum(7)

# num = int(input("enter the number:"))
# sum=sum(range(1,num+1))
# print(sum)


#list comprehension:
""" It offers you a smaller line of code that you can create a new list from the existing list"""

# list_fruits=["apple","banana","grapes","mango","orange"]
# a = []
# for i in list_fruits:
#     if "a" in i:
#
#         a.append(i)
# print(a)


# list_fruits=["apple","banana","grapes","mango","aaaa"]
# new=[i for i in list_fruits if "b" in i ]
# print(new)

# li=[list comprehension:
""" It offers you a smaller line of code that you can create a new list from the existing list"""

# list_fruits=["apple","banana","grapes","mango","aaaa"]
# a = []
# for i in list_fruits:
#     if "a" in i:
#         a.append(i)
# print(a)

# list_fruits=["apple","banana","grapes","mango","aaaa"]
# new=[i for i in list_fruits if i != "banana"]
# print(new)

#crreate a list of numbers from 0 to 20?
# num=[]
# for i in range(0,20):
#     num.append(i)
# print(num)

# list comparention
# num=[i for i in range(21)]
# print(num)
#
# even=[i for i in range(21) if i%2==0]
# print(f"even numbers{even}")
#
# odd=[i for i in range(21) if i%2==0]
# print(f"odd numbers{odd}")
#
#
# # create a new list of numbers in the range of 20 the output must  be multiple of 2:
#
# nemb=[i*2 for i in range(21)]
# print(nemb)

# =========================================================================================
"""Lambda"""
# what is lambda?
# lambda is a "anonynous function"
# anonymous function means this function doesn't have name
# def f1(x):
#     return(x)
# print(f1(20))

# syntax for lambda(): "lambda arguments: expression"
# lambda is an anonymous function it can have many arguments and single expression"

# what is an expression?
# expression is some kind of statement/calculation/steps using that values to give single value
# lambda is an anonymous function how can you call it.
# we generally use this function where it has some name.
# means we can create a variable to call this function.

# x=lambda a: a+10
# # where your calling the lambda function use the variable name.
# print(x(5))

#
# x=lambda a,b,c : a+b+c
# print(x(5,6,7))

# when we can use the lambda function ?
# create function that can give square of every number?

"""def sqr(x):
    return x **2
def cube(x):
    return x **3
def four(x):
    return x**4

print(sqr(2))
print(cube(2))
print(four(2))"""

# def pow(n):
#     return lambda a: a**n
# sqr = pow(2)
# cub= pow(3)
# print(sqr(6))
# print(cub(3))

# what is global variable?







# what is local variable?
# creating a variable inside the function is known as local variable.

# def f():
#     x = "balu"
#     return x
# print(f())

# ==============================================================================

"""Map():"""
# what map does?
# it uses a function on iterables/.
# wha is iterables?
# list,tuple,dict,set,array,
# map will take a function and runs it over the iterables.
""" functions are the 1st clas objects. which means one function can act as an arguments from another function"""
# syntax: map = (function,iterables)
a= ("apple","banana","mango","orange")
# lent=[]
# for i in a:
#     lent.append(len(i))
# print(lent)
#
#
# # list comprention
# l=[len(i) for i in a]
# print(l)
# print("============")
#
#
# a= ("apple","banana","mango","orange")
# # if you want to display the output by using the map function we need to decide in which iterables (list,tuple,set) the output has
# lent = tuple(map(len,a))
# print(lent)


# def a1(x):
#     return "hello " + x
# print(a1("apples"))
#
# # apply the function foe each iten in the collection.
#
# l=list(map(a1,a))
# print(l)
#
# # when we have to use the map function?
# """ when we are having multiple user input collection then we cam use the map function """
#
# user = input()
# print(user)
# print(type(user))

# user = input().split()
# print(user)
# print(type(user))
#
# num= []
# for i in user:
#     num.append(i)
# print(num)


# take a set of numbers being separated with the spaces.
# user=input().split()
# print(user)
# print(type(user))

# how to convert the string of elements into the string

# user= input().split()
# num=[]
# for i in user:
#     num.append(int(i))
# print(num)
# print(type(num))

# user = input().split()
# num=set(map(int,user))
# print(num)
# print(type(num))

# numb= tuple(map(int,input().split()))
# print(numb)

# before executing the map() we need to decide in what type of collection, do we need this

# how can you print the following 10 20 30 40 50 in double that to in tuple?

# lambda:- you can have many arguments but single expression
# double = tuple(map(lambda a:a*2,numb))
# print(double)

#

# double = tuple(map(lambda a:a*2,map(int,input().split())))
# print(double)

"""map(int,input().split())--> map storing entire thing/data, if we want to be in a readable we need to add "tuple","list","set" """

# ==============================================================================
""" Filter():- collection_name(filter(function,iterable))"""
# filter give output of the collection if the condition is true

# age=[18,48,21,22,12,20,11,7,66,34,56]
# # def adult(x):
#     if x >=18:
#         return x
# f1=list(filter(adult,age))
# print(f1)
# #print(adult(19))

# f1=list(filter(lambda a:a>=18,age))
# f1.sort()
# print(f1)

# how can i give more expressions when i am using the conditional statements.
# shall we use the logical operations in lambda ---> yes
# f1=list(filter(lambda a:a>=18 and a<=40,age))
# print(f1)
#
# f1=list(filter(lambda a: 18 <=a<=40,age))
# print(f1)
""" filters basically it filters your original collection that returns true or false, any value that comes out to the true the original value can be stored as a collection(list,set,tuple) of items """
# ==================================
""" regular expressions"""
# is a built in package which is known as "re"
# A RegEx, or regular expressions is a sequence of character that forms a s

# import re
# txt = "hello world!"
# # search weather world is present or not
# x=re.search("world!$",txt)
# print(x)

# regular expression function
# findall() ---> returns a list containing all matches
# search() --> return match objects
# split
# sub--> it is used to replace one are many matches with the string





""" Class and Object """
# why we are creating the classes and objects?

# how to create a class?
# to create a class wee are using the key word "class".

""" synatax of class:- class classname:"""
# class customers:
#     pass
# # object creation
# c1= customers()   #----> object
# print(c1)



# what is __main__?
# main is nothing but from which file the class is comming from

""" Attribute :- there are 2 types
1. class attributes:
class attributes comes from class and these attributes accessible by every object (common attributes).
2.object attributes :-
object attributes means unique attributes that can be applicable to particular objects """

# create a class
# class customer:
# # create class attributes --> creating variables inside tha class
#     bank_name="union bank"
#     branch="Hyderabad"
#     state= "telangana"
#     Ifsc="FDM2357045"
#
# #create a object
# c1=customer()
# c2=customer()
# # how can oject cam access the class attribute
# print(c1.bank_name)
# print(c2.Ifsc)

# create the methods for class customers
# what is method?
# method can be created inside the class.
# methods are noting but creating functions inside the class.

# class customer:
#     bank_name="union bank"
#     branch="Hyderabad"
#     state= "telangana"
#     Ifsc="FDM2357045"
# # creating methods
#     def welcome(self):
#        print("Hello and welcome to union bank")
# #create a object
# c1=customer()
# c2=customer()
# # how can we access the particular methods ?
# c1.welcome()
# print(c1.bank_name)
# c2.welcome()
# print(c2.branch)

# what is self?
# self its a extra parameter in the method defination.
# class .method(object)
# self act as a pointer/referance to access the object.


# read the file.
""" f = open("trail.txt")
print(f.read())
f.close()"""

#To read the excel file use "xlrd" library
#what is xlrd
# import xlrd
# """xlrd is a library for reading data and formatting information from excel file
# .it supports .xls format only"""
# loc="C:\\Users\\91630\\OneDrive\\Desktop\\Financial Sample (1).xls"
# # use xlrd.ope_workbook to read the xls file.
# wb=xlrd.open_workbook(loc)
# # how to access the particular sheet data?
# sheet = wb.sheet_by_index(0)
# #xls _sheet_by_index  starts with zero
# #read data sell wise
# # if i want to know how many rows and columns in given file.
# print(sheet.nrows)
# print(sheet.ncols)
# #read the particular cell
# #cell_value(row,col)
# #indexing can be starts from zero
# print(sheet.cell_value(7,2))   # 7th row 2nd column
# # print entire rows
# print(sheet.row_values(0))
# print(sheet.col_values(1))
# #extract all the data in console.
# for x in range(sheet.nrows):
#     print(sheet.row_values(x))


# Iterators:-
# what is iterators?
# iterators helps you take large bunch of data in limited memory space
# means it breaks the large data in to tiny chunks.
# in iterators we are having 2 protocols
# 1. __iter__()
# 2. __next__()
l=["apple","banana","grapes","mango","orange"]
"""for i in l:
    # i is iter over each and every elements in the collection.
    print(l)"""
#
# x=iter(l)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# class number:
#     def __iter__(self):
#         self.inital = 0
#         return self
#     def __next__(self):
#         if self.inital <=5:
#            x = self.inital
#            self.inital +=1
#            return x
#         else:
#             StopAsyncIteration("are you mad")
# n = number()
# # for x in n:
# #    print(x)
# x = iter(n)
# print(next(n))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

"""======================================================"""

# GENARATERS:-
"""a generator is function that returns an iterator that produce a sequence of values when iterated over"""
# when we have to use this generators?
"""generators are use when we want to produce large sequence of values, we don't want to store all of them in the memory at once"""

# use "def" , instead of "return"  use "yield"

# def my_generator(n):
#     value = 0
#     # loop until counter is less than n
#     while value < n:
#         yield value
#         value += 1
# # iterate over your generator to generate sequence of values
# for value in my_generator(3):
#     print(value)

""" Note:- when your using integer directly into for loop it throws an error use it with the range function.
            when your using generators then instead of return use yield it support int object in for loop """

# pickling:-
""" the process of converting any type of object in python for example (list, tuple, set,--etc) on to bytes is known as pickling."""
""" when it comes to python these pickling conversions is known as "serialisation" and "de-serialisation" """

# what is bytes?
# 0's and 1's is known as bytes
# to do the pickling use package called "pickle"

# convertion of 2d data formate to 1d data and store it
# and in same time convertion 1d data into 2d is known as pickling

# import pickle
# open a pickle file.txt
# pickle_file = open("pickle2.txt","wb") # wb is known as work as bytes
# # use pickle.dump to dump the file
# my_dict = {"1":"a","2":"b"}
# pickle.dump(my_dict,pickle_file)
# #pickle.dump(collection_name,pickle_file name(where you war
# pickle_file=open("pickle2.txt","rb")
# # load the data that you have stored
# new_dict = pickle.load(pickle_file)
# print(new_dict)


"""step1:- import pickle library
step2:- create a pickle file in "wb"
step3:- use "pickle.dump" to convert the data
step4:- read the actual data  by using "open(pickle filename","rb")
step5:- after that load the data into new file
step6:- print the file"""

# ==============================================

# python Pip:-
""" pip :- python install packages """
""" pip is basically package manger for the python package or module"""
# what is package?
""" package is basically something that contains all the files you needed"""
# packages contains all the files you need for certain modules.
# what is module?
""" modules are code libraries which you can include in your project."""
# Numpy
# Pandas
# matplotlib
# seaborn
# pendulum
# python image processing
# movie py
# tkinter
# pyqt
# py32
# pytest

# how to install this package?
# what is global package?
# what is local package?
""" py -m pip install "package name" when you use cmd """
""" !pip install "package name" ---> in  colab notebook and jupyter notebook"""
# what is global package and what is local package?
# import camelcase
# x = camelcase.CamelCase()
# aa = "hi there! this is the message to check each word of letters are capital"
# print(x.hump(aa))

# how to uninstall packages from cmd?
# py -m uninstall "package name"
# how to check what are all packages present in your system?
# py-m pip list
# how to upgrade your pip?
# py -m pip install --upgrade pip
# how to check the version of your pip?
# py -m pip --version


# =======Json==============
""" java script object notation"""
""" It is basically a syntax that storing and exchanging the data. """
""" { first _name:"Balu",
       "last_name:"kavide",
       address:{street: jangaon,
                "city:}"""

import json
# # what is parse?
# """ it is a method where one string of data is converting into another form of data """
# person = {"name": "balu",
#           "language":["english","telugu"]}
# # convert this into jason format
# person_dict = json.dumps(person)
# print(person_dict)
# print(type(person_dict))

a="C:\\Users\\91630\\OneDrive\\Desktop\\sample1 js.json"
with open(a) as b:
    data = json.load(b)
print(data)












