class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter

        counts = Counter(nums)
        for count in counts:
            if counts[count] > 1:
                return True
        return False