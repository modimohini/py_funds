""" # Print multiplication table form 1 to 10
for x in range(1,11):
    for y in range(1,11):
        table = x * y
        print(table, end = " ")
    print("\n") """

from __future__ import print_function

def pr(y):
    for x in range(1,y+1):
        j =print(x , end = "")
        h = "% s" % j
    print("")

z = input("give number: ")
y = int(z)
pr(y)

