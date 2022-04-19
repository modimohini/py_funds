word = "hello"


### abc cab bca 
# user input word
# convert word into list []
# lenght of list
# for item in range(len(list))
# join list as new_word 
# check if the new_word != word 
    # log out the output else log "reach all possible pattern "

""" list_word = list(word)
b = ''
n = 0 
for item in range(len(list_word)):
    if n < len(list_word):
        li = list_word.pop(n)
        print(li)
        n += 1
        for item in list_word:
            # print(item)
            b = b + item
        print(b)
        c = b + li
        print(c) """



# In-place rotates s towards left by d
def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    if tmp != s:
        print(tmp)
    else:
        print('reach all combo')
    
   
# In-place rotates s
# towards right by d
def rightrotate(s, d):
   
   return leftrotate(s, len(s) - d)
 
# Driver code
if __name__=="__main__":
  
    str2 = "abc"
    print(leftrotate(str2, 0))
    print(leftrotate(str2, 1))
    print(leftrotate(str2, 2))
    print(leftrotate(str2, 3))
    print(leftrotate(str2, 4))


