# This function performs the bucket sort algorithm on a given array.
# It divides the input range into equal-sized buckets, distributes the elements into the buckets,
# sorts each bucket, and then concatenates the sorted buckets to get the final sorted array.
def bucket_sort(arr):
    n = len(arr)  # Get the length of the array
    max_val = max(arr)  # Find the maximum value in the array

    # Create empty buckets, the number of buckets can be adjusted based on the range of input values
    num_buckets = n
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets based on their value ranges
    for num in arr:
        bucket_index = int(num * num_buckets / (max_val + 1))  # Calculate the appropriate bucket index
        buckets[bucket_index].append(num)  # Add the element to the corresponding bucket

    # Sort individual buckets using another sorting algorithm (e.g., insertion sort)
    for bucket in buckets:
        insertion_sort(bucket)  # Apply insertion sort to sort each bucket in place

    # Concatenate the sorted buckets to get the final sorted array
    sorted_array = [num for bucket in buckets for num in bucket]
    arr[:] = sorted_array  # Copy the sorted elements back to the original array


# This function performs the insertion sort algorithm on a given array.
# It sorts the array by repeatedly taking elements from the unsorted part and inserting them in the correct position
# in the sorted part of the array.
def insertion_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted in the sorted part
        j = i - 1  # Index of the last element in the sorted part
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift elements to the right to make space for the new element
            j -= 1
        arr[j + 1] = key  # Insert the current element in the correct position


# Example usage
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
bucket_sort(arr)  # Sort the array using bucket sort
print("Sorted array:", arr)  # Print the sorted array
'''
Time Complexity	 
Best	O(n+k)
Worst	O(n2)
Average	O(n)
Space Complexity	O(n+k)
Stability	Yes
'''