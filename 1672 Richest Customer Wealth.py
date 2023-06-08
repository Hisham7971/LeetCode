class Solution:
    def maximumWealth(self, accounts): #: List[List[int]]) -> int:
        return max([sum(x) for x in accounts])
    
customers = [[23,45],[35,89],[85,65]]
x = Solution()
y = x.maximumWealth(customers)
print(y)


