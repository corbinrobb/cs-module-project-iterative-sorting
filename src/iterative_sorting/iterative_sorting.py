
# Selection sort psuedo
# loop through each index
    # declare current index and smallest index
    # in each index start another loop from current index to end
        # if any value is smaller than smallest index value then
        # switch value with smallest index


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                temp = arr[smallest_index]
                arr[smallest_index] = arr[j]
                arr[j] = temp

    return arr

# Bubble sort psuedo
# store last index
# while last index is not 0:
    # loop from 0 to last index:
        # if cur is greater that next
            # switch current and next values
    # change last index - 1
# return list

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    last_index = len(arr) - 1
    while last_index > 0:
        for i in range(last_index):
            curr_num = arr[i]
            next_num = arr[i + 1]
            if curr_num > next_num:
                arr[i] = next_num
                arr[i+1] = curr_num
        last_index -= 1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    if not len(arr):
        return arr
        
    buckets = [0 for n in range(max(arr) + 1)]

    new_arr = []

    for n in arr:
        if n < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            buckets[n] += 1

    for i, n in enumerate(buckets):
        if n > 0:
            for j in range(n):
                new_arr.append(i)


    return new_arr


# ^^^^ Not the most elegant solution but it works for now