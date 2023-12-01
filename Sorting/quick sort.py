def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


'''
Best	O(n*log n)
Worst	O(n2)
Average	O(n*log n)
Space Complexity	O(log n)
Stability	No
'''