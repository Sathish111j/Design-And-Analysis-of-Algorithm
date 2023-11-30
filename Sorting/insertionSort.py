arr = [5, 4, 3, 2, 1]


def insertionsort(arr):
    for i in range(len(arr) -1):
        for j in range(i + 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


insertionsort(arr)
for k in arr:
    print(k, end=" ")

'''
Time Complexity	 
Best	O(n)
Worst	O(n2)
Average	O(n2)
Space Complexity	O(1)
Stability	Yes
'''