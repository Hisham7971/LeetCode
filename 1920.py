# Build Array from Permutation #

nums = [0, 2, 1, 5, 3, 4]
ans = list()

for i in range(len(nums)):
    ans.append(nums[nums[i]])

print(ans)
