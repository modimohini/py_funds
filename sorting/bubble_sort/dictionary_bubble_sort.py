def bubble_sort(element, key=None):
    size = len(element)
    for i in range(size-1):
        for j in range(size-1-i):
            a = element[j][key]
            b = element[j+1][key]
            if a > b:
                temp = element[j]
                element[j] = element[j+1]
                element[j+1] = temp



# element = [ "Japanese", "American", "Mexican", "French" ]
element = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ] 
bubble_sort(element, key= 'transaction_amount')
print(element)