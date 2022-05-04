# # constructor cannot return any value .. so solution will error out 
# class Class_A:
#     def __init__(self, var):
#         return var
# obj = Class_A('hi')
# print(obj)

# # CHOOSE correct output 
# r1 = '{0},{2} and {1}'.format('a','b','c')
# r2 = '{},{} and {}'.format('a','b','c')
# print(r1)
# print(r2)

# # predict output
# d = {5:5, 15:'15','5':5,'15':25}
# d[str(15)] = 100
# print(d)
# L = list(d)
# L.append("py")
# print(L)

# try:
#     print(30/0)
# except ZeroDivisionError:
#     print(" 0 div err")
# else:
#     print("nothing wrg")
# except:
#     print("someitng wrg")

# #i = ""
# for i in "    ":
#     print("Java", end = i)

# class A:
#     def __init__(self):
#         self.num1 = 10
#     def show_num1(self):
#         print(self.num1)

# class B(A):
#     def __init__(self):
#         self.num2 = 20
#         super().__init__()
#     def show_num2(self):
#         print(self.num2)

# obj = B()
# print(type(obj.show_num1))
# obj.show_num2


# from datetime import datetime
 
# datetime = datetime(2019, 11, 27, 11, 27, 22)
# print(datetime.strftime('%y/%B/%d %H:%M:%S'))
###################################
# class Test:
#     def __init__(self, s='Welcome'):
#         self.s = s
 
#     def print(self):
#         print(self.s)
 
 
# x = Test()
# x.print()
#################################
# class Cat:
#     Species = 1
 
#     def get_species(self):
#         return 'kitty'
 
 
# class Tiger(Cat):
#     def get_species(self):
#         return 'tiggy'
 
#     def set_species(self):
#         pass
 
 
# creature = Tiger()
# print(hasattr(creature, "Species"),
#       hasattr(Cat, "set_species"))

#################################

# d = {}
# d[1] = 1
# d['1'] = 2
# d[1] += 1
 
# sum = 0
 
# for k in d:
#     sum += d[k]
 
# print(sum)

#################################
# try:
#     file = open('test.txt', 'r')
#     # insert your code here
#     data = file.read()
#     print(data)
# except:
#     print('Something went wrong!')

#################################

x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
 
def func(data):
    res = data[0][0]
    print("this is res value: " + str(res))
    for da in data:
        print(da)
        for d in da:
            print(" ---- " + str(d))
            if res < d:
                print(res)
                res = d
    return res
 
print(func(x[0]))