def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    count = [0] * range_val
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in reversed(range(len(arr))):
        count[arr[i] - min_val] -= 1
        output[count[arr[i] - min_val]] = arr[i]

    return output

arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))
