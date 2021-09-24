def quick_sort(arr,low,high):

    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)

    return arr

def partition(arr, low, high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1




if __name__=="__main__":

    arr_input=input("Type in the array:\n").split()
    arr=[int(x) for x in arr_input]
    print("Array sorted by quick sort:")
    print(quick_sort(arr,0,len(arr)-1))
