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
