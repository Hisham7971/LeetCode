class Solution:
    def sum(self, num1: int, num2: int) -> int: # "-> int" at the end of the line indicates that the method will return an integer
        return num1 + num2

x = Solution()
y = x.sum(3, 4)
print(y)