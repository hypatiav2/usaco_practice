# Problem: Field Reduction
testmode = False

if testmode==False:
  fin = open('reduce.in', 'r')
  fout = open('reduce.out', 'w')

  def read():
    global fin
    return fin.readline()
  def show(x):
    global fout
    fout.write(str(x) + "\n")
else:
  def read():
    return input()
  def show(x):
    print(x)
    
n = int(read())
cows = set()
for i in range(n):
    x, y = map(int, read().split())
    cows.add((x, y))

min_x, max_x, min_y, max_y = float("inf"), float("-inf"), float("inf"), float("-inf")
for x, y in cows:
    min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)

ans = (max_x - min_x) * (max_y - min_y)

removed = set()

for x, y in cows:
    removed.add((x, y))
    min_x, max_x, min_y, max_y = float("inf"), float("-inf"), float("inf"), float("-inf")
    for i, j in cows - removed:
        min_x, max_x, min_y, max_y = min(min_x, i), max(max_x, i), min(min_y, j), max(max_y, j)
    ans = min(ans, (max_x - min_x) * (max_y - min_y))
    if len(removed) == 3:
        break
show(ans)

if testmode==False:
  fout.close()
