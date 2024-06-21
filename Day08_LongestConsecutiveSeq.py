# Brute force method
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the list
        s = list(set(sorted(nums)))
        s = sorted(s)
        print('s:',s)
        if nums == []:
            return 0
        long_max = 1
        count = 1
        for i in range(len(s)-1):
            if s[i+1] - s[i] == 1:
                count = count +1
                long_max = max(count, long_max)
            else:
                count = 1
        print("long_max: ", long_max)
        return long_max


# nums = [0,-1]
nums = [-1, 2,20,4,10,3,4,5]

# Output: 4

obj = Solution()
output = obj.longestConsecutive(nums)
output
