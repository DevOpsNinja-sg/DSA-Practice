class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for num in sett:
            if num - 1 not in sett:
                current = num
                length = 1

                while current + 1 in sett:
                    current+=1
                    length+=1

                longest = max(longest,length)

        return longest