#Problem: Drought

t = int(input())
def allEqual(iterable):
  iterator = iter(iterable)
    
  try:
    firstItem = next(iterator)
  except StopIteration:
    return True
        
  for x in iterator:
    if x!=firstItem:
      return False
  return True

def reduction(list1):
  newlist = sorted(list(set(list1)))
  secondmax = newlist[-2]
  return newlist[-1] - secondmax

answers = []
for i in range(t):
  n = int(input())
  line = input().split()
  line = [int(i) for i in line]
  bags = 0
  neg = False
  while allEqual(line) != True and neg == False:
    ind = line.index(max(line))
    if ind < n-1 and (line[ind] == line[ind+1]):
      difference = reduction(line)
      line[ind] -= difference
      line[ind+1] -= difference
      bags+=difference
    elif ind !=0 and (line[ind] == line[ind-1]):
      difference = reduction(line)
      line[ind] -= difference
      line[ind-1] -= difference
      bags+=difference
    elif ind == 0:
      line[ind] -= 1
      line[ind+1] -= 1
      bags+=1
    elif ind == n-1:
      line[ind] -= 1
      line[ind-1] -= 1
      bags+=1
    elif line[ind+1] < line[ind-1]:
      line[ind] -= 1
      line[ind+1] -= 1
      bags+=1
    elif line[ind-1] < line[ind+1]:
      line[ind] -= 1
      line[ind-1] -= 1
      bags+=1
    else:
      line[ind] -= 1
      line[ind+1] -= 1
      bags+=1
    if line[ind] < 0:
      neg = True
    elif ind < n-1 and line[ind+1] < 0:
      neg = True
    elif ind != 0 and line[ind-1] < 0:
      neg = True
  if neg == True:
    answers.append(-1)
  else:
    answers.append(bags*2)

for a in answers:
  print(a)

    

