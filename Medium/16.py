class Solution:
    def threeSumClosest(self, nums, target) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1
            while left < right:
                summ = nums[i]+nums[left]+nums[right]
                tmp = abs(summ - target)
                if summ == target:
                    return summ
                elif summ < target:
                    # update
                    if tmp < abs(res - target):
                        res = summ
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    left += 1
                else:
                    if tmp < abs(res - target):
                        res = summ
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    right -= 1
        return res
