def in_place_sorting(arr):
    for i in range (0,len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if(arr[min_index]>arr[j]):
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

arr=[4,5,3,1,2,8]
print(in_place_sorting(arr))
