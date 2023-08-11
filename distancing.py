#Distancing

#n = int(input())
#nums = input()
#nums = nums.split(' ')

def find_winner(n, nums): 
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
        print("...",left,right)
        #if  (left > min(sofar_r,sofar_l) and right > min(sofar_r,sofar_l)):
        if  (left > min(sofar_r,sofar_l) and right >min(sofar_r,sofar_l)):
                sofar_l = left
                sofar_r = right
                sofar_i = x
                print(sofar_l,sofar_r)
    print(sofar_i)
    return sofar_i

# testing
print(find_winner(5,[1,11,12,23,24])==0)
print("###")
print("####")
print(find_winner(5,[1,4,10,16,18])==2)
print("###")
print(find_winner(1,[1])==0)
print("###")
print(find_winner(5,[1,2,3,4,5])==0)
print("###")
print(find_winner(2,[1,50])==0)
print("###")