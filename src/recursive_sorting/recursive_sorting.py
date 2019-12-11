# TO-DO: complete the helper function below to merge 2 sorted lists
def merge(listA, listB): # merges sub-lists into sorted list
    sorted_list = []
    a_idx = 0
    b_idx = 0
    while a_idx < len(listA) and b_idx < len(listB):
        if listA[a_idx] < listB[b_idx]:
            sorted_list.append(listA[a_idx])
            a_idx += 1
        else:
            sorted_list.append(listB[b_idx])
            b_idx += 1
    if a_idx == len(listA):
        sorted_list.extend((listB[b_idx:])) # if listA has been looped through, no need to compare listA value with listB value, push rest of listB to sorted_list
    else:
        sorted_list.extend(listA[a_idx:])
    return sorted_list

def merge_sort(list): # breaks down lists
    if len(list) <= 1: # if list has zero or one items, it is already sorted
        return list
    # split list in half and call merge sort recursively on each half
    left, right = merge_sort(list[:int(len(list)/2)]), merge_sort((list[int(len(list)/2):]))

    # merge sub-lists into sorted_list
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
