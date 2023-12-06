# This function performs the counting sort algorithm on a given array.
# It sorts the array by counting the occurrences of each element and then placing them in the correct sorted order.
def counting_sort(arr):
    n = len(arr)  # Get the length of the array
    max_val = max(arr)  # Find the maximum value in the array

    # Create a count array to store the frequency of each element
    count = [0] * (max_val + 1)

    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1

    # Modify the count array to store cumulative counts
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # Create an output array to store the sorted elements
    output = [0] * n

    # Build the output array by placing elements in their correct sorted positions
    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1

    # Copy the sorted elements from the output array back to the original array
    arr[:] = output


# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)  # Sort the array using counting sort
print("Sorted array:", arr)  # Print the sorted array
'''
Time Complexity	 
Best	O(n+k)
Worst	O(n+k)
Average	O(n+k)
Space Complexity	O(max)
Stability	Yes
'''