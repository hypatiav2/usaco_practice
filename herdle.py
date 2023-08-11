# Problem: Herdle

green = 0
yellow = 0
correct = []
for i in range(3):
  correct.append(list(input()))

guess = []
for i in range(3):
  guess.append(list(input()))

for i in range(3):
  for m in range(3):
    if guess[i][m] == correct[i][m]:
      green+=1
      correct[i][m] = "_"
      guess[i][m] = "*"

for i in range(3):
  for m in range(3):
    if guess[i][m] in correct[0]:
      if guess[i][m] == correct[i][m]:
        green+=1
        correct[i][m] = "_"
      else: 
        yellow+=1
        index = correct[0].index(guess[i][m])
        correct[0][index] = "_"

    elif guess[i][m] in correct[1]:
      if guess[i][m] == correct[i][m]:
        green+=1
        correct[i][m] = "_"
      else: 
        yellow+=1
        index = correct[1].index(guess[i][m])
        correct[1][index] = "_"

    elif guess[i][m] in correct[2]:
      if guess[i][m] == correct[i][m]:
        green+=1
        correct[i][m] = "_"
      else: 
        yellow+=1
        index = correct[2].index(guess[i][m])
        correct[2][index] = "_"

print(green)
print(yellow)
