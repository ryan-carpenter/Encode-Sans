oldWght = 222 # update for each instance

oldMin = 34
newMin = 34

oldMax = 222 # update for each width series
newMax = 232

newWght = (oldWght - oldMin) * (newMax - newMin) / (oldMax - oldMin) + newMin

print(round(newWght, 3))