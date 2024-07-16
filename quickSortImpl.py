#9. How is an integer array sorted inplace using the quicksort algorithm?
def quicksort(arr, low, high):
    while low < high:
        
        if high - low < 10:
            insertion_sort(arr, low, high)
            break        
        
        pi = partition(arr, low, high)
       
        if pi - low < high - pi:
            quicksort(arr, low, pi - 1)
            low = pi + 1
        else:
            quicksort(arr, pi + 1, high)
            high = pi - 1

def partition(arr, low, high):
    
    mid = low + (high - low) 
    pivot = median_of_three(arr, low, mid, high)
    arr[pivot], arr[high] = arr[high], arr[pivot]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def median_of_three(arr, low, mid, high):
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid

def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Sorted array:", arr)
