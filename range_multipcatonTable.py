# Print multiplication table form 1 to 10
for x in range(1,11):
    for y in range(1,11):
        table = x * y
        print(table, end = " ")
    print("\n")