def k_most_frequent(arr, k):
  base_dict = {}
  final_set = set()

  for i in arr:
    if i in base_dict:
      base_dict[i] += 1
      if base_dict[i]>= k:
        final_set.add(i)
    else:
      base_dict[i] = 1
      if base_dict[i]>= k:
        final_set.add(i)

  return list(final_set)


arr = [1,1,1,2,2,3,4,4,6]
# arr = [1]
k_most_frequent(arr, 2)


  
