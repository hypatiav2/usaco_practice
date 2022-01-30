# Problem: Comfortable Cows
cowlist = []
n = int(input())
for m in range(n):
  temp = input().split()
  cowlist.append((int(temp[0]),int(temp[1])))
print(cowlist)


# Sumall
n = int(input())
for i in range(1,n+1):
    if i%2 ==0:
        print(i)