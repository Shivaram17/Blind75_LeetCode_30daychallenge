def count_len(l):
  # if list not empty
  if not l:
    return 0
  return 1 + count_len(l[1:])

l = [1,2,3]
count_len(l)
