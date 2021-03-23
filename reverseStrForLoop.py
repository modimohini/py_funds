#Reverse a given number and return true if it is the same as the original number

# appending char in reverse orders
given_srt =  '12156'  # '121'
reverse_order = ""
correct_order = ""
for x in given_srt:
    print(x)
    reverse_order = x + reverse_order           # work like prepend            65121
    print(reverse_order, "reverse_order")

    correct_order = correct_order + x           # work like append
    print("correct_order", correct_order)

if given_srt == reverse_order:
    print("match")
else:
    print("no match")