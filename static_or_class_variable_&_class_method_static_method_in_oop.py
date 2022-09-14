#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task- 01

class Student:
    ID = 0
    def __init__(self, name, department, age, cgpa):
        self.name = name 
        self.department = department 
        self.age = age 
        self.cgpa = cgpa
        Student.ID += 1 
        
    def get_details(self):
        print(f"ID: {Student.ID}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Age: {self.age}")
        print(f"CGPA: {self.cgpa}")
        
    @classmethod
    def from_String(cls, info):
        name, department, age, cgpa = info.split("-")
        obj = cls(name, department, age, cgpa)
        return obj
    
#================================================================
s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()


# In[2]:


# Task- 02

class Assassin:
    number = 0
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate 
        Assassin.number += 1
        
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Success rate: {self.rate}%")
        print(f"Total number of Assassin: {Assassin.number}")
    
    @classmethod
    def failureRate(cls, name, f_rate):
        rate = 100 - f_rate
        return cls(name, rate)
    
    @classmethod
    def failurePercentage(cls, name, f_percentage):
        rate = 100 - int(f_percentage[0 : 2])
        return cls(name, rate)
        
#======================================================================
john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()


# In[2]:


# Task- 03

class Passenger:
    count = 0
    
    def __init__(self, name):
        self.name = name 
        Passenger.count += 1
        
    def set_bag_weight(self, weight):
        self.weight = weight
        
        if self.weight <= 20:
            self.fare = 450
            
        elif 21 <= self.weight <= 50:
            self.fare = 450 + 50
            
        elif self.weight > 50:
            self.fare = 450 + 100
            
    def printDetail(self):
        print(f"Name: {self.name}")
        print(f"Bus Fare: {self.fare}")

#==================================================================

print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)


# In[6]:


# Task- 04

class Travel:
    count = 0
    
    def __init__(self, source, destination, time = None):
        self.source = source 
        self.destination = destination 
        self.time = time
        Travel.count += 1
        
    def display_travel_info(self):
        if self.time == None:
            return f"Source:{self.source} \nDestination: {self.destination} \nFlight Time: 1:00"
        else:
            return f"Source:{self.source} \nDestination: {self.destination} \nFlight Time: {self.time}:00"
    
    def set_destination(self, new_destination):
        self.destination = new_destination
        
    def set_source(self, new_source):
        self.source = new_source
    
    def set_time(self, new_time):
        self.time = new_time
       
#========================================================================
print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)


# In[2]:


# Task- 05

class Employee:
    def __init__(self, name, workingPeriod):
        self.name = name
        self.workingPeriod = workingPeriod
        
    @classmethod
    def employeeByJoiningYear(cls, name, year):
        workingPeriod = 2022 - year
        obj = cls(name, workingPeriod)
        return obj
    
    @staticmethod 
    def experienceCheck(wp, gender):
        if wp < 3 and gender == "male":
            return "He is not experienced"
        elif wp < 3 and gender == "female":
            return "She is not experienced"
        elif wp >= 3 and gender == "male":
            return "He is experienced"
        elif wp >= 3 and gender == "female":
            return "She is experienced"
            
#================================================================
employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))


# In[11]:


# Task- 06

class Laptop:
    laptopCount = 0
    
    def __init__(self, name, count):
        self.name = name 
        self.count = count 
        Laptop.laptopCount += count
    
    @classmethod
    def resetCount(cls):
        cls.laptopCount = 0
        
    @staticmethod
    def advantage():
        print("Laptops are portable")

#==================================================================
lenovo = Laptop("Lenovo", 5);
dell = Laptop("Dell", 7);
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)


# In[2]:


# Task- 07

class Cat:
    Number_of_cats = 0
    
    def __init__(self, color, activity):
        self.color = color
        self.activity = activity
        Cat.Number_of_cats += 1
        
    def changeColor(self, new_color):
        self.color = new_color
        
    def printCat(self):
        print(f"{self.color} cat is {self.activity}")
        
    @classmethod
    def no_parameter(cls):
        obj = cls("white", "sitting")
        return obj
    
    @classmethod
    def first_parameter(cls, color):
        obj = cls(color, "sitting")
        return obj
    
    @classmethod
    def second_parameter(cls, activity):
        obj = cls("Grey", activity)
        return obj

#====================================================================
print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)


# In[5]:


# Task- 08

import math
class Cylinder:
    radius = 5
    height = 18
    
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height 
        print(f"Default radius={Cylinder.radius} and height={Cylinder.height}.")
        print(f"Updated: radius={self.radius} and height={self.height}.")
        Cylinder.radius = self.radius
        Cylinder.height = self.height
        
    @classmethod
    def swap(cls, height, radius):
        obj = cls(radius, height)
        return obj
              
    @classmethod
    def changeFormat(cls, info):
        radius, height = info.split("-")
        obj = cls(float(radius), float(height))
        return obj
    
    @staticmethod
    def area(radius, height):
        A = (2 * math.pi * radius * radius) + (2 * math.pi * radius * height)
        print(f"Area: {A}")
              
    @staticmethod
    def volume(radius, height):
        V = math.pi * radius * radius * height
        print(f"Volume: {V}")

#=========================================================================
c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)


# In[7]:


# Task- 09

class Student:
    ts = 0
    bracus = 0
    ois = 0
    
    def __init__(self, name, dept, institute = None):
        self.name = name
        self.dept = dept
        self.institute = institute
            
    def individualDetail(self):
        if self.institute == None:
            print(f"Name: {self.name}")
            print(f"Department: {self.dept}")
            print("Institution: BRAC University")
            Student.bracus += 1
            Student.ts += 1
            
        else:
            print(f"Name: {self.name}")
            print(f"Department: {self.dept}")
            print(f"Institution: {self.institute}")
            Student.ois += 1
            Student.ts += 1
            
    @classmethod
    def createStudent(cls, name, dept, institute = None):
        if institute == None:
            obj = cls(name, dept)
            return obj
        else:
            obj = cls(name, dept, institute)
            return obj
    
    @classmethod
    def printDetails(cls):
        print(f"Total Student(s): {cls.ts}")
        print(f"BRAC University Student(s): {cls.bracus}")
        print(F"Other Institution Student(s): {cls.ois}")
        
#=======================================================================
Student.printDetails()
print('#########################')
mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()
print('========================')
harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()
print('=========================')
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()


# In[7]:


# Task- 10

class SultansDine:
    total_branch = 0
    total_sell = 0
    info_list = []
    
    def __init__(self, location):
        self.location = location
        SultansDine.total_branch += 1
        
    def sellQuantity(self, num):
    
        if num<10:
            self.branch_sell = num*300
        elif num<20:
            self.branch_sell = num*350
        else:
            self.branch_sell = num*400
            
        SultansDine.total_sell += self.branch_sell
        
    def branchInformation(self):
        print(f"Branch Namre: {self.location}")
        print(f"Branch Sell: {self.branch_sell} Taka")
        SultansDine.info_list.append(self.location)
        SultansDine.info_list.append(self.branch_sell)
        
    @classmethod
    def details(cls):
        print(f"Total Bumber of Branch(s): {cls.total_branch}")
        print(f"Total sell: {cls.total_sell} Taka")
        
        for i in range(0, len(SultansDine.info_list), 2):
            print(f"Branch Name: {SultansDine.info_list[i]}, Branch Sell: {SultansDine.info_list[i + 1]} Taka")
            print(f"Branch consists of total sell's: {(SultansDine.info_list[i + 1] / SultansDine.total_sell) * 100:.2f}%")

#=========================================================================================================================
SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()


# In[11]:


#Task- 11 (Tracing)

class Puzzle:
    x = 0

    def methodA(self):
        Puzzle.x = 5
        z = Puzzle.x + self.methodB(Puzzle.x)
        print(Puzzle.x, z)
        z = self.methodB(z + 2) + Puzzle.x
        print(Puzzle.x, z)
        self.methodB(Puzzle.x, z)
        print(Puzzle.x, z)

    def methodB(self, *args):
        
        if len(args) == 1:
            y = args[0]
            Puzzle.x = y + Puzzle.x
            print(Puzzle.x, y)
            return Puzzle.x + 3
        else:
            z, x = args
            z = z + 1
            x = x + 1
            print(z, x)

p = Puzzle()
p.methodA()
p.methodA()
p = Puzzle()
p.methodA()
p.methodB(7)


# In[5]:


#Task- 12 (Tracing)

class FinalT6A:
    temp = 3

    def __init__(self, x, p):
        self.sum, self.y = 0, 2
        FinalT6A.temp += 3
        self.y = self.temp - p
        self.sum = self.temp + x
        print(x, self.y, self.sum)

    def methodA(self):
        x, y = 0, 0
        y = y + self.y
        x = self.y + 2 + self.temp
        self.sum = x + y + self.methodB(self.temp, y)
        print(x, y, self.sum)

    def methodB(self, temp, n):
        x = 0
        FinalT6A.temp += 1
        self.y = self.y + (FinalT6A.temp)
        FinalT6A.temp -= 1
        x = x + 2 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum
    
q1 = FinalT6A(2,1)
q1.methodA()
q1.methodA()


# In[3]:


# Task- 13 (Tracing)

class A:
    temp = 4
    def __init__(self):
        self.y = self.temp - 2
        self.sum = self.temp + 1
        A.temp -= 2
        self.methodA(3, 4)
        
    def methodA(self, m, n):
        x = 0
        self.y = self.y + m + (self.temp)
        A.temp += 1
        x = x + 1 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)

class B:
    x = 0
    def __init__(self, b = None):
        self.y, self.temp, self.sum = 5, -5, 2

        if b == None:
            self.y = self.temp + 3
            self.sum = 3 + self.temp + 2
            self.temp -= 2
        
        else:
            self.sum = b.sum
            B.x = b.x
            b.methodB(2, 3)
            
    def methodA(self, m, n):
        x = 2
        self.y = self.y + m + (self.temp)
        self.temp += 1
        x = x + 5 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        
    def methodB(self, m, n):
        y = 0
        y = y + self.y
        B.x = self.y + 2 + self.temp
        self.methodA(self.x, y)
        self.sum = self.x + y + self.sum
        print(self.x, y, self.sum)

    
a1 = A()
b1 = B()
b2 = B(b1)
b1.methodA(1, 2)
b2.methodB(3, 2)


# In[7]:


#Task- 14 (Tracing)

class msgClass:
    def __init__(self):
        self.content = 0

class Quiz3:
    x = 0
    def __init__(self, k = None):
        self.sum, self.y = 0, 0
        if k is None:
            self.sum = 5
            Quiz3.x = 2
            self.y = 2
            
        else:
            self.sum = self.sum + k
            self.y = 3
            Quiz3.x += 2
            
    def methodA(self):
        x = 1
        y = 1
        msg = [None]
        myMsg = msgClass()
        myMsg.content = Quiz3.x
        msg[0] = myMsg
        msg[0].content = self.y + myMsg.content
        self.y = self.y + self.methodB(msg[0])
        y = self.methodB(msg[0]) + self.y
        x = y + self.methodB(msg, msg[0])
        self.sum = x + y + msg[0].content
        print(x, y, self.sum)
        
    def methodB(self, *args):
        if len(args) == 2:
            mg2, mg1 = args
            x = 2
            self.y = self.y + mg2[0].content
            mg2[0].content = self.y + mg1.content
            x = x + 2 + mg1.content
            self.sum = self.sum + x + self.y
            mg1.content = self.sum - mg2[0].content
            print(Quiz3.x, self.y, self.sum)
            return self.sum

        elif len(args) == 1:
            mg1, = args
            x = 1
            y = 2
            y = self.sum + mg1.content
            self.y = y + mg1.content
            x = Quiz3.x + 5 + mg1.content
            self.sum = self.sum + x + y
            Quiz3.x = mg1.content + x + 3
            print(x, y, self.sum)
            return y
        
a1 = Quiz3()
a2 = Quiz3(5)
msg = msgClass()
a1.methodA()
a2.methodB(msg)


# In[ ]:




