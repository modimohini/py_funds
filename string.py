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

