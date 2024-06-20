class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

    
    
    #     l = []
    #     arr = []
    #     for i in nums:
    #         arr = nums.copy()
    #         c = 1
    #         print(i)
    #         arr.remove(i)
    #         print('arr', arr, 'nums ',nums)
    #         for j in arr:
    #             c = c*j
    #         l.append(c)
    #     print('list: ', l)
        
    #     return l
        
