
# def double_values(list1):
#     doubles = []
#     for num in list1:
#         doubles.append(num * 2)
# #    print(doubles)
#     return doubles

# first_list = [1, 2, 3, 4]
# print(double_values(first_list))

######################################
# pair1 = ('a', 'b', 'c')
# pair2 = ('d', 'e', 'f')
# index = 0

# while index < len(pair1):
#     for item in pair2:
#         print(pair2[index], item)
#     index += 1

###########################################

def fib(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        yield a
fib_gen = fib(4)
print(fib_gen)