def linear_search(arr, target):
    # Your code here
    for i, n in enumerate(arr):
        if n == target:
            return i

    return -1   # not found

# binary search psuedo
# declare end index and begin index
# while beginning <= end:
    # mid = halfway index between begin and end
    # if target is < arr[midpoint]
        # ending = midpoint - 1
    # elif target is > arr[midpoint]
        # begin = midpoint + 1
    # elif target == arr[midpoint]
        # reuturn midpoint

import math

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    upper = len(arr) - 1
    lower = 0

    while lower <= upper:
        mid = int(math.floor((upper + lower)/2))
        
        if target < arr[mid]:
            upper = mid - 1
        elif target > arr[mid]:
            lower = mid + 1
        elif target == arr[mid]:
            return mid

    return -1  # not found
