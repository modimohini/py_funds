given = "121"

rev =  reversed(given)
for x in rev:
    print(x, " ", rev)

    if x == rev:
        print("true")
    else:
        print("false")