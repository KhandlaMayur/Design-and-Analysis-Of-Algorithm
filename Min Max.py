def min_max(arr):
    if not arr:
        return None, None  

    min_val = max_val = arr[0]

    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val

arr = [4, 5, 6, 10, 7, 8, 3]
print(min_max(arr))
