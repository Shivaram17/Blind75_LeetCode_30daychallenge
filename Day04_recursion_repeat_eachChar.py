# loop method
def without_recursion(s,n):
  s1=""
  for i in s:
    s1 = s1+i*3
  return s1
# recursion method
def with_recursion(s,n):
  if not s:
    return ""
  return s[0]*n + with_recursion(s[1:],n)

# check output
s = "Hello"
without_recursion(s,n)
with_recursion(s,n)
