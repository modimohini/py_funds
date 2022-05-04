# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
exp_list = ['2200','2350','2600','2200','2190']

# 1. In Feb, how many dollars you spent extra compare to January?
print("expense for month of Feb " + exp_list[1])
# 2. Find out your total expense in first quarter (first three months) of the year.
three_months_exp = int(exp_list[0])+int(exp_list[1])+int(exp_list[2])
print(three_months_exp)

# total months_exp
no_of_months_exp = 0
for item in exp_list:
    no_of_months_exp += int(item)
print("total no_of_months_exp "+ str(no_of_months_exp))

# 3. Find out if you spent exactly 2000 dollars in any month
x = '2000'
for item in exp_list:
    if item == x:
        print("match")
    else:
        None
print(exp_list)

print("Did I spent 2000$ in any month? ", str(2000) in exp_list) # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
june = "1980"
exp_list.append(june)
print(exp_list)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

exp_list[3] = int(exp_list[3]) - 200
print(exp_list)

# 6. converting string list to int's 
# for x in range(0,len(exp_list)):
#     exp_list[x] = int(exp_list[x])  
# print(exp_list)

new_li = list(map(int, exp_list))
print(new_li)