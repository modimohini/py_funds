""" Given a string, display only those characters which are present at an even index number. """

user_str = input("enter some word: ")
def evenString(str):
    for x in range(0, len(str)-1, 2):
        print ("index[" ,x,"]" , str[x])

evenString(user_str)


