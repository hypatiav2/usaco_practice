import math
answers  = []
t = int(input())
for case in range(t):
    inp = input().split()
    n,p = int(inp[0]), int(inp[1])
    totals = 1
    for i in range(n):
        totals = (totals * (math.factorial(i+p+2) / math.factorial(i+2))) % (10**9+7)
    answers.append(totals)
for i in answers:
    print(i)