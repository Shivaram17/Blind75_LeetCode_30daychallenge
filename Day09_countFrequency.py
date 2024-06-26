# count the frequency of elements in the list
def counter(arr):
  freq ={}
  for i in arr:
    freq[i] = freq.get(i,0) + 1
  return freq

counter([2,2,1,3,4,4,5,6,2,2,3,4])
