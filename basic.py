# Problem: Comfortable Cows
cowlist = []
n = int(input())
for m in range(n):
  temp = input().split()
  cowlist.append((int(temp[0]),int(temp[1])))
print(cowlist)

#Reverse Print
n = int(input())
cows = []
for i in range(n): cows.append(input())
for m in reversed(cows): print(m)

#Copy Machine
n = int(input())
cows = []
for i in range(n): cows.append(input())
for m in reversed(cows): print(m)

#Evensteven
n = int(input())
list1 = []
for i in range(n):
    list1.append(int(input()))
for m in list1: print(m)
    
# Sumall
n = int(input())
for i in range(1,n+1):
    if i%2 ==0:
        print(i)