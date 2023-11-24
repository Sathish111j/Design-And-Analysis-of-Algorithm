arr = [5, 4, 3, 2, 1]


def bubleSort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break


bubleSort(arr)

for k in arr:
    print(k, end=" ")

'''
Time Complexity
Best	O(n)
Worst	O(n^2)
Average	O(n^2)
Space Complexity	 O(1)
Stability	Yes
'''