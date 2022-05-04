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
message = input("enter msg: ")

print("lowercase: ", message.lower())
print("uppercase: ", message.upper())
print("Capitalized: ", message.capitalize())
print("title case: ", message.title())

words = message.split()
print("words:", words)

sort_words = sorted(words)
print(sort_words)

string = "".join(words)
print(string)

ls = list(message)
print(ls)

