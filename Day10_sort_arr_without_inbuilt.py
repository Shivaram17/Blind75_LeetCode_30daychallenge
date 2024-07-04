
arr = [1,3,5,4,7]

# list of numbers sort it without in build function
        
def sort_list(l):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            continue
        else:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    return arr 

print(sort_list(arr))

print("Try programiz.pro")
