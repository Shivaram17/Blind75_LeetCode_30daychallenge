def findi_missing_num():
  list_dict = {}
  for i in l:
    list_dict[i] = True
  for i in range(len(l)):
    if not list_dict.get(i):
      return i
  return None
