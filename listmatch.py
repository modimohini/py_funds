"""Given a list of numbers, return True if first and last number of a list is same"""

given_list = [10, 20, 30, 40, 10]

first_num = given_list[0]
print(first_num)
last_num_index = len(given_list)-1
# last_num = (given_list[last_num_index])
last_num = given_list[-1]

if (first_num == last_num):
    print(given_list, " result is True")
else:
    print(given_list, " False")



