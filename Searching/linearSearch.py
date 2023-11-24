list1 = [1, 242, 33, 55, 34, 77, 97]


def linear_scearch(list, ele):
    for i in range(len(list)):
        if list[i] == ele:
            return i


print(linear_scearch(list1, 34))
