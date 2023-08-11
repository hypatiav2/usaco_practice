answers  = []
t = int(input())
for case in range(t):
    inp = input().split()
    n,p = int(inp[0]), int(inp[1])
    totals = 1
    for i in range(1,n+1):
        for j in range(1,p+1):
            totals = (totals * (i+j+1))  % (10**9+7)
    answers.append(totals)
for i in answers:
    print(i)