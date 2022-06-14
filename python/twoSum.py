class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            m = target - num
            if m in d:
                return d[m],i    
            d[num] = i
            print(d)

nums = [3,7,4,15]
target = 11
prob = Solution()
print(prob.twoSum(nums, target))

