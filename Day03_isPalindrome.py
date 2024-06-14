def is_Palindrome(str):
  len_str = len(str)
  c=0
  for i in range(len_str/2):
    if str[i] == str[len_str-i-1]:
      continue
    else:
      c=1
      break

  # shortcut
  print(str[::-1]==str)
  return c==0
