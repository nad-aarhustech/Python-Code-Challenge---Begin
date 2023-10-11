def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
target = 10
print(linear_search(arr, target))