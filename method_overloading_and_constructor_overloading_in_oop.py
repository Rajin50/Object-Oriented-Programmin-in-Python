#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task- 01

class Customer:
    def __init__(self, name):
        self.name = name

    def greet(self, name = None):
        if name == None:
            print("Hello!")
        else:
            print(f"Hello {self.name}!")

    def purchase(self, *args):
        print(f"{self.name}, you purchased {len(args)} item(s):")
        for i in args:
            print(i)

#========================================================================
customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")


# In[2]:


# Task- 02

class Panda:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
  
    def sleep(self, hrs = None):
        if hrs == None:
            return f"{self.name}'s duration is unknown thus should have only bamboo leaves"
        elif 3 <= hrs <= 5:
            return f"{self.name} sleeps {hrs} hours daily and should have Mixed Veggies"
        elif 6 <= hrs <= 8:
            return f"{self.name} sleeps {hrs} hours daily and should have Eggplant & Tofu"
        elif 9 <= hrs <= 11:
            return f"{self.name} sleeps {hrs} hours daily and should have Broccoli Chicken"

#========================================================================================================
panda1 = Panda("Kunfu","Male", 5)
panda2 = Panda("Pan Pan","Female",3)
panda3 = Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())


# In[3]:


# Task- 03

class Cat:
    def __init__(self, color = "White", activity = "sitting"):
        self.color = color 
        self.activity = activity

    def changeColor(self, new_color):
        self.color = new_color 

    def printCat(self):
        print(f"{self.color} cat is {self.activity}")

#===============================================================================
c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()


# In[4]:


# Task- 04

class Student:
    def __init__(self, name = None):
        self.name = name

    def quizcalc(self, *args):
        sum = 0
        for j in args:
            sum += j
        self.average = sum / 3

    def printdetail(self):
        if self.name == None:
            print(f"Hello default student")
        else:
            print(f"Hello {self.name}")

        print(f"Your average quiz score is {self.average}")

#========================================================================
s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()


# In[5]:


# Task- 05

class Student:
    def __init__(self, name, id, dept = "CSE"):
        self.name = name
        self.id = id
        self.dept = dept

    def dailyEffort(self, hrs):
        self.hrs = hrs

    def printDetails(self):
        print(f'Name: {self.name}')
        print(f"ID: {self.id}")
        print(f"Department: {self.dept}")
        print(f"Daily Effort: {self.hrs} hour(s)")
        if self.hrs <= 2:
            print("Suggestion: Should give more effort!")
        elif self.hrs <= 4:
            print("Suggestion: Keep up the good work!")
        else:
            print("Suggestion: Excellent! Now motivate others.")

#=================================================================================
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()


# In[6]:


# Task- 06

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    def add_Symptom(self, *args):
        self.args = args
  
    def printPatientDetail(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

        if len(self.args) == 1:
            a = self.args[0]
            print(f"Symptoms: {a}")

        elif len(self.args) == 2:
            a, b = self.args
            print(f"Symptoms: {a}, {b}")

        elif len(self.args) == 3:
            a, b, c = self.args
            print(f"Symptoms: {a}, {b}, {c}")

#===============================================================
p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()


# In[10]:


# Task- 07

class Match:
    def __init__(self, team):
        self.run = 1
        self.total_over = 0
        self.wicket = 0
        self.team = team
        self.new = self.team.split("-")
        print("5..4..3..2..1.. Play !!!")
        
    def add_run(self, addrun):
        self.run += addrun
        self.sum_run = self.run
        
    def add_over(self,over):
        self.total_over += over
        if self.total_over <= 5:
            self.addover = over
        else:
            print("Warning! Cannot add 5 over/s (5 over match)")
        self.sum_over = self.total_over

    def add_wicket(self, wicket):
        self.wicket = wicket

    def print_scoreboard(self):
        return f"Batting Team: {self.new[0]} \nBowling Team: {self.new[1]} \nTotal Runs: {self.sum_run} Wickets: {self.wicket} Overs: {self.addover}"


#===============================================================================================================================
match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())


# In[11]:


# Task- 08

class ParcelKoro:
    def __init__(self, name = None, product_weight = 0):
        self.name = name
        self.product_weight = product_weight
                      
    def calculateFee(self, location = None):
        self.location = location
        self.total_fee = (self.product_weight * 20)
        if location == None:
            self.total_fee += 50
        else:
            self.total_fee += 100
            
    def printDetails(self):
        if self.name == None:
            print("Customer Name: No name set")
        else:
            print(f"Customer Name: {self.name}")
        
        if self.product_weight == 0:
            print(f"Product Weight: {self.product_weight}")
            print("Total fee: 0")
        else:
            print(f"Product Weight: {self.product_weight}")
            print(f"Total fee: {self.total_fee}")

#==============================================================================================
print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()
                     


# In[4]:


# Task- 09

class Batsman:
    def __init__(self, *args):
        self.args = args
        if len(self.args) == 2:
            self.runs, self.balls = self.args
            print("Name: New Batsman")
        elif len(self.args) == 3:
            self.name, self.runs, self.balls = self.args
            print(f"Name: {self.name}")
            
    def battingStrikeRate(self):
        self.strike = (self.runs / self.balls) * 100
        return self.strike
        
    def setName(self, new):
        self.new = new
        print(f"Name: {self.new}")
    
    def printCareerStatistics(self):
        print(f"Run Scored: {self.runs}, Balls Faced: {self.balls}")

#======================================================================================================
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())


# In[3]:


# Task- 09

class Batsman:
    def __init__(self, *arg):
        self.arg = arg

    def printCareerStatistics(self):
        if len(self.arg) == 2:
            self.rs, self.bf = self.arg
            print(f"Name: New Batsman \nRuns Scored: {self.rs}, Balls Faced: {self.bf}")
                  
        elif len(self.arg) == 3:
            self.name, self.rs, self.bf = self.arg      
            print(f"Name: {self.name} \nRuns Scored: {self.rs}, Balls Faced: {self.bf}")

    def battingStrikeRate(self):
        return ((self.rs / self.bf) * 100)

    def setName(self, name):
        self.name = name 
        print(self.name)

#==============================================================================================================
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())


# In[4]:


# Task- 10

class EPL_Team:
    def __init__(self, team, song = "No Slogan"):
        self.team = team
        self.song = song
        self.title = 0
        
    def increaseTitle(self):
        self.title += 1
        
    def changeSong(self, new_song):
        self.song = new_song
        
    def showClubInfo(self):
        return f"Name: {self.team} \nSong: {self.song} \nTotal No of title: {self.title}"

#===========================================================================================================
manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())


# In[10]:


# Task- 11

class Author:
    def __init__(self, name=None, *books):
        self.name = name
        if name == None:
            self.name = "Default"
            
        booklist = ""
        if len(books) > 0:
            for i in books:
                booklist += i + "\n"
            self.books = booklist

    def changeName(self, new_name):
        self.name = new_name

    def addBooks(self, *books):
        booklist = ""
        for i in books:
            booklist += i + "\n"

        self.books = booklist

    def printDetails(self):
        print(f"Author Name: {self.name}")
        print("------------")
        print(f"List of Books:")
        print(self.books)

#=================================================================================================
auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print("===================")
auth2.printDetails()
print("===================")
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()


# In[26]:


# Task- 12 

class TaxiLagbe:
    def __init__(self, taxi_no, area):
        self.taxi_no = taxi_no
        self.area = area
        self.passanger = []
        
    def addPassenger(self, *args):
        for i in args:
            if len(self.passanger) >= 4:
                print("Taxi Full! No more passengers can be added.")
                break
                
            x = i.split("_")
            print(f"Dear {x[0]}! Welcome to TaxiLagbe.")
            self.passanger.append(x)
         
    def printDetails(self):
        print(f"Trip info for Taxi number: {self.taxi_no}")
        print(f"This taxi can cover only {self.area} area.")
        print(f"Total passengers: {len(self.passanger)}")
        print("Passenger lists:")
        
        if len(self.passanger) == 4:
            print(f"{self.passanger[0][0]}, {self.passanger[1][0]}, {self.passanger[2][0]}, {self.passanger[3][0]}")
            
        elif len(self.passanger) == 2:
            print(f"{self.passanger[0][0]}, {self.passanger[1][0]}")
        
        self.sum = 0
        for j in self.passanger:
            self.sum += int(j[1])
            
        print(f"Total collected fare: {self.sum} Taka")

#===========================================================================================================================
taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()
    


# In[9]:


# Task- 13

class Account:
    def __init__(self, name = "Default Account", balance = 0.0):
        self.name = name
        self.balance = balance
        
    def details(self):
        r = f"{self.name} \n{self.balance}"
        return r
    
    def withdraw(self, withdraw):
        self.remain_balance = self.balance - withdraw
        
        if self.remain_balance >= 3071:
            print(f"Withdraw successful! New balance is: {self.remain_balance}")
        else:
            print("Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.")
        
#=====================================================================================================================
a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)


# In[32]:


# Task- 14

class StudentDatabase:
    def __init__(self, name, id):
        self.name = name 
        self.id = int(id)
        self.grades = {}
        
    def calculateGPA(self, listR, session):
        courses = []
        grade = 0
        courses_dic = {}
        
        for i in range(len(listR)):
            courses_gpa = listR[i].split(": ")
            courses.append(courses_gpa[0])
            gpa = float(courses_gpa[1])
            grade += 3 * gpa
            
        result = grade / (len(courses)*3)
        courses_dic[tuple(courses)] = round(result,3)
        self.grades[session] = courses_dic
        
    def printDetails(self):
        print("Name:",self.name)
        print("ID:",self.id)
        
        for x,y in self.grades.items():
            print("Courses taken in " + x + ":")
            for i,j in y.items():
                for c in i:
                    print(c)
                print("GPA:",j)

#==============================================================================================
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()


# In[11]:


# Task- 15 (Tracing)

class FinalT6A:
    def __init__(self, x, p):
        self.temp, self.sum, self.y = 4, 0, 1
        self.temp += 1
        self.y = self.temp - p
        self.sum = self.temp + x
        print(x, self.y, self.sum)
        
    def methodA(self):
        x = 0
        y = 0
        y = y + self.y
        x = self.y + 2 + self.temp
        self.sum = x + y + self.methodB(self.temp, y)
        print(x, y, self.sum)
        
    def methodB(self, temp, n):
        x = 0
        temp += 1
        self.y = self.y + temp
        x = x + 3 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum

q1 = FinalT6A(2,1)
q1.methodA()
q1.methodA()


# In[3]:


# Task- 16 (Tracing)

class Quiz3A:
    def __init__(self, k = None):
        self.temp, self.sum, self.y = 4, 0, 0
        if k != None:
            self.temp += 1
            self.temp = self.temp
            self.sum = self.temp + k
            self.y = self.sum - 1
        else:
            self.y = self.temp - 1
            self.sum = self.temp + 1
            self.temp += 2
    def methodB(self, m, n):
        x = 0
        self.temp += 1
        self.y = self.y + m + (self.temp)
        x = x + 2 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum

a1 = Quiz3A()
a1.methodB(1,2)
a2 = Quiz3A(3)
a2.methodB(2,4)
a1.methodB(2,1)
a2.methodB(1,3)


# In[4]:


# Task- 17 (Tracing)

class Test5:
    def __init__(self):
        self.sum = 0
        self.y = 0
    def methodA(self):
        x=y=k=0
        msg = [5]
        while (k < 2):
            y += msg[0]
            x = y + self.methodB(msg, k)
            self.sum = x + y + msg[0]
            print(x ," " , y, " " , self.sum)
            k+=1
    def methodB(self, mg2, mg1):
        x = 0
        self.y += mg2[0]
        x = x + 3 + mg1
        self.sum += x + self.y
        mg2[0] = self.y + mg1
        mg1 += x + 2
        print(x , " " ,self.y, " " , self.sum)
        return mg1
    
t1 = Test5()
t1.methodA()
t1.methodA()
t1.methodA()


# In[5]:


# Task- 18 (Tracing)

class Test4:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x, y = 0, 0
        msg = [0]
        msg[0] = 5
        y = y + self.methodB(msg[0])
        x = y + self.methodB(msg, msg[0])
        self.sum = x + y + msg[0]
        print(x, y, self.sum)
    def methodB(self, *args):
        if len(args) == 1:
            mg1 = args[0]
            x, y = 0, 0
            y = y + mg1
            x = x + 33 + mg1
            self.sum = self.sum + x + y
            self.y = mg1 + x + 2
            print(x, y, self.sum)
            return y
        else:
            mg2, mg1 = args
            x = 0
            self.y = self.y + mg2[0]
            x = x + 33 + mg1
            self.sum = self.sum + x + self.y
            mg2[0] = self.y + mg1
            mg1 = mg1 + x + 2
            print(x, self.y, self.sum)
            return self.sum

t3 = Test4()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()


# In[6]:


# Task- 19 (Tracing)

class msgClass:
    def __init__(self):
        self.content = 0
class Q5:
    def __init__(self):
        self.sum = 1
        self.x = 2
        self.y = 3
        
    def methodA(self):
        x, y = 1, 1
        msg = []
        myMsg = msgClass()
        myMsg.content = self.x
        msg.append(myMsg)
        msg[0].content = self.y + myMsg.content
        self.y = self.y + self.methodB(msg[0])
        y = self.methodB(msg[0]) + self.y
        x = y + self.methodB(msg[0], msg)
        self.sum = x + y + msg[0].content
        print(x," ", y," ", self.sum)
        
    def methodB(self, mg1, mg2 = None):
        if mg2 == None:
            x, y = 5, 6
            y = self.sum + mg1.content
            self.y = y + mg1.content
            x = self.x + 7 +mg1.content
            self.sum = self.sum + x + y
            self.x = mg1.content + x +8
            print(x, " ", y," ", self.sum)
            return y
        
        else:
            x = 1
            self.y += mg2[0].content
            mg2[0].content = self.y + mg1.content
            x = x + 4 + mg1.content
            self.sum += x + self.y
            mg1.content = self.sum - mg2[0].content
            print(self.x, " ",self.y," ", self.sum)
            return self.sum

q = Q5()
q.methodA()


# In[ ]:




