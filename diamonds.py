# Problem: Diamonds
testmode = True

if testmode==False:
  fin = open('diamond.in', 'r')
  fout = open('diamond.out', 'w')

  def read():
    global fin
    return fin.readline()
  def show(x):
    global fout
    fout.write(str(x))
else:
  def read():
    return input()
  def show(x):
    print(x)
    
n, k = list(map(int, read().split()))
diamonds = list(map(int, read().split()))
diamonds.sort()

dp = [1]*n

for i in range(n):
    for j in range(i):
        if abs(diamonds[i]-diamonds[j])<=k:
            dp[i] = max(dp[i], dp[j]+1)
show(max(dp))

if testmode==False:
  fout.close()
