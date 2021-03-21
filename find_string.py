""" Return the count of sub-string “Jenny” appears in the given string"""

given_string = "Jenny is good in school, Jenny is good  good leader."
find = given_string.count("Jenny")
print(find)

def countStr(stuff):
    count = 0 
    for x in range(len(stuff)-1):   
        count += stuff[x: x + 4] == "good"
    print(count)

countStr(given_string)

