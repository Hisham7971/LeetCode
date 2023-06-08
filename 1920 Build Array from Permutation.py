# Intuition: nums[nums[i]], here we are checking the index value in the inner list, 
#            then that value is taken as the index value of the outer list.
# Approach:
# Time complexity: 0(n)
# Space complexity: 0(n)


nums = [0,2,1,5,3,4]
n = list(range(len(nums)))
for i in range(len(nums)):
    n[i]=nums[nums[i]]
print(n)


# USING GENERATOR EXPRESSION
# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#        return (nums[i] for i in nums)