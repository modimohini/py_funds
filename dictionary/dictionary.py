# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print(Dict)
 
# # Creating a Dictionary
# # with Mixed keys
# Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
# print("\nDictionary with the use of Mixed Keys: ")
# print(Dict) 

""" word = "hello"
match_set = "billo"
x = []
for i in match_set:
    x += i
print(x)
for j in range(0,len(x)): 
    print(j)
    for k in (j+1, len(x)):
        if x[j] == x[k]:
            c = c + 1 
            print(x[j])
            print(c)
        else:
            print(x(j)) """

from curses import keyname


word = "facebook"
new_word = "heloo"


def count_char(word):
    char_di = {}
    for i in word:
        if i in char_di:
            char_di[i] += 1
        else:
            char_di[i] = 1
    print(char_di)

word1 = count_char(word)
word2 = count_char(new_word)

if word2[0] in word1[0:]:
    print("exist")
else:
    print("no")