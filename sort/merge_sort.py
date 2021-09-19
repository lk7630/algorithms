def merge_sort(arr):
    if len(arr)>=2:
        mid=len(arr)//2
        left_arr=arr[:mid]
        right_arr=arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i=j=k=0
        left_len=len(left_arr)
        right_len=len(right_arr)
        while i<left_len and j<right_len:
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1

        while i<left_len:
            arr[k]=left_arr[i]
            k+=1
            i+=1

        while j<right_len:
            arr[k]=right_arr[j]
            k+=1
            j+=1

    return arr

if __name__=="__main__":

    arr_input=input("Type in the array:\n").split()
    arr=[int(x) for x in arr_input]
    print("Array sorted by merge sort:")
    print(merge_sort(arr))
