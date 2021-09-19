def insertion_sort(arr):
    result=[]
    result.append(arr.pop(0))
    for array_value in arr:
        smallest_flag=True
        for i in range(len(result)-1,-1,-1):
            if array_value >= result[i]:
                result.insert(i+1,array_value)
                smallest_flag=False
                break
        if smallest_flag:
            result.insert(0,array_value)
    arr=result
    return arr

if __name__=="__main__":
    arr_input=input("Type in the number array:\n").split()
    arr=[int(x) for x in arr_input]#convert to array of integer
    print("Array sorted by insertion sort:")
    print(insertion_sort(arr))
