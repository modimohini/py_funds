#Reverse a given number and return true if it is the same as the original number
given_srt =  '12156'  # '121'

def reverse_join(string_given):
    x = ''.join(reversed(string_given))
    return x

print(reverse_join(given_srt))