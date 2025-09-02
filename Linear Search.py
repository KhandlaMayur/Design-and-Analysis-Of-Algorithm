def linear_search(arr,key):
    for i in range(0,len(arr)):
        if(key==arr[i]):
            print("Element Found")
            return key
  
    print("Element not Found")

arr=[15,5,2,3,4,7]
key=3
linear_search(arr,key)
