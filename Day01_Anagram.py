# blind 75 anagrams
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

      count = 0
      # sort the strings
      s = "".join(sorted(s))
      t = "".join(sorted(t))

      print(t, s)
      if len(s) != len(t):
        return False
      for i in range(len(s)):
        if t[i] != s[i]:
          return False
        else:
          count = count +1

      return True

s = "racecar"
t = "carrace"

obj = Solution()
output_ana = obj.isAnagram(s,t)

output_ana



        
