
# brute force method O(n*2)
class Solution:
  def productExceptSelf(self, nums):
    l = []
    arr = []
    for i in nums:
      arr = nums.copy()
      c = 1
      print(i)
      arr.remove(i)
      print('arr', arr, 'nums ',nums)
      for j in arr:
        c = c*j
      l.append(c)
      print('list: ', l)
      
    return l

# nums = [1,2,3,4]
nums = [-1,0,1,2,3]
obj = Solution()
output = obj.productExceptSelf(nums)
output
