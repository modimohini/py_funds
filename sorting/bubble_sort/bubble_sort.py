def bubble_sort(element):
    size = len(element)
    for i in range(size-1):
        for j in range(size-1-i):
            if element[j] > element[j+1]:
                tmp = element[j]
                element[j] = element[j+1]
                element[j+1] =  tmp


if __name__ == '__main__':
    #element = [19, 229, 31, 31, 25, 9999, 31, 88]
    element = [ "Japanese", "American", "Mexican", "French" ]

    bubble_sort(element)
    print(element)