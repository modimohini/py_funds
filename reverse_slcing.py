#Reverse a given number and return true if it is the same as the original number

# appending char in reverse orders
given_srt =  '12156'  # '121'
rever_str = ''

for x in given_srt[::-1]:
    rever_str =  rever_str + x

print(rever_str)

# reverse with functi
def reverse_slicing(slice):
    return slice[::-1]

input_str = 'abcd'
print(reverse_slicing(input_str))

