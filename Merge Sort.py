def mergesort(arr):
    if(len(arr)<=1):
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=mergesort(left)
    right=mergesort(right)
    return (merge(left,right))

def merge(left,right):
    merge=[]
    i=j=0

    while i<len(left) and j<len(right):
        if(left[i]<right[j]):
            merge.append(left[i])
            i=i+1
        else:
            merge.append(right[j])
            j=j+1
    
    merge.extend(left[i:])
    merge.extend(right[j:])
    return merge

arr=[2,5,4,1,6,9,3]
print(mergesort(arr))
