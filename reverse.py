""" given = "121"

rev =  reversed(given)
print(rev)
for x in rev:
    print(x, " ", rev)

    if x == rev:
        print("true")
    else:
        print("false") """





word = "Easy"
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

combo(x)
