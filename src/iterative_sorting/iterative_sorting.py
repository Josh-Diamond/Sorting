# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ): # finds smallest value in set and swaps with current index (left => right)
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # Find next smallest element
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # SWAP
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    curr_swaps = 1
   # loop if swapped
    while curr_swaps > 0:
        curr_swaps = 0
        for i in range(0, len(arr) - 1):
            # Compare current iteration with next iteration
            if arr[i] > arr[i + 1]:
                # SWAP
                swap = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = swap
                curr_swaps += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr