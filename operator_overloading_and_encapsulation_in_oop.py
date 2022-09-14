#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Task- 04

class Color:
    def __init__(self, clr):
        self.clr = clr

    def __add__(self, other):
        combined = self.clr + other.clr
    
        if combined == "redyellow" or combined == "yellowred":
            return Color("Orange")
        elif combined == "redblue" or combined == "bluered":
            return Color("Violet")
        elif combined == "yellowblue" or combined == "blueyellow":
            return Color("Green")

#==========================================================================
C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)


# In[6]:


# Task- 05

import math
class Circle:
    def __init__(self, r):
        self.__r = r
        
    def area(self):
        A = math.pi * (self.__r ** 2)
        return A 
    
    def setRadius(self, new_r):
        self.__r = new_r
        
    def getRadius(self):
        return self.__r
    
    def __add__(self, other):
        R = self.__r + other.__r
        return Circle(R)
        
#======================================================================
c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())
c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())
c3 = c1 + c2
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())


# In[2]:


# Task- 06

class Triangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height
        
    def area(self):
        A = 0.5 * self.__base * self.__height 
        return A
        
    def setBase(self, new_base):
        self.__base = new_basae
        
    def getBase(self):
        return self.__base
    
    def setHeight(self, new_height):
        self.__height = new_height 
        
    def getHeight(self):
        return self.__height
    
    def __sub__(self, other):
        B = self.__base - other.__base
        H = self.__height - other.__height 
        return Triangle(B, H) 

#=================================================================
t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())
t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())
t3 = t1 - t2
print("Third Triangle Base:" , t3.getBase())
print("Third Triangle Height:" , t3.getHeight())
print("Third Triangle area:" ,t3.area()) 


# In[4]:


# Task- 07

class Dolls:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
        
    def __gt__(self, other):
        if self.price > other.price:
            return True
        else:
            return False
        
    def __add__(self, other):
        new_name = self.name + " " + other.name
        new_price = self.price + other.price 
        return Dolls(new_name, new_price)
    
    def detail(self):
        if len(self.name.split()) <= 2:
            return f"Doll: {self.name} \nTotal Price: {self.price} taka"
        else:
            return f"Dolls: {self.name} \nTotal Price: {self.price}"
        
#===================================================================================================
obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")


# In[13]:


# Task- 08

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Coordinates(new_x, new_y)
    
    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        return Coordinates(new_x, new_y)
    
    def detail(self):
        return (self.x, self.y)
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return "The calculated coordinates are the same."
        else:
            return "The calculated coordinates are NOT the same."

#================================================================================
p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))
p4 = p1 - p2
print(p4.detail())
p5 = p1 * p2
print(p5.detail())
point_check = (p4 == p5)
print(point_check)


# In[1]:


# Task- 01

class Marks:
    def __init__(self, mark):
        self.mark = mark 

    def __add__(self, other):
        sum = self.mark + other.mark
        return Marks(sum)

#============================================================
Q1 = Marks(int(input("Quiz 1 (out of 10): ")))
Q2 = Marks(int(input("Quiz 2 (out of 10): ")))
Lab = Marks(int(input("Lab (out of 30): ")))
Mid = Marks(int(input("Mid (out of 20): ")))
Final = Marks(int(input("Final (out of 30): ")))
total = Q1 + Q2 + Lab + Mid + Final
print("Total marks: {}".format(total.mark))


# In[2]:


# Task- 02

class Teacher:
    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept
        self.__list = []
  
    def addCourse(self, c):
        self.__list.append(c.course)

    def printDetail(self):
        print("=" * 50)
        print(f"Name: {self.__name}")
        print(f"Department: {self.__dept}")
        print("List of courses")
        print("=" * 50)
        for i in self.__list:
            print(i)
        print("=" * 50)

class Course:
    def __init__(self, course):
        self.course = course


#==========================================================================
t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")
c1 = Course("CSE 110 Programming Language I")
c2 = Course("CSE 111 Programming Language-II")
c3 = Course("CSE 220 Data Structures")
c4 = Course("CSE 221 Algorithms")
c5 = Course("CCSE 230 Discrete Mathematics")
c6 = Course("CSE 310 Object Oriented Programming")
c7 = Course("CSE 320 Data Communications")
c8 = Course("CSE 340 Computer Architecture")
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()


# In[3]:


# Task- 03

class Team:
    def __init__(self, Country = None):
        self.__Country = Country
        self.__list = []
    
    def setName(self, desh):
        self.desh = desh
        if self.__Country == None:
            self.__Country = self.desh

    def addPlayer(self, n):
        self.__list.append(n.name)

    def printDetail(self):
        print("=" * 30)
        print(f"Team: {self.__Country}")
        print("List of Players:")
        print(self.__list)
        print("=" * 30)

class Player:
    def __init__(self, name):
        self.name = name

#====================================================================
b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()

