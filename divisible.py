"""Given a list of numbers, Iterate it and print only those numbers which are divisible of 5"""
given_list = [10, 20, 33, 46, 55]

for x in given_list:
   
    if ( x % 5  == 0):
        print("devisible num " , x)
    else:
        print("not divisible by 5 ", "given number ", x )
# comm  