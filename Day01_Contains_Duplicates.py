# blind 75
# contains duplicates
class Solution:
    def hasDuplicate(self, nums):
      count = 0
      l = []
      for i in nums:
        if i not in l:
          l.append(i)
          count = count + 1
        else:
          count = count
      if count != len(nums):
        return True
      return False


arr = [1,2,3,5,4]
# 
obj = Solution()
output = obj.hasDuplicate(arr)

output
