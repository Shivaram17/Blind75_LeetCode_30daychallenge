# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

arr = [1,3,5,5,6,7]
target = 10

def index_sum(arr, target):
    index_list = []
    
    # get the index of two numbers that add up to the target
    for i in range(len(arr)-1):
        for j in range(1,len(arr)):
            if arr[i] + arr[j] == target:
                index_list.append(i,j)
                return index_list
    return None
    
index_sum(arr, target)
        
            
        

print("Try programiz.pro")

# arr 
