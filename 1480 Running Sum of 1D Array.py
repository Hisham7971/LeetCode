class Solution:
    def runningSum(self, nums): # List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            nums[i+1]=nums[i]+nums[i+1]
        return nums

x = Solution()

y = x.runningSum([1,2,3,4,5])
print(y)