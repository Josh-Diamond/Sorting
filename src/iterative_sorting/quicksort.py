import statistics

def partition(data):
    left = []
    pivot = statistics.median(data)
    right = []

    for num in data[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return left, pivot, right

def quicksort(data):
    if len(data) <= 1:
        return data

    left, pivot, right = partition(data)
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([5,3,4,9,8,5,7,4,5,2]))
