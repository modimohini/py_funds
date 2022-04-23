
# # create a nested dictionary with 3 
# # fields of 3 students
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20}
# } 
# # iterate all the nested dictionaries with 
# # both keys and values
# for i in data:
#     print(data[i])
# for i in data:
#     print(data[i].keys())
# for i in data:
#     print(data[i].values())

########### iterate through word and count each char frequency 
user_str = "hello"
user_str2 = "yellllow"
char_freq = {}

for i in user_str:
    if i in char_freq:
        char_freq[i] += 1
    else:
        char_freq[i] = 1        
print(char_freq)  

for j in user_str2:
    if j in char_freq:
        print(j)
        print('no set needed')
        char_freq[j] -= 1
    else:
        char_freq[j] = 1
        print("new set needed") 
print(char_freq)    

# #  Using items() + dictionary comprehension
# res = {key: val for key, val in char_freq.items() if val < 0}
# print("sets of 'hello' are needed for " + str(res))    

# Using lambda + filter()