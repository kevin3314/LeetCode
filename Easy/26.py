class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)

        current_val = nums[0]
        count = 1
        index = 1

        while index < len(nums):
            if nums[index] > current_val:
                count += 1
                current_val = nums[index]
                index += 1

            else:
                del nums[index]

        print(nums)
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,2]))
    
