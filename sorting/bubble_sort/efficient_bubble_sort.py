def bubble_sort(element):
    size = len(element)
    for i in range(size-1):
        swapped = False 
        for j in range(size-1-i):
            if element[j] > element[j+1]:
                tmp = element[j]
                element[j] = element[j+1]
                element[j+1] =  tmp
                swapped = True
        if not swapped:
            #print("all sorted already!")
            break


if __name__ == '__main__':
    #element = [19, 229, 31, 31, 25, 9999, 31, 88]
    element = [1,2,3,2]
    bubble_sort(element)
    print(element)