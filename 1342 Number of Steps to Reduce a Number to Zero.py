class Solution:
    def numberOfSteps(self, num: int) -> int:
        step_count = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
                step_count += 1
            else:
                num -= 1
                step_count += 1
        return step_count
    
x = Solution()
y = x.numberOfSteps(45)
print(y)