string = input().split()
k = int(string[0])
n = int(string[1])
allranks = []
pairs = []
consistent = True
for m in range(k):
    allranks.append(input().split())
for q in allranks[0]:
    for m in allranks[0]:
        for s in allranks:
            if s.index(q) >= s.index(m) or m==q:
                consistent = False
        if consistent == True:
            pairs.append((q,m))
        consistent = True
print(len(pairs))



