# check if the list is sorted
def isSorted(arr):
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      return False
  return True

# arr = [1,2,3,4]
# arr = [-1, 1,3,3,4]
arr = [0, 1,3,2,4]

isSorted(arr)

# better approach
def is_sorted(arr):
  return all(arr[i] > arr[i+1] for i in range(len(arr)-1))
arr = [0, 1,3,2,4]
is_sorted(arr)
