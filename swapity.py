# Problem: Swapity Swap

testmode = False
if testmode==False:
  fin = open('swap.in', 'r')
  fout = open('swap.out', 'w')

  def read():
    global fin
    return fin.readline()
  def show(x):
    global fout
    fout.write(x + "\n")
else:
  def read():
    return input()
  def show(x):
    print(x)
    
    


pair = read().split()
n = int(pair[0])
k = int(pair[1])

pair = read().split()
a1 = int(pair[0])-1
a2 = int(pair[1])-1

pair = read().split()
b1 = int(pair[0])-1
b2 = int(pair[1])-1

cows = list(range(1,n+1))
count = 0

def swap(cowlist):
  global a1,a2,b1,b2
  cowlist = cowlist[0:a1] + cowlist[a2:a1-1:-1] + cowlist[a2+1:]
  cowlist = cowlist[0:b1] + cowlist[b2:b1-1:-1] + cowlist[b2+1:]
  return cowlist


def smart(cows,count):
  global k
  reversed_list = cows
  for i in range(k%count):
    reversed_list = swap(reversed_list)
  return reversed_list
  
final = cows
for i in range(k):
  count+=1
  final = swap(final)
  if final == cows:
    final = smart(cows,count)
    break


for i in final:
  show(str(i))


if testmode==False: fout.close()
