# Data structure 

# Array

# linked-list 

# Stacks and Queues

# Hash Tables 

# Graphs and Trees

# Heaps 

# Most Common Word 

# Larget Numbers 

# Diffrence of Arrays 

# LRU Cache 

# Balanced Tree



s = "That I the ever did see. Dusty as the handle on the door"
word = s.split()
print(word)
print(len(word))

j = "".join(word)
print(j)

x = list(j)
print(x)

count = 0
for i in word:
    if i == 'the':
        count += 1
print(str(count) + " words found it!")
