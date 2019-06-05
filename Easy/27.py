class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:        
        if not nums:
            return 0

        index = 0

        while index < len(nums):
            if nums[index] == val:
                del nums[index]
            else:
                index += 1

        return len(nums)
