# def swap(a, b, arr):
#     arr[a], arr[b] = arr[b], arr[a]

def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements):
    pivot_index = 0
    pivot = elements[pivot_index]
    start = pivot_index + 1
    end = len(elements - 1 )

    while start < end: 
        while elements[start] <= pivot:
            start += 1
        
        while elements[end] > pivot:
            end -=1
        
        if start < end:
            swap(start, end, elements)
    swap(pivot_index, end, elements)

def quick_sort(elements):
    partition(elements)



if __name__ == '__main__':
    elements = [19, 229, 31, 31, 25, 9999, 31, 88]
    quick_sort(elements)
    print(elements)