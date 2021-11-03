"""two list of numbers create a new list such that new list should contain only odd numbers from the 
first list and even numbers from the second list"""
list1 =  [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]
y = []
new_list = []
even_list = []
odd_list = []
for x in list1:
    if (x % 2 != 0):
        new_list.append(x) 
        odd_list.append(x)   
for x in list2:
    if (x % 2 == 0):
        new_list.append(x)
        even_list.append(x)
print(new_list)
print(even_list, "even")
print(odd_list, 'odd')

