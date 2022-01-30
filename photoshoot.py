#Photoshoot

from itertools import permutations as permute

fin = open("photo.in", "r")
fout = open("photo.out", "w+")

useless, line = fin.readlines()

nums = [int(i) for i in line.split(" ")]

def main(nums):
    foo = [i+1 for i in range(len(nums)+1)]
    bar = permute(foo)
    
    for permutation in bar:
      boo = False
      for i in range(1, len(permutation)):
          if permutation[i]+permutation[i-1] != nums[i-1]:
              boo = False
              break
          else:
            boo = True
      
      if boo:
          return permutation

final = " ".join([str(i) for i in main(nums)])
fout.write(final)

fin.close()
fout.close()
