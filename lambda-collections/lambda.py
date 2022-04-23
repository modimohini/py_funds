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
print(sorted(city, key = lambda li: li.lower()))

# sort dic 
people = [
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Fred Ward", "age": 77},
    {"name": "finn Carter", "age": 59},
    {"name": "Ariana Richards", "age": 40},
    {"name": "Victor Wong", "age": 74},
]

sort_by_name = sorted(people, key = lambda d: d['name'].lower())
# print(sort_by_name)

# map in lambda for dictionary  
name_age = list(
    map(lambda d: f"{d['name']} is {d['age']} years old", sort_by_name)
)
print(name_age)

# filter in lambda for dictionary  
under_seventy = sorted(
    filter(lambda d: d['age'] < 60, sort_by_name), key = lambda d: d['age']
)
print(under_seventy)
