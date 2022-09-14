#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Task- 01

class Calculator:
    def __init__(self, first_value, operator, second_value):
        self.first_value = first_value
        self.operator = operator
        self.second_value = second_value
        print("Let's Calculate!")

        if self.operator == "+":
            Calculator.add(self)
        elif self.operator == "-":
            Calculator.subtract(self)
        elif self.operator == "*":
            Calculator.multiply(self)
        elif self.operator == "/":
            Calculator.divide(self)
    def add(self):
        print(f"Value 1: {self.first_value} \nOperator: {self.operator} \nValue 2: {self.second_value} \nResult: {self.first_value + self.second_value}")
    def subtract(self):
        print(f"Value 1: {self.first_value} \nOperator: {self.operator} \nValue 2: {self.second_value} \nResult: {self.first_value - self.second_value}")
    def multiply(self):
        print(f"Value 1: {self.first_value} \nOperator: {self.operator} \nValue 2: {self.second_value} \nResult: {self.first_value * self.second_value}")
    def divide(self):
        print(f"Value 1: {self.first_value} \nOperator: {self.operator} \nValue 2: {self.second_value} \nResult: {self.first_value / self.second_value}")

first_value = int(input())
operator = input()
second_value = int(input())

Cal = Calculator(first_value, operator, second_value)


# In[3]:


# Task- 02

class Course:
    def __init__(self, c, f, n):
        self.c = c
        self.f = f
        self.n = n
    def detail(self):
        print(f"{self.c} - {self.f} - {self.n}")

c1 = Course("CSE110", "TBA", 8)
c1.detail()
print("===============")
c2 = Course("CSE111", "TBA", 9)
c2.detail()


# In[4]:


# Task- 03

class Patient:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} cm")

    def printDetails(self):
        h = self.height / 100
        print(f"BMI: {self.weight / h ** 2}")


p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()


# In[5]:


# Task- 04

class Vehicle:
    def __init__(self, x= 0, y= 0):
        self.x = x
        self.y = y
    def moveUp(self):
        self.y += 1
    def moveDown(self):
        self.y -= 1
    def moveLeft(self):
        self.x -= 1
    def moveRight(self):
        self.x += 1
    def print_position(self):
        print((self.x, self.y))

car = Vehicle()
car.print_position()
car.moveUp()
car.print_position()
car.moveLeft()
car.print_position()
car.moveDown()
car.print_position()
car.moveRight()


# In[6]:


# Task- 05

class Shape:
    def __init__(self, shape, n1, n2):
        self.shape = shape
        self.n1 = n1
        self.n2 = n2

    def area(self):
        if self.shape == "Triangle":
            print(f"Area: {0.5 * self.n1 * self.n2}")
        elif self.shape == "Square":
            print(f"Area: {self.n1 * self.n2}")
        elif self.shape == "Rhombus":
            print(f"Area: {0.5 * self.n1 * self.n2}")
        elif self.shape == "Rectangle":
            print(f"Area: {self.n1 * self.n2}")
        else:
            print("Shape unknown")

triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()


# In[7]:


# Task- 06

class Calculator:
    def __init__(self):
        print("Calculator is ready!")

    def calculate(self, value1, value2, operator):
        self.value1 = value1
        self.value2 = value2
        self.operator = operator
    
        if self.operator == "+":
            self.x = self.value1 + self.value2
        elif self.operator == "-":
            self.x = self.value1 - self.value2
        elif self.operator == "*":
            self.x = self.value1 * self.value2
        elif self.operator == "/":  
            self.x = self.value1 / self.value2
        return self.x

    def showCalculation(self):
        print(self.value1, self.operator, self.value2, "=", self.x)

c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()


# In[13]:


# Task- 07

class Student:
    def __init__(self, name, id, dept, cgpa):
        self.name = name
        self.id = id
        self.dept = dept
        self.cgpa = cgpa
        
    def calculate_CGPA(self):
        sum = 0
        for i in self.cgpa:
            sum += i * 3
        self.result = sum / (len(self.cgpa) * 3)
        return self.result
    
    def print_details(self):
        print(f"Name: {self.name}, ID: {self.id}")
        print(f"Department: {self.dept}")
        print(f"CGPA: {self.result}")
        
        if self.result > 3.80:
            print("Your academic standing is 'Highest Distinction'")
        elif 3.65 < self.result <= 3.80:
            print("Your academic standing is 'High Distinction'")
        elif 3.50 < self.result <= 3.65:
            print("Your academic standing is 'Distinction'")
        elif 2.00 < self.result <= 3.50:
            print("Your academic standing is 'Satisfactory'")
        elif self.result < 2.00:
            print("Sorry, you cannot graduate")
        
            

s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
s1.calculate_CGPA()
print("==========================")
s1.print_details()
print("==========================")
s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
s2.calculate_CGPA()
print("==========================")
s2.print_details()
print("==========================")
s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
s3.calculate_CGPA()
print("==========================")
s3.print_details()


# In[3]:


# Task- 08

class Shinobi:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.mission = 0
        self.salary = 0
        
    def changeRank(self, rank):
        self.rank = rank
        
    def calSalary(self, mission):
        self.mission = mission
        
        if self.rank == "Genin":
            self.salary = self.mission * 50
        elif self.rank == "Chunin":
            self.salary = self.mission * 100
        else:
            self.salary = self.mission * 500
    
    def printInfo(self):
        print(f"Name: {self.name}")
        print(f"Rank: {self.rank}")
        print(f"Number of mission: {self.mission}")
        print(f"Salary: {self.salary}")
        
naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()


# In[9]:


# Task- 09

class Programmer:
    def __init__(self, name, language, experience):
        print("Horray! A new programmer is born")
        self.name = name
        self.language = language
        self.experience = experience 
        
    def addExp(self, add_exp):
        self.add_exp = add_exp
        print(f"Updating experience of {self.name}")
        self.experience += self.add_exp
        
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Language: {self.language}")
        print(f"Experience: {self.experience}")
        
p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails() 


# In[24]:


# Task- 10

class UberEats:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"{self.name}, welcome to UberEats!")
        
    def add_items(self, food1, food2, price1, price2):
        self.food1 = food1
        self.food2 = food2
        self.price1 = price1
        self.price2 = price2
        
        self.orders = {}
        self.orders[self.food1] = self.price1
        self.orders[self.food2] = self.price2
        
        self.payment = self.price1 + self.price2
        
    def print_order_detail(self):
        return f"User detsils: Name: {self.name}, Phone: \n{self.phone}, Address: {self.address}, \nOrders: {self.orders}, \nTotal Paid Amount: {self.payment}"
        

order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())


# In[36]:


# Task- 11

class Spotify:
    def __init__(self, list):
        self.list = list
        print("Welcome to Spotify")
        
    def playing_number(self, num):
        self.num = num
        if self.num <= len(self.list):
            print("##########################")
            for i in range(1, len(self.list) + 1):
                if i == self.num:
                    return f"Playing {self.num} number song for you \nSong name: {self.list[i - 1]}"
                 
        else:
            return f"{self.num} number song not found. Your playlist \nhas {len(self.list)} songs only."
        
        
    def add_to_playlist(self, name):
        self.name = name
        self.list.append(self.name)
        
user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
print("=========================")
print(user1.playing_number(4))
user1.add_to_playlist("Dusk Till Dawn")
print(user1.playing_number(3))
print(user1.playing_number(4))


# In[1]:


# Task- 12

class Test:
    def __init__(self):
        self.sum = 0
        self.y = 0

    def methodA(self):
        x=0
        y =0
        y = y + 7
        x = y + 11
        self.sum = x + y
        print(x , y, self.sum)

    def methodB(self):
        x = 0
        self.y = self.y + 11
        x = x + 33 + self.y
        self.sum = self.sum + x + self.y
        print(x , self.y, self.sum)
        
t1 = Test()
t1.methodA()
t1.methodA()
t1.methodB()
t1.methodB()


# In[7]:


# Task- 13

class Scope:
    def __init__(self):
        self.x, self.y = 1, 100
    def met1(self):
        x = 3
        x = self.x + 1
        self.y = self.y + self.x + 1
        x = self.y + self.met2() + self.y
        print(x, self.y)
    def met2(self):
        y = 0
        print(self.x, y)
        self.x = self.x + y
        self.y = self.y + 200
        return self.x + y
    
q2 = Scope()
q2.met1()
q2.met2()
q2.met1()
q2.met2()
    


# In[3]:


# Task- 14

class Test3:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x, y = 2, 3
        msg = [0]
        msg[0] = 3
        y = self.y + msg[0]
        self.methodB(msg, msg[0])
        x = self.y + msg[0]
        self.sum = x + y + msg[0]
        print(x, y, self.sum)
    def methodB(self, mg2, mg1):
        x = 0
        self.y = self.y + mg2[0]
        x = x + 33 + mg1
        self.sum = self.sum + x + self.y
        mg2[0] = self.y + mg1
        mg1 = mg1 + x + 2
        print(x, self.y, self.sum)

t3 = Test3()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()
       


# In[6]:


# Task- 15

class Test5:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x = 0
        z = 0
        while (z < 5):
            self.y = self.y + self.sum
            x = self.y + 1
            print(x, self.y, self.sum)
            self.sum = self.sum + self.methodB(x, self.y)
            z += 1
    def methodB(self, m, n):
        x = 0
        sum = 0
        self.y = self.y + m
        x = n - 4
        sum = sum + self.y
        print(x, self.y, sum)
        return self.sum
    
t5 = Test5()
t5.methodA()


# In[ ]:




