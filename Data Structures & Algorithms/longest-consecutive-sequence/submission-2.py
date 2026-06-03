class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in numSet:
            if (num-1) not in numSet:
                curNum = num
                curLongest = 1

                while (curNum+1) in numSet:
                    curNum += 1
                    curLongest += 1

                longest = max(longest, curLongest)
        return longest

