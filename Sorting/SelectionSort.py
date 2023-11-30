arr = [5,4,3,2,1]


def SelectionSort(arr):
    for i in range(len(arr)):
        maxindex = 0
        for j in range(len(arr) - i):
            if arr[j] > arr[maxindex]:
                maxindex = j
        arr[maxindex], arr[len(arr) - i-1] = arr[len(arr) - i-1], arr[maxindex]


SelectionSort(arr)

for k in arr:
    print(k, end=" ")

'''
Time Complexity	 
Best	O(n^2)
Worst	O(n^2)
Average	O(n^2)
Space Complexity	O(1)
Stability	No
'''
