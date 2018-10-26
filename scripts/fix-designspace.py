# set up for Encode Sans

import math
import sys
import re
from glyphsLib import glyphdata
from glyphsLib import GSFont
# import objc

filename = sys.argv[-1]
font = GSFont(filename)

# def evenRound(number):
# 	if int(number) % 2 == 0:
# 		return int(number)
# 	else:
# 		return int(number) + 1

# If set to false, the files master locations and instance values will all be changed
nonDestructive = False

# Width coordinates
wdthMax = 1000.0
wdthMin = 0.0

# Bold Extended and Bold Condensed original values
# TODO: make these read from the file rather than relying on user entry
wghtWideMax = 232.0
wghtCondMax = 193.0

# Set this if using a 6 master setup with equal middle masters
wghtMid = 0.0

# Light Extended and Light Condensed original values
wghtWideMin = 34.0
wghtCondMin = 34.0

# Light Extended master index + Condensed Bold master index (starts from 0). Find these values in the GlyphsApp font.masters list.
wideLightIndex = 2
condBoldIndex = 1

# Set this if using a 6 master setup with equal middle masters
# wghtMid = 130.0
# wghtMidNew = wghtCondMin + ((wghtMid - wghtCondMin) / (wghtCondMax - wghtCondMin)) * (wghtWideMax - wghtCondMin)

widthDict = {0.0 : 70.0, 250.0 : 85.0, 500.0 : 100.0, 750.0 : 115.0, 1000.0 : 130.0}


for instance in font.instances:
	if instance.active == True:
		# Find max weight at this width
		wghtIntrMax = round(wghtCondMax + ( ((instance.widthValue - wdthMin) / (wdthMax - wdthMin)) * (wghtWideMax - wghtCondMax) ))
		
		# Find min weight at this width
		wghtIntrMin = round(wghtCondMin + ( ((instance.widthValue - wdthMin) / (wdthMax - wdthMin)) * (wghtWideMin - wghtCondMin) ))
		
		# Original weight
		oldWght = instance.weightValue

		newWght = round( wghtCondMin + ( ((instance.weightValue - wghtIntrMin) / (wghtIntrMax - wghtIntrMin)) * (wghtWideMax - wghtCondMin)))

		# If the font's master light weights don't match, this will match them
		font.masters[wideLightIndex].weightValue = wghtCondMin

		# In Encode Sans, the Condensed Bold has a lighter weight than the Extended Bold. This sets it as the same max.
		font.masters[condBoldIndex].weightValue = wghtWideMax
		
		# font.masters[1].weightValue = wghtMidNew # used in a 6-master setup

		instance.weightValue = newWght

		# insert customParameter weightClass 250 for thin instances, to support some software
		# this only work properly for Encode for now
		if instance.weightValue == wghtCondMin:
			instance.customParameters['weightClass'] = 250
			
		instance.widthValue = widthDict[instance.widthValue]

		instance.name = re.sub("^\d* ", "", instance.name)

		print "Interp Values:", str(wghtIntrMax) + ", " + str(wghtIntrMin), "     Original Weight", oldWght, "scaled to", newWght
		# print "Renamed as", instance.name, "\n"

## makes a dictionary of morphed designspace weight values, so it can find the mode value, then apply that to all instances to make an aligned grid
## assumes that weights instances have same names across different widths

wghtDict = {}
for instance in font.instances:
	wghtDict[instance.name] = []

for instance in font.instances:
	# print(instance.weightValue)
	wghtDict[instance.name].append(instance.weightValue)

# reduce weightDict entries down to mode value of each list
for key, val in wghtDict.items():
	print("weight values for " + key + " across widths: " + str(val))
	modeVal = max(set(val), key=val.count)
	print(str(modeVal) + " set as normalized value for " + key + "\n")
	wghtDict[key] = modeVal

# print(wghtDict)

# set instance wght values to the standardized values
for instance in font.instances:
	instance.weightValue = wghtDict[instance.name]

for master in font.masters:
	master.widthValue = widthDict[master.widthValue]
			
if nonDestructive == False:		
	print "\nScaled file to a rectangular designspace"

# for instance in font.instances:
# 	if instance.active:
# 		if instance.weightValue < 71.0 + 5 and instance.weightValue > 71.0 - 5:
# 			instance.weightValue = 71.0
# 		elif instance.weightValue < 120.0 + 5 and instance.weightValue > 120.0 - 5:
# 			instance.weightValue = 120.0
# 		elif instance.weightValue < 177.0 + 5 and instance.weightValue > 177.0 - 5:
# 			instance.weightValue = 177.0


font.save(filename)