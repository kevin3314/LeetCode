class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        if n < 4:
            return []
        res = []

        for i in range(0, n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j>i+1 and nums[j-1] == nums[j]:
                    continue
                l, r = j+1, n-1
                while l < r:
                    summ = nums[i] + nums[j] + nums[l] + nums[r]
                    if summ < target:
                        l += 1
                    elif summ > target:
                        r -= 1
                    else:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res


def main():
    sol = Solution()
    print(sol.fourSum([0,0,0,0], 0))

if __name__ == "__main__":
    main()
