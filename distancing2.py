# Problem: Distancing2
n = int(input())
nums = input()
nums = nums.split(' ')
right = 0
left = 0
sofar_r = 0
sofar_l = 10000
sofar_i = 0
for x in range(n):
    if n==2:
        sofar_i = 0
        break
    if x != 0:
        left = int(nums[x])-int(nums[x-1])
    else: left = 10000
    if x != n-1:
        right = int(nums[x+1])-int(nums[x])
    else:
        right = 100000
    #if  (left > min(sofar_r,sofar_l) and right > min(sofar_r,sofar_l)):
    if  (left > min(sofar_r,sofar_l) and right >min(sofar_r,sofar_l)):
            sofar_l = left
            sofar_r = right
            sofar_i = x
print(sofar_i)
