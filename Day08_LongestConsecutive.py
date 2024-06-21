class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O n linear time neetcode solution
        numSet = set(nums)
        longest = 0
        for n in nums:
            # start of the sequence
            if n-1 not in numSet:
                length = 0
                while n+length in numSet:
                    length +=1
                longest = max(length, longest)
        return longest


        # # sort the list
        # s = list(set(sorted(nums)))
        # s = sorted(s)
        # print('s:',s)
        # if nums == []:
        #     return 0
        # long_max = 1
        # count = 1
        # for i in range(len(s)-1):
        #     if s[i+1] - s[i] == 1:
        #         count = count +1
        #         long_max = max(count, long_max)
        #     else:
        #         count = 1
        # print("long_max: ", long_max)
        # return long_max
        
