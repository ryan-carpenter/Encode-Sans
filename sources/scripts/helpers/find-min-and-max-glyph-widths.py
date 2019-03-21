wdthList = []
wdthWghtDict = {}

for instance in font.instances:
	wdthWghtDict[str(instance.widthValue)] = {}
	wdthList.append(instance.widthValue)

wdthList = set(wdthList)

for instance in font.instances:
	wdthWghtDict[str(instance.widthValue)][instance.weight]= (instance.weightValue)

# get max and min widths
wdthMax = max(wdthList)
wdthMin = min(wdthList)

# finds min wdth from widths list 
minWdthWghts = wdthWghtDict[str(wdthMin)]

# finds min wght value of instances in the min width
minWdthMinWght = minWdthWghts[min(minWdthWghts, key=lambda key: minWdthWghts[key])]

# finds max wght value of instances in the min width
minWdthMaxWght = minWdthWghts[max(minWdthWghts, key=lambda key: minWdthWghts[key])]

# finds weights dictionary from max width wdthWghtDict
maxWdthWghts = wdthWghtDict[str(wdthMax)]

# finds min wght value of instances in the max width
maxWdthMinWght = maxWdthWghts[min(maxWdthWghts, key=lambda key: maxWdthWghts[key])]

# finds max wght value of instances in the max width
maxWdthMaxWght = maxWdthWghts[max(maxWdthWghts, key=lambda key: maxWdthWghts[key])]

print(minWdthMinWght,maxWdthMinWght, minWdthMaxWght, maxWdthMaxWght)