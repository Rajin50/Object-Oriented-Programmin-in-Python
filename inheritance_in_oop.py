#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task- 01

class Student:
    def __init__(self, name='Just a student', dept='nothing'):
        self.__name = name
        self.__department = dept
        
    def set_department(self, dept):
        self.__department = dept
        
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
        
    def __str__(self):
        return 'Name: '+self.__name+' Department: '+self.__department

class BBA_Student(Student):
    def __init__(self, name = "default", dept = "BBA"):
        super().__init__(name, dept)

#==========================================================================================
print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))


# In[2]:


# Task- 02

class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def moveUp(self):
        self.y+=1
        
    def moveDown(self):
        self.y-=1
        
    def moveRight(self):
        self.x+=1
        
    def moveLeft(self):
        self.x-=1
        
    def __str__(self):
        return '('+str(self.x)+' , '+str(self.y)+')'

class Vehicle2010(Vehicle):
    def moveUpperLeft(self):
        super().moveLeft()
        super().moveUp()

    def moveUpperRight(self):
        super().moveRight()
        super().moveUp()

    def moveLowerRight(self):
        super().moveRight()
        super().moveDown()

    def moveLowerLeft(self):
        super().moveLeft()
        super().moveDown()
    
    def equals(self, other):
        return self.x == other.x and self.y == other.y

#===========================================================================
print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))


# In[3]:


# Task- 03

class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
        
    def set_name(self,name):
        self.__name = name
        
    def get_name(self):
        return self.__name


class Cricket_Tournament(Tournament):
    def __init__(self, name = "Default", num_of_team = 0, type = "No type"):
        super().__init__(name)
        self.num_of_team = num_of_team
        self.type = type

    def detail(self):
        return f"Cricket Tournament Name: {self.get_name()} \nNumber of Teams: {self.num_of_team} \nType: {self.type}"


class Tennis_Tournament(Tournament):
    def __init__(self, name, players):
        super().__init__(name)
        self.players = players 

    def detail(self):
        return f"Tennis Tournament Name: {self.get_name()} \nNumber of Players: {self.players}"

#===============================================================================================================================
ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())


# In[4]:


# Task- 04

class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price
        
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+" Price: "+str(self.__price)

class Book(Product):
    def __init__(self, id, title, price, isbn, publisher):
        super().__init__(id, title, price)
        self.isbn = isbn
        self.publisher = publisher

    def printDetail(self):
        return f"{self.get_id_title_price()} \nISBN: {self.isbn} Publisher: {self.publisher}"

class CD(Product):
    def __init__(self, id, title, price, band, duration, genre):
        super().__init__(id, title, price)
        self.band = band
        self.duration = duration
        self.genre = genre 
    
    def printDetail(self):
        return f"{self.get_id_title_price()} \nBand: {self.band} Duration: {self.duration}minutes \nGenre: {self.genre}"

#============================================================================================================================
book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())


# In[5]:


# Task- 05

class Animal:
    def __init__(self,sound):
        self.__sound = sound

    def makeSound(self):
        return self.__sound

class Printer:
    def printSound(self, a):
        print(a.makeSound())

class Dog(Animal, Printer):
    def __init__(self, sound):
        super().__init__(sound)

class Cat(Animal, Printer):
    def __init__(self, sound):
        super().__init__(sound)

#================================================================
d1 = Dog('bark')
c1 = Cat('meow')
a1 = Animal('Animal does not make sound')
pr = Printer()
pr.printSound(a1)
pr.printSound(c1)
pr.printSound(d1)


# In[6]:


# Task- 06

class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base
        
    def get_height_base(self):
        return "Height: "+str(self.height)+", Base: "+str(self.base)

class triangle(Shape):
    def __init__(self, name = "Default", height = 0, base = 0):
        super().__init__(name, height, base)

    def calcArea(self):
        self.area = 0.5 * self.base * self.height

    def printDetail(self):
        return f"Shape name: {self.name} \n{self.get_height_base()} \nArea: {self.area}"

class trapezoid(Shape):
    def __init__(self, name, height, base, side):
        self.side = side
        super().__init__(name, height, base)

    def calcArea(self):
        self.area = ((self.base + self.side) / 2) * self.height

    def printDetail(self):
        return f"Shape name: {self.name} \n{self.get_height_base()}, Side_A: {self.side}\nArea: {self.area}"

#======================================================================================================================
tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())


# In[7]:


# Task- 07

class Football:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0

    def get_name_team(self):
        return 'Name: '+self.__name+', Team Name: ' +self.__team

class Player(Football):
    def __init__(self, team_name, name, role, goal, total_played):
        self.goal = goal
        self.total_played = total_played
        super().__init__(team_name, name, role)

    def calculate_ratio(self):
        self.goal_ratio = self.goal / self.total_played

    def print_details(self):
        print(f"{self.get_name_team()} \nTeam Role: {self.role} \nTotal Goal: {self.goal}, Total Played: {self.total_played} \nGoal Ratio: {self.goal / self.total_played} \nMatch Earning: {(self.goal * 1000) + (self.total_played * 10)}K")

class Manager(Football):
    def __init__(self, team_name, name, role, total_win):
        self.total_win = total_win
        super().__init__(team_name, name, role)

    def print_details(self):
        print(f"{self.get_name_team()} \nTeam Role: {self.role} \nTotal Win: {self.total_win} \nMatch Earning: {self.total_win * 1000}K")

#============================================================================================================================================
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
