given = "121"

rev1 =  list(reversed(given))
rev = "".join(rev1)
print(rev)
if rev == given:
    print(True)
else:
    print(False)






""" word = "Easy"
x = list(word)
print(x)

nw = []
n_ln = []

def combo(x):
    for i in range(1,len(x)):
        print(i)
        for i in x:
            n_ln.append(i)
            print(n_ln)
            new_word = "".join(n_ln)
        print(new_word)
        if new_word == word:
            print("match")
        else:
            continue

combo(x) """
