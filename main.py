"""
# Problem: Comfortable Cows

cowlist = []
n = int(input())
for m in range(n):
  temp = input().split()
  cowlist.append((int(temp[0]),int(temp[1])))
print(cowlist)'''



# Problem: Triangles

from itertools import permutations
fin = open('triangles.in', 'r')
fout = open('triangles.out', 'w')

posts = []
areas = []
n = int(fin.readline().strip())

for i in range(n): 
  pair = fin.readline().split()
  post = (int(pair[0]),int(pair[1]))
  posts.append(post)

posts = list(permutations(posts,3))
for m in posts:
  if m[0][0]==m[1][0] and m[0][1] == m[2][1]:
    areas.append(abs(m[0][1] - m[1][1]) * abs(m[0][0] - m[2][0]))

fout.write(str(int(max(areas))))
fout.close()



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

"""