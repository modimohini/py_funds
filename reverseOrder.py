"""code to extract each digit from an integer, in the reverse order"""
given_int = 7536
rever_int = ""
z = str(given_int) # conver int to string 
for x in z:
    rever_int = x  + " " + rever_int     
print(rever_int)
# while loop
while (given_int > 0):
    digit = given_int % 10
 
    given_int = given_int // 10
    print(digit, end = " ")