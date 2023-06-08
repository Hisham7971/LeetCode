arr = [3,4,1,2,6]
target = 6
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(i,j)

# Leetcode solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return (i,j)