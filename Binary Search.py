def binary_search(arr, key, left, right):
    if left <= right:
        mid = (left + right) // 2 
        if arr[mid] == key:     
            return mid
        elif arr[mid] < key:       
            return binary_search(arr, key, mid + 1, right)
        else:                     
            return binary_search(arr, key, left, mid - 1)
    else:
        return -1 
arr = [1, 2, 3, 4, 6, 7, 8, 9, 11, 14]
key = 3
left = 0
right = len(arr) - 1
index = binary_search(arr, key, left, right)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
