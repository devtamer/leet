class Solution:
    def findallmissingNums(self, nums):
        for i in range(len(nums)):

nums = [4,3,2,7,11,2,3,1]
prob = Solution()
print(prob.findallmissingNums(nums))

# For each number i in nums,
# we mark the number that i points as negative.
# Then we filter the list, get all the indexes
# who points to a positive number.
# Since those indexes are not visited. 