n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

for num in nums[:]:
    if nums.count(num) >1:
        num_count = nums.count(num)

        for _ in range(num_count):
            nums.remove(num)

    
if len(nums) ==0:
    print(-1)
else:
    print(max(nums))
