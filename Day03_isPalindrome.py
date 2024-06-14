def is_Palindrome(str):
  len_str = len(str)
  c=0
  for i in range(len(str)):
    if str[i] == str[len(str)-i-1]:
      continue
    else:
      c=1
      break
  return c==0
