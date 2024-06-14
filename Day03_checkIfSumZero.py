def checkSumZero(l):
  if len(l) < 2:
    return False
  l = set(l)
  for i in l:
    if -i in l:
      return True
  return False
