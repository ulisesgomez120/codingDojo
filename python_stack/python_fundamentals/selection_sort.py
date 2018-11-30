def find_min(arr):
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum

def selection_sort(arr):
    for i in range(len(arr)):
        unsorted = arr[i:]
        mini = find_min(unsorted)
        mini_index = arr[i:].index(mini) + i
        arr[i], arr[mini_index] = arr[mini_index], arr[i]
    print(arr) 

selection_sort([3, 2, 8, 6, 6, 1])
selection_sort([3,2,8,6,1,7,6,9,7,7,0,5])
selection_sort([3, 2, 8, 6, 1])
