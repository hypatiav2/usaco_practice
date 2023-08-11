#Dice 

def beat(x,y):
  xPoints = 0
  yPoints = 0
  noPoints = 0
  for i in range(4):
    for m in range(4):
      if x[i] > y[m]:
        xPoints+=1
      elif y[m] > x[i]:
        yPoints+=1
      else:
        noPoints+=1
  if yPoints > xPoints:
    return y
  elif xPoints > yPoints:
    return x
  else: 
    return None

answers = []
t = int(input())

import itertools
for q in range(t):
  temp = input().split()
  temp = [int(i) for i in temp]
  aDice = temp[0:4]
  bDice = temp[4:9]

  win1 = beat(aDice, bDice)
  if win1 == None:
    answers.append("no")
    continue 
  for comb in itertools.combinations_with_replacement([1, 2, 3, 4,5,6,7,8,9,10], 4):
    win2 = beat(comb,bDice)
    win3 = beat(comb,aDice)
    if win2 == None or win3 == None:
      pass
    elif win1 != win2 and win1 != win3 and win3 != win2:
      answers.append("yes")
      break
  else:
    answers.append("no")

for s in answers:
  print(s)

