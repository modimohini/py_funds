var = 'hello world'
li = var.split()
print(li)
li2 = []
for i in var:
    li2.append(i)
print(li2)

print(li2[0:5])
print(li2[:5])

print(li2[6:])