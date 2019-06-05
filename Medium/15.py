class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return[]

        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                if nums[i] + nums[left] + nums[right] is 0:
                    res.append([ nums[i], nums[left], nums[right] ])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        x = [list(t) for t in res]
        return x
