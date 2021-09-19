def selection_sort(arr):
    result=[]
    while(len(arr)>0):
        (_,index)=find_min(arr)
        result.append(arr.pop(index))
    arr=result
    return arr

def find_min(arr):
    min=arr[0]
    index=0
    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
            index=i
    return (min,index)

if __name__=="__main__":

    arr_input=input("Type in the array:\n").split()
    arr=[int(x) for x in arr_input]
    print("Array sorted by selection sort:")
    print(selection_sort(arr))
