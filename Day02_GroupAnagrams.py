from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):

        #default dict mapping the charCount to list of Anagrams
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            # map the chars count to anagrams
            for c in s:
                count[ord(c) - ord("a")] += 1

            # attaching the mapped charcount to list of anagrams
            res[tuple(count)].append(s)

        return res.values()

#
strs = ["act","pots","tops","cat","stop","hat"]

obj = Solution()
output_list = obj.groupAnagrams(strs)
output_list
