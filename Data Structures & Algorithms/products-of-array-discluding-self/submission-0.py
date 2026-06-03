class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n

        leftprod = 1
        for i in range(n):
            ans[i] = leftprod
            leftprod *= nums[i]

        rightprod = 1
        for i in range(n-1, -1, -1):
            ans[i] *= rightprod
            rightprod *= nums[i]

        return ans