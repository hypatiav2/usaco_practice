# Problem: Mad Scientist
fin = open('breedflip.in', 'r')
fout = open('breedflip.out', 'w')

n = int(fin.readline().strip())
stringA = fin.readline().strip()
stringB = fin.readline().strip()

equal = True
num = 0

for i in range(n):
  if stringA[i] != stringB[i]:
    equal = False
  elif stringA[i] == stringB[i] and equal == False: 
    equal = True
    num+=1
if equal == False:
  num+=1

fout.write(str(num))
fout.close()