#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Task- 01 (String)

user_input = input()

upper_case = 0
lower_case = 0
for letter in user_input:
    if ord("A") <= ord(letter) <= ord("Z"):
        upper_case += 1
    elif ord("a") <= ord(letter) <= ord("z"):
        lower_case += 1

if upper_case > lower_case:
    print(user_input.upper())

elif lower_case >= upper_case:
    print(user_input.lower())
        
    


# In[3]:


# Task- 02 (String)

user_input = input()

is_alpha = False
is_num = False
digit = "0123456789"

for elements in user_input:
    if elements in digit:
        is_num = True
    elif ord("A") <= ord(elements) <= ord("Z") or ord("a") <= ord(elements) <= ord("z"):
        is_alpha = True

if is_num == True and is_alpha == False:
    print("NUMBER")
    
if is_alpha == True and is_num == False:
    print("WORD")
    
if is_num == True and is_alpha == True:
    print("MIXED")


# In[1]:


# Task- 03 (String)

user_input = input()

upper_case = ""
for letter in user_input:
    if ord("A") <= ord(letter) <= ord("Z"):
        upper_case += letter
        
p = user_input.index(upper_case[0])
q = user_input.index(upper_case[1])

if q - p == 1:
    print("BLANK")
    
else:
    print(user_input[p + 1 : q])


# In[3]:


# Task- 04 (String)

user_input = input()

word_list = user_input.split(", ")

output = ""
for i in word_list[0]:
    if i in word_list[1]:
        output += i

for j in word_list[1]:
    if j in word_list[0]:
        output += j

if output == "":
    print("Nothing is common")
    
else:
    print(output)


# In[6]:


# Task- 05 (String)

user_input = input()

is_upper = False
is_lower = False
is_num = False
is_sp = False
digit = "0123456789"
special_character = "_$#@"

for character in user_input:
    if character in digit:
        is_num = True
    elif ord("A") <= ord(character) <= ord("Z"):
        is_upper = True
    elif ord("a") <= ord(character) <= ord("z"):
        is_lower = True
    elif character in special_character:
        is_sp = True
        
if is_upper == True and is_lower == True and is_num == True and is_sp == True:
    print("OK")
    
if is_upper == False and is_lower == True and is_num == False and is_sp == False:
    print("Uppercase character missing, Digit missing, Special character missing")
    
if is_upper == True and is_lower == True and is_num == False and is_sp == True:
    print("Digit missing")


# In[7]:


# Task- 01 (List)

my_list = []

while True:
    user_input = input()
    if user_input == "STOP":
        break
    else:
        my_list.append(user_input)

i = 0
new_list = []

while i < len(my_list):
    if my_list[i] not in new_list:
        print(my_list[i], "-", my_list.count(my_list[i]), "times")
  
    new_list.append(my_list[i])
    i += 1


# In[3]:


# Task- 02 (List)

user_input = int(input())
final_list = []

for i in range(user_input):
    List = [int(elements) for elements in input().split(" ")]
    
    if len(List) != 3:
        print("There're not three integer")
        
    else:
        for idx in range(3):
            if len(final_list) == 0:
                final_list = List
                
            elif List[idx] > final_list[idx]:
                final_list[idx] = List[idx]
                
Aggregate = 0
for num in final_list:
    Aggregate += num

print(Aggregate)
print(final_list)
        


# In[1]:


# Task- 03 (List)

List = [elements for elements in input().split(" ")]

Inequality = False
end = "STOP"

while end not in List:
    for idx in range(len(List) - 1):
        if abs(int(List[idx]) - int(List[idx + 1])) > (len(List) - 1):
            Inequality = True
            break
            
        else:
            continue
    
    #print("Not UB Jumper") if Inequality else print("UB Jumper")
    
    if Inequality == True:
        print("Not UB Jumper")
        
    else:
        print("UB Jumper")
        
    List = [elements for elements in input().split(" ")]


# In[4]:


# Task- 04 (List)

n, k = map(int, input().split(" "))
num_of_times = [int(elements) for elements in input().split(" ")]

list = []

for times in num_of_times:
    if times + k <= 5:
        list.append(times)
        
team = len(list) // 3
print(team)


# In[7]:


# Task- 01 (Function)

def AmiKenoMota(Height, Weight):
    BMI = Weight / Height ** 2
    
    
    if BMI < 18.5:
        x = "Underweight"
        
    elif 18.5 <= BMI <= 24.9:
        x = "Normal"
        
    elif 25 <= BMI <= 30:
        x = "Overweight"
        
    elif BMI > 30:
        x= "Obese"
        
    return x, BMI

user_input = input()

sliced = user_input[1 : len(user_input)-1]
p = sliced.split(", ")
height = int(p[0]) / 100 
weight = int(p[1])

function = AmiKenoMota(height, weight)

condition, score = function
s = round(score, 1)

print(f"Score is {s}. You are {condition}")


# In[9]:


# Task- 02 (Function)

def sum_of_num(a, b, d):
    sum = 0
    for i in range(a, b):
        if i % d == 0:
            sum += i
    return sum

user_input = eval(input())
maximum, minimum, divisor = user_input

function = sum_of_num(maximum, minimum, divisor)
print(function)


# In[12]:


# Task- 03 (Function)

def total_price(Burger, Place = "Mohakhali"):
    Menu = {"BBQ Chicken Cheese Burger": 250, "Beef Burger": 170, "Naga Drums": 200}
    
    Total_price = 0
    meal_cost = 0
    
    if Burger in Menu.keys():
        meal_cost += Menu[Burger]
    Total_price += meal_cost
    
    if Place != "Mohakhali":
        Total_price += 60 
    elif Place == "Mohakhali":
        Total_price += 40
    
    tax = meal_cost * 0.08
    Total_price += tax
    
    return Total_price

user_input = eval(input())

if len(user_input) == 2:
    food, location = user_input
    function = total_price(food, location)
    
else:
    food = user_input
    function = total_price(food)

print(function)
        
    
    


# In[4]:


# Task- 04 (Function)

def replace_domain(email, n_domain, o_domain = "kaaj.com"):
    if n_domain in email:
        x = "Unchanged: " + email
        
    else:
        parts = email.split("@")
        parts[1] = n_domain
        x = "Changed: " + parts[0] + "@" + parts[1]
        
    return x

function = replace_domain("rajin@sheba.xyz", "sheba.xyz")
print(function)


# In[14]:


# Task- 05 (Function)

def palindrome_checker(string):
    
    if " " in string:
        
        s = string.split(" ")
        word = ""
        for i in s:
            word += i
        
        if word[0 : ] == word[-1 : : -1]:
            x = "Palindrome"
    
    elif string[0 : ] == string[-1 : : -1]:
        x = "Palindrome"
        
    else:
        x = "Not a palindrome"
        
    return x

user_input = input()
function = palindrome_checker(user_input)

print(function)


# In[20]:


# Task- 06 (Function)

def capitalizes(string):
    correction = string[0].upper() + string[1]
    
    for idx in range(2, len(string) - 1):
        if string[idx - 2] in ".!?" and string[idx - 1] == " ":
            correction += string[idx].upper()
        elif string[idx - 1] == " " and string[idx + 1] == "  " and string[idx] == "i":
            correction += string[idx].upper()
        else:
            correction += string[idx]
            
    correction += string[-1]
    
    return correction

user_input = capitalizes(input())
print(user_input)


# In[16]:


# Task- 01 (Dictionary & Tuple)

def dict_converter(string):
    dict41 = {}
    list_a = string.split(", ")
    num = "0123456789"

    for i in list_a:
        list_b = i.split(": ")
        
        if num in list_b:
            dict41[list_b[0]] = int(list_b[1])
        else:
            dict41[list_b[0]] = int(list_b[1])
            
    return dict41

dict_1 = dict_converter(input())
dict_2 = dict_converter(input())

dict51 = {}
for i in dict_1:
    for j in dict_2:
        if i == j:
            sum = dict_1[i] + dict_2[j]
            dict51[i] = sum
        if j not in dict51:
            dict51[j] = dict_2.get(j)
        if i not in dict51:
            dict51[i] = dict_1.get(i)

print(dict51)

list = []
for values in dict51.values():
    if values not in list:
        list.append(values)
        
print("Values:", tuple(sorted(list)))
    
            


# In[23]:


# Task- 02 (Dictionary & Tuple)

list_a = []
list_b = []
dict99 = {}

while 'STOP' not in list_a:
    list_a.append(input())

for elements in (list_a):
    counter = list_a.count(elements)
    dict99[elements] = counter
    
    if elements == 'STOP':
        pass
    
    else:
        if elements not in list_b:
            print(elements, '-', dict99[elements], 'times')
            list_b.append(elements)


# In[26]:


# Task- 03 (Dictionary & Tuple)

def making_dict(a1):
    dict101 = {}
    
    splited = a1.split(", ")
    
    for i in range(len(splited)):
        splited_pro = splited[i].split(" : ")
        dict101[splited_pro[0]] = splited_pro[1]
        
    return dict101

dictionary = making_dict(input())

output = {}
for key, value in dictionary.items():
    if value not in output.keys():
        output[value] = [key]
    else :
        output[value].append(key)
        
print(output)


# In[3]:


# Task- 04 (Dictionary & Tuple)

dictionary = {1: ".,?!:", 2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL", 6: "MNO", 7: "PQRS", 8: "TUV", 9: "WXYZ", 0: " "}

user_input = input().upper()

presses = ""
for character in user_input:
    for key in dictionary:
        if character in dictionary[key]:
            position = dictionary[key].index(character) + 1
            presses += str(key) * position

print(presses)

