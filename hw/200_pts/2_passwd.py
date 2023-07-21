numbers = input()
min_len = int(input())
#  sort arr
nums = numbers.split(",")
map(lambda x: int(x), nums)
nums.sort()
print(nums[0:3])
print(nums, min_len)
res = []
for i in range(len(nums)):
    if i > len(nums) - int(min_len):
        continue
    for j in range(i+min_len, len(nums)+1):
        r = nums[i:j]
        if r not in res:
            res.append(nums[i:j])
print(res)