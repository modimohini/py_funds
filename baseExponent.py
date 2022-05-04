"""Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp."""
base = 5
exponent = 4
result = 1
num = exponent

while num > 0:
    result = result * base 
    num = num - 1
    print(result)
    

