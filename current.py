# Problem: 

testmode = True
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



if testmode==False:
  fout.close()
