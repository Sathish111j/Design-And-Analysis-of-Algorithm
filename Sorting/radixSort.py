# This function performs the counting sort algorithm on a given array considering a specific digit place (exp).
# It sorts the array based on the digit at the current place (units, tens, hundreds, etc.).
def counting_sort(arr, exp):
    n = len(arr)  # Get the length of the array
    output = [0] * n  # Create an output array of the same length filled with zeros
    count = [0] * 10  # Create a count array to store the frequency of each digit (0-9)

    # Count the occurrences of each digit at the current place
    for i in range(n):
        index = arr[i] // exp  # Calculate the index for the count array based on the digit at exp place
        count[index % 10] += 1  # Increment the count for the corresponding digit

    # Update the count array to store cumulative counts
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1  # Start iterating from the last element of the original array
    while i >= 0:
        index = arr[i] // exp  # Calculate the index for the count array again
        output[count[index % 10] - 1] = arr[i]  # Place the current element in the output array at the right position
        count[index % 10] -= 1  # Decrement the count for the corresponding digit
        i -= 1  # Move to the next element in the original array

    # Copy the sorted elements from the output array back to the original array
    for i in range(n):
        arr[i] = output[i]


# This function performs the radix sort algorithm on a given array.
# It sorts the array by considering each digit place (from least significant digit to most significant digit)
# and calling the counting_sort function to sort the array based on each digit place.
def radix_sort(arr):
    max_value = max(arr)  # Find the maximum value in the array
    exp = 1  # Initialize the exponent for the current digit place
    while max_value // exp > 0:
        counting_sort(arr, exp)  # Call counting_sort to sort the array based on the current digit place
        exp *= 10  # Move to the next digit place (10s, 100s, 1000s, ...)


# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)  # Sort the array using radix sort
print("Sorted array:", arr)  # Print the sorted array
'''
Time Complexity	 
Best	O(n+k)
Worst	O(n+k)
Average	O(n+k)
Space Complexity	O(max)
Stability	Yes
'''