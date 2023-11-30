arr = [24, 24, 532, 245, 242, 24, 2456, 77, 5, 868, 35232]


# def merge_sort_inplace(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#
#     merge_sort_inplace(left)
#     merge_sort_inplace(right)
#
#     merge_inplace(left, right, arr)
#
#
# def merge_inplace(left, right, arr):
#     i = j = k = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1
#
#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1
#
#     while j < len(right):
#         arr[k] = right[j]
#         j += 1
#         k += 1
#
#
# merge_sort_inplace(arr)
#
# for k in arr:
#   print(k, end=" ")
#
#

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


for k in merge_sort(arr):
    print(k, end=" ")
'''

Time Complexity	 
Best	O(n*log n)
Worst	O(n*log n)
Average	O(n*log n)
Space Complexity	O(n)
Stability	Yes
'''