'''
Best	O(nlog n)
Worst	O(nlog n)
Average	O(nlog n)
Space Complexity	O(1)
Stability	No
'''


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is larger than the current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is larger than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the current root, swap them
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (maximum) element with the last element
        heapify(arr, i, 0)  # Call heapify on the reduced heap


arr=[3,3,235,23,12,45,1,43,23,4,13,2,3,23,1,3,23,4]
heap_sort(arr)
print("Sorted array:", arr)


def heapify(arr, n, i, key_index):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left][key_index] > arr[largest][key_index]:
        largest = left

    if right < n and arr[right][key_index] > arr[largest][key_index]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key_index)

def heap_sort(arr, key_index):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key_index)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key_index)

# Example usage:
input_list = [(1, 2), (4, 3), (0, 3)]
key_index = 0  # Sort based on the second element of each tuple

heap_sort(input_list, key_index)
print("Sorted list:", input_list)


