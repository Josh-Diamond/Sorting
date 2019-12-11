# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB): # merges sub-lists into sorted list
    sorted_arr = []
    a_idx = 0
    b_idx = 0
    while a_idx < len(arrA) and b_idx < len(arrB):
        if arrA[a_idx] < arrB[b_idx]:
            sorted_arr.append(arrA[a_idx])
            a_idx += 1
        else:
            sorted_arr.append(arrB[b_idx])
            b_idx += 1
    if a_idx == len(arrA):
        sorted_arr.extend((arrB[b_idx:])) # if arrA has been looped through, no need to compare arrA value with arrB value, push rest of arrB to sorted_arr
    else:
        sorted_arr.extend(arrA[a_idx:])
    return sorted_arr

def merge_sort(arr): # breaks down lists
    if len(arr) <= 1: # if arr has zero or one items, it is already sorted
        return arr
    # split list in half and call merge sort recursively on each half
    left, right = merge_sort(arr[:int(len(arr)/2)]), merge_sort((arr[int(len(arr)/2):]))

    # merge sub-lists into sorted_arr
    return merge(left, right)

birthday = [1991, 10, 21]
print(merge_sort(birthday))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
