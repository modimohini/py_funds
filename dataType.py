""" L = [1, "a" , "stringss" , 1+2]
print (L)
L.append(88)
print (L)
L.pop(-2)
print (L)
print (L[2])

#1: Iteration by for loop on list/string
for i in L:
    print(i)

#2: Iteration by while loop for a condition
k = 1
while (k < 5):
    print(k)
    k += 1

#3:Iteration by for loop for range
for i in range(0, 4):
    print (i) """

""" def wnw(n):
    for n in range (1,110):
        if n % 2:
            print(str(n) + " Weird")
        elif n in range(2,5):
            print(str(n) + " Not Weird")
        elif n in range(6,19):
            print(str(n) + " Weird")
        elif n in range(20,101):
            print('Not Weird')

user_input = int(input("int: "))
wnw(user_input) """

""" def nf(n):
    for i in range(0,n):
        print(i)

user_input = int(input("int: "))
nf(user_input) """

""" def swap_case(s):
    st = s.swapcase() 
    print(st)
    return

if __name__ == '__main__':
    someStr = "GinJon"
    swap_case(someStr) """

""" def swap_case(s):
    r = (s.swapcase()) 
    print(r)
    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result) """


# Super helpful to check for any digit in the string will be true/false
""" def st(s):
    res = any(i.isalnum() for i in s)
    r = any(i.isalpha() for i in s)
    re = any(i.isdigit() for i in s)
    rl = any(i.islower() for i in s)
    ru = any(i.isupper() for i in s)
    print(res)
    print(r)
    print(re)
    print(rl)
    print(ru)

if __name__ == '__main__':
    s = input()
    st(s)
   """

""" def unq(d):
    a = set(d)
    print(len(d))
    print(len(a))
    print(a)

da = ('UK','China','USA','France','New Zealand','UK','France','UK','France')
unq(da) """

""" # unique names

n = int(input("No of names: "))
a = []
for i in range(n):
    a.append(input("list " + str(n) + " names: "))
s = set(a)
print(len(s)) """

""" def split_and_join(line):
    # write your code here
    s = line.split(" ")
    j = "-".join(s)
    print(j)

if __name__ == '__main__':
    line = input()
    r = split_and_join(line)
    print(r) """


""" def fnrun(a):
    print(a)
    hr = a.sort()
    print(hr[-1]) """

""" # find the 2nd runner up for the score: 
if __name__ == '__main__':
    n = int(input("No of score: "))
    arr = []
    for i in range(n):
        arr.append(input("list " + str(n-1) + " score: "))
        
    print(arr)
    s = set(arr)
    print(s)
    r = list(s)
    r.sort()
    print(r)
    print(r[-2]) """

""" ##### ARRAYS ######
# append(), insert(i,x) --> insert value x at i'th position 
import array

arr = [1, 2, 2, 2, 3]
print(arr)
for i in range(len(arr)):
    print(arr[i], end = " ")
print("\r")
arr.append(4)
print(arr)
arr.insert(1,500)
print(arr)

# pop(), remove()
print(arr.pop(4)) # pop value can be printed 
print(arr)
print(arr.remove(500)) # no value to show --> None
print(arr)

# index(), reverse()
print(arr.index(2)) # index(x) will print index of 1'st occurance of value 'x'
arr.reverse()
print(arr)

# typecode --> datatype, itemsize --> size of single array element, buffer_info() --> addr in which array is stored and number of elements
arr1= array.array('i',[19, 229, 31, 31, 25, 9999, 31, 888888888]) 
print(arr1.typecode)
print(arr1.itemsize)
print(arr1.buffer_info)

# count(), extend(arr) --> append whole array to another array
print(arr1.count(31))
arr1.extend(arr)
print(arr1)

# forlist(list)
arr1.fromlist(arr)
print(arr1)

# tolist() --> transform array to list
li = arr1.tolist()
print(li) """
""" 
def revarr():
    a = int(input())
    b = []
    for i in range(a):
        b.append(int(input()))
        print(b)
        b.reverse()
        print(b)

revarr() """

##### ARRAY ROTATION #####

""" n = int(input("size of array: "))
arr = []
d = int(input("rotate by how many: "))
rotated_arr = []
for i in range(n):
    arr.append(int(input()))
print(arr)
rotate = d - n

for i in range(rotate):
    if d <= n:
            new_arr = arr.pop(d)
            print([new_arr])
            rotated_arr.append(new_arr)
            print(rotated_arr)

rotated_arr.extend(arr)
print(rotated_arr)  """


""" n = int(input())
arr = [] # 5 6 7 1 2 3 4
d = int(input("rotation time "))

for i in range(n):
    arr.append(int(input()))
# print(arr)

a2 = arr[d]
r = n - d
a = []
for i in range(r):
    if d <= n:
            new_arr = arr.pop(d)
            # print([new_arr])
            a.append(new_arr)
            # print(a)

a.extend(arr)
print(a)  """


""" def wnw():
    for n in range (1,30):
        if n % 2:
            print("Weird")
        elif n >= 2 or n <= 5:
            print("Not Weird")
        elif n >= 6 or n <= 20:
            print(str(n) + " Weird")

wnw() """
            
n = int(input())
def input_arr(n):
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(arr)

d = int(input("rotation time "))
r = n - d
a = []
def rotate(arr,d):
   # a2 = arr[d]
    for i in range(r):
        if d <= n:
                new_arr = arr.pop(d)
                # print([new_arr])
                a.append(new_arr)
                # print(a)

    a.extend(arr)
    print(a)

if __name__ == '__main__':
    user_arr = input_arr(n)
    rotate(user_arr,d)





