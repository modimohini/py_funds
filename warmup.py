"""

s = "Hello World Hello World "
s = s.replace("Hello","Universe")
v = s.replace("World", "HI")
print(s) 
print(v)


s = "That I ever did see. Dusty as the handle on the door"
index = s.find("Dusty")
p = s.find("I")
print(index) 
print(p)

#find a word 
s = "That I ever did see. Dusty as the handle on the door"

if "Dusty" in s:
    print("query found")
count = 0
if "the" in s:
    count += 1
    print(str(count) + " found it!")



# define strings                                                         
firstname = "Bugs"
lastname = "Bunny"

# define our sequence                                                    
sequence = (firstname,lastname)
seq = (lastname, firstname)
# join into new string                                                   
name = " ".join(sequence)
print(name)

newseq = " ".join(seq)

words = ["How","are","you","doing","?"]
sentence = ' '.join(words)
print(sentence)

index = sentence.find("u")
print(index) 

s = "Its to easy"
words = s.split()
print(words)

print(len(words))
print(len(s))

word = "Easy"
x = list(word)
print(x)



import random

# Create a random floating point number and print it.
print(random.random())

# pick a random whole number between 0 and 10.
print(random.randrange(0,10))

# pick a random floating point number between 0 and 10.
print(random.uniform(1,10))


name = input('What is your name? ')
print('Hello ' + name)

job = input('What is your job? ')
print('Your job is ' + job)

num = int(input('Give me a number? '))
print('You said: ' + str(num))


#### Control structures
x = 4
if x < 5:
    print("x is smaller than five")
    print("this means it's not equal to five either")
    print("x is an integer")


#
gender = input("Gender? ")
gender = gender.lower()
if gender == "male":
    print("Your cat is male")
elif gender == "female":
    print("Your cat is female")
else:
    print("Invalid input")

age = int(input("Age of your cat? "))
if age < 5:
    print("Your cat is young.")
else:
    print("Your cat is adult.")



# for 
city = ['Tokyo','New York','Toronto','Hong Kong']
print('Cities loop:')
for x in city:
    print('City: ' + x)

print('\n')  # newline

num = [1,2,3,4,5,6,7,8,9]
print('x^2 loop:')
for x in num:
    y = x * x
    print(str(x) + ' * ' + str(x) + ' = ' + str(y))


# while
x = 7                              
while x < 10:
    print(x)
    x = x + 1


def currentYear():
    print('2018')

currentYear()

#Functions with parameters
def f(x,y):
    return x*y

print(f(3,4))


# list 
list = [ "New York", "Los Angles", "Boston", "Denver" ]

print(list)     # prints all elements
print(list[0])  # print first element

list2 = [1,3,4,6,4,7,8,2,3]

print(sum(list2))
print(min(list2))
print(max(list2))
print(list2[0])
print(list2[-1])


#List operations append pop
x = [3,4,5]
x.append(6)
print(x)
x.append(7)
print(x)
x.pop()
print(x)
x.pop()
print(x)

"""
# list sort 
x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
print(x)

words = ["Be","Car","Always","Door","Eat" ]
words.sort()
print(words)

# reverse order
x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
x = list(reversed(x))
print(x)


# Best way to sort in reverse order
words = ["Be","Car","Always","Door","Eat" ]
words = words[::-1]
print(words)


# range(start, stop, step)
# range(stop)

x = list(range(100))
print(x)

x = list(range(1,11))
print(x)

for i in range(1,11):
   print(i)

for i in range(0,25,5):
   print(i)



#Dictionary
words = {}
words["BMP"] = "Bitmap"
words["BTW"] = "By The Way"
words["BRB"] = "Be Right Back"

print (words["BMP"])
print (words["BRB"])


myfile = open("/Users/MohiniM/Desktop/Desktop/Mohini/PR/GitStuff/day1/py_funds/Lorem.txt","rt")
contents = myfile.read()
myfile.close()
print(contents)


filename = "/Users/MohiniM/Desktop/Desktop/Mohini/PR/GitStuff/day1/py_funds/Lorem.txt"
with open(filename) as f:
    content = f.readlines()
print(content)

infile = open(filename, 'r')
data = infile.read()
infile.close()
print(data)


#!/usr/bin/env python

# create and open file
f = open("test.txt","w")

# write data to file 
f.write("Hello World, \n")
f.write("This data will be written to the file.")

# close file
f.close()

#!/usr/bin/env python

# create and open file
f = open("test.txt","a")

# write data to file 
f.write("Don't delete existing data \n")
f.write("Add this to the existing file. some more")

# close file
f.close()

filename = "test.txt"
with open(filename) as f:
    content = f.readlines()
print(content)


# nested  Loop
#!/usr/bin/python

persons = [ "John", "Marissa", "Pete", "Dayton" ]
restaurants = [ "Japanese", "American", "Mexican", "French" ]

for person in persons:
    for restaurant in restaurants:
        print(person + " eats " + restaurant)
#Print the following pattern

for x in range(6):
    for y in range(x):
        print('*'+ str(x), end=" ")
    print("\n")


#  Slice Lists/Arrays
persons = [ "John", "Marissa", "Pete", "Dayton" ]

slice = persons[0:2]
print(slice)

#String slicing
destination = "summer holiday at beach"
mySlice = destination[0:6]
print(mySlice)


# multiple return 
def getPerson():
    name = "Leona"
    age = 35
    country = "UK"
    return name,age,country

name,age,country = getPerson()
print(name)
print(age)
print(country)



#  A global variable 
balance = 0

def addAmount(x):
    global balance
    balance = balance + x

addAmount(5)
print(balance)

import time

print("Hello")
time.sleep(1)
print("World")
time.sleep(1)



import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in: Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
y = re.search("ai", txt)
print(y)


# number divisible by 4 print link, numb div by 6 print in, num div by 4 & 6 print linkin

x = list(range(1,101))


def likedin():
    for i in x:
        if i % 4:
            print("Link " + str(i))
        elif i % 6:
            print("in" + str(i))
        elif i % 4 == i % 6:
            print("linkedin " + str(i))
        else:
            print(i)
likedin()

from typing import Dict



# python comprehension

def old_data(data_list):
    temp = []
    for dataa in data_list:
        temp.append(dataa//2*67 - 5)
    return temp

def new_data(data_list):
    return [dataa//2*67 - 5 for dataa in data_list]

if __name__ == "__main__":
    data_list = [0, 5, 10, 3]
    print(new_data(data_list) == old_data(data_list))
"""

# Dictionary

_dict = {1: 'name', 2: [4,5,6], 'animal' : 'dog'}
print(_dict)
print(_dict[2])
print(_dict['animal'])

""" # Creating a Dictionary with dict method 
Dict = dict({'emp1': {1: 'Ges'},
        'emp2': {'Name': 'Forg'}
        })

Dict[0] = 'jerry'
Dict[2] = 'tom', 2, 5, 6 # adding set of values 
print(Dict)

# adidng nested values 
Dict[0] = 'hello' 

print("updating value: ")
print (Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life'}}
print("\nAdding a Nested Key: ")
print(Dict)

print(Dict.get(5), Dict.get("emp1"))

# deleting a key using pop() method 
popp = Dict.pop(2)
print('\n dict after deleting: ' + str(popp) + '\n' + str(Dict))

print("\n after pop")
poppy = Dict.popitem()
print(Dict)
Dict.clear()
print (Dict)

import sys
file_path = 'randomfile.txt'
sys.stdout = open(file_path, "w")
print("This text will be added to the file")