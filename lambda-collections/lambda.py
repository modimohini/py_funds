def sq(num):
    return num * num 
sq_lambda = lambda num: num * num 
assert sq(4) == sq_lambda(4)


given_list = [10, 20, 33, 47, 10, 990]
new_range = map(lambda num: num * 2, given_list) # map act like for loop
print(list(new_range))

evens = filter(lambda num: num % 2 == 0, given_list)
print(list(evens))

from functools import reduce
the_sum = reduce(lambda acc, num: acc + num, given_list, 0)
print(the_sum)

city = ['Tokyo','New York','Toronto','Hong Kong', 'ping', 'nigeria']
print(sorted(city))

print("sorting wiht lambda key")
print(sorted(city, key = lambda s: s.lower()))

