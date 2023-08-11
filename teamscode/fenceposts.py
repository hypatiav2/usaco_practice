def MinOperation(a, b, n):
     
    a.sort(reverse = False)
    b.sort(reverse = False)
 

    result = 0
 
    for i in range(0, n, 1):
        if (a[i] > b[i]):
            result = result + abs(a[i] - b[i])
 
        elif(a[i] < b[i]):
            result = result + abs(a[i] - b[i])
 
    return result

n = input().split()
n,m = int(n[0]),int(n[1])
a = [int(x) for x in input().split()]
oldb = [int(x) for x in input().split()]
b = []
for i in range(m):
    for q in range(oldb[i]):
        b.append(i+1)
for h in a:
    if h > m: b.append(h)

print(MinOperation(a, b, n))