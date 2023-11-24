list1=[1,3,44,55,66,77,88,99,100,101,102]


def binarySearch(list,ele):
    start =0
    end=len(list)-1

    while start<=end:
        mid=int(start+(end-start)/2)
        if list[mid]==ele:
            return mid
        elif list[mid]>ele:
            end = mid - 1

        else:
            start = mid + 1
    return -1


print(binarySearch(list1,1))