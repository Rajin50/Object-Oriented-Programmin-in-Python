#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task- 01

class DataType:
    def __init__(self, name, value):
        self.name = name
        self.value = value

#==================================================        
data_type1 = DataType("Integer", 1234)
print(data_type1.name)
print(data_type1.value)
print('=====================')
data_type2 = DataType("String", "Hello")
print(data_type2.name)
print(data_type2.value)
print('=====================')
data_type3 = DataType("Float", 4.0)
print(data_type3.name)
print(data_type3.value)


# In[2]:


# Task- 02
class Flower:
    def __init__(self):
        pass

#=================================================================
flower1 = Flower()
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print("=====================")
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)

# Subtask- 2, 3

if flower1 == flower2:
    print("they are same")
else:
    print("they are different")


# In[3]:


# Task- 03

class Joker:
    def __init__(self, name, power, is_he_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he_psycho

#=====================================================================
j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")

if j1 == j2:
    print('same')
else:
    print('different')
    
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')

print("=====================")

# Subtask- 2, 3

print("j1 is a location & j2 is another location. Both objects location are not same. That's why 1st if/else block have printed different.")
print("j1.name and j2.name, both instance variables are staying in two different location. But both contains same string. That's why 2nd if/else block have printed same.")


# In[4]:


# Task- 04

class Pokemon:
    def __init__(self, pokemon1_name, pokemon2_name, pokemon1_power, pokemon2_power, damage_rate):
        self.pokemon1_name = pokemon1_name
        self.pokemon2_name = pokemon2_name
        self.pokemon1_power = pokemon1_power
        self.pokemon2_power = pokemon2_power
        self.damage_rate = damage_rate

#=======================================================================================================
team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name,
team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name,
team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power +
team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)

# Subtask- 2, 3
team_bulb = Pokemon('bulbasaur', 'squirtle', 80, 70, 9)
print('=======Team 2=======')
print('Pokemon 1:',team_bulb.pokemon1_name,
team_bulb.pokemon1_power)
print('Pokemon 2:',team_bulb.pokemon2_name,
team_bulb.pokemon2_power)
bulb_combined_power = (team_bulb.pokemon1_power +
team_bulb.pokemon2_power) * team_bulb.damage_rate
print('Combined Power:', bulb_combined_power)


# In[5]:


# Task- 05

class Player:
    def __init__(self):
        pass

#=================================================================
player1 = Player()
player1.name = "Ronaldo"
player1.jersy_number = 9
player1.position = "Striker"
print("Name of the Player:", player1.name)
print("Jersey Number of player:", player1.jersy_number)
print("Position of player:", player1.position)
print("===========================")
player2 = Player()
player2.name = "Neuer"
player2.jersy_number = 1
player2.position = "Goal Keeper"
print("Name of the player:", player2.name)
print("Jersey Number of player:", player2.jersy_number)
print("Position of player:", player2.position)


# In[6]:


# Task- 06

class Country:
    def __init__(self, name = "Bangladesh", continent = "Asia", capital = "Dhaka", fifa_ranking = 187):
        self.name = name
        self.continent = continent
        self.capital = capital
        self.fifa_ranking = fifa_ranking

#=========================================================================================
country = Country()
print('Name:',country.name)
print('Continent:',country.continent)
print('Capital:',country.capital)
print('Fifa Ranking:',country.fifa_ranking)
print('===================')
country.name = "Belgium"
country.continent = "Europe"
country.capital = "Brussels"
country.fifa_ranking = 1
print('Name:',country.name)
print('Continent:',country.continent)
print('Capital:',country.capital)
print('Fifa Ranking:',country.fifa_ranking)


# In[7]:


# Task- 07

class DemonSlayer:
    def __init__(self, name, style, number_of_technique, kill):
        self.name = name
        self.style = style
        self.number_of_technique = number_of_technique
        self.kill = kill 

#=================================================================================================
tanjiro = DemonSlayer("Tanjiro", "Water Breathing", 10, 10)
print('Name:',tanjiro.name)
print('Fighting Style:',tanjiro.style)
print(f'Knows {tanjiro.number_of_technique} technique(s) and has killed {tanjiro.kill} demon(s)')
print('===================')
zenitsu = DemonSlayer("Zenitsu", "Thunder Breathing", 1, 4)
print('Name:',zenitsu.name)
print('Fighting Style:',zenitsu.style)
print(f'Knows {zenitsu.number_of_technique} technique(s) and has killed {zenitsu.kill} demon(s)')
print('===================')
inosuke = DemonSlayer("Inosuke", "Beast Breathing", 5, 7)
print('Name:',inosuke.name)
print('Fighting Style:',inosuke.style)
print(f'Knows {inosuke.number_of_technique} technique(s) and has killed {inosuke.kill} demon(s)')
print('===================')
print(f'{tanjiro.name}, {zenitsu.name}, {inosuke.name} knows total {tanjiro.number_of_technique + zenitsu.number_of_technique + inosuke.number_of_technique} techniques')
print(f'They have killed total {tanjiro.kill + zenitsu.kill + inosuke.kill} demons')


# In[3]:


# Task- 08

class box:
    def __init__(self, args):
        self.height = args[0]
        self.width = args[1]
        self.breadth = args[2]
        print("Creating a Box!")
        print(f"Volume of the box is {self.height * self.width * self.breadth} cubic units.")
        
#==================================================================================================        
print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)


# In[1]:


# Task- 09

class buttons:
    def __init__(self, word, spaces, border):
        self.word = word
        self.spaces = spaces
        self.border = border

        print(f"{self.word} Button Specifications:")
        print(f"Button name: {self.word}")
        
        y = 2 + (2 * self.spaces) + len(self.word)
        
        print(f"Number of the border characters for the top and the bottom: {y}")
        print(f"Number of spaces between the left side border and the first character of the button name: {self.spaces}")
        print(f"Number of spaces between the right side border and the last character of the button name: {self.spaces}")
        print(f"Characters representing the borders: {self.border}")
        print()
        
        line1 = self.border * y
        line2 = self.border + " " * self.spaces + self.word + " " * self.spaces + self.border
        
        print(line1)
        print(line2)
        print(line1)


#===========================================================================================================================
word = "CANCEL"  
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')


# In[6]:


# Task- 10

class Wadiya():
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True

# Subtask- 1, 2, 3, 4        
wadiya = Wadiya()
print("Part 1:")
print(f"Name of President: {wadiya.name}")
print(f"Designation: {wadiya.designation}")
print(f"Number of wife: {wadiya.num_of_wife}")
print(f"Is he/she a dictator: {wadiya.dictator}")

#=========================================================================================
print("Part 2:")
wadiya.name = "Donald Trump"
wadiya.designation = "President"
wadiya.num_of_wife = 1
wadiya.dictator = False
print(f"Name of President: {wadiya.name}")
print(f"Designation: {wadiya.designation}")
print(f"Number of wife: {wadiya.num_of_wife}")
print(f"Is he/she a dictator: {wadiya.dictator}")


# In[8]:


# Task- 11

class Human: 
    def __init__(self):
        self.age = 0
        self.height = 0.0
        
        
#========================================
h1 = Human()
h2 = Human()
h1.age = 21
h1.height = 5.5
print(h1.age)
print(h1.height)
h2.height = h1.height - 3
print(h2.height)
h2.age = h1.age
h1.age += h1.age
print(h1.age)
h2 = h1
print(h2.age)
print(h2.height)
h1.age += h1.age
h2.height += h2.height
print(h1.age)
print(h1.height)
h2.age += h2.age
h1.age = h2.age
print(h2.age)


# In[11]:


# Task- 12

class Student: 
    def __init__(self):
        self.name = None
        self.cgpa = 0.0

#==================================================
s1 = Student()
s2 = Student()
s3 = None
s1.name = "Student One"
s1.cgpa = 2.3
s3 = s1
s2.name = "Student Two"
s2.cgpa = s3.cgpa + 1
s3.name = "New Student"
print(s1.name)
print(s2.name)
print(s3.name)
print(s1.cgpa)
print(s2.cgpa)
print(s3.cgpa)
s3 = s2
s1.name = "old student"
s2.name = "older student"
s3.name = "oldest student"
s2.cgpa = s1.cgpa - s3.cgpa + 4.5
print(s1.name)
print(s2.name)
print(s3.name)
print(s1.cgpa)
print(s2.cgpa)
print(s3.cgpa)


# In[12]:


# Task- 13

class Ninja: 
    def __init__(self):
        self.rank = 0
        self.stamina = 0.0

#===================================================
naruto = Ninja()
yellow_flash = Ninja()
naruto.rank = 1
naruto.stamina = 95.0
print(naruto.rank)
print(naruto.stamina)
yellow_flash.stamina = naruto.stamina - 2
print(yellow_flash.stamina)
yellow_flash.rank += (naruto.rank + 1)
print(yellow_flash.rank)
minato = yellow_flash
print(minato.rank)
print(minato.stamina)
naruto.rank = minato.rank - 1
naruto.stamina = yellow_flash.stamina + 3
print(naruto.rank)
print(naruto.stamina)
naruto.rank = -(-naruto.rank)
yellow_flash.stamina = -(-minato.stamina)
print(naruto.rank)
print(minato.stamina)

