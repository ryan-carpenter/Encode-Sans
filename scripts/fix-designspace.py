# set up for Encode Sans

import math
import sys
import re
from glyphsLib.glyphdata import get_glyph
from glyphsLib import GSFont
import objc

filename = sys.argv[-1]
font = GSFont(filename)

def evenRound(number):
	if int(number) % 2 == 0:
		return int(number)
	else:
		return int(number) + 1

# If set to false, the files master locations and instance values will all be changed
nonDestructive = False

# Width coordinates
wdthMax = 1000.0
wdthMin = 0.0

# Bold Extended and Bold Condensed original values
wghtWideMax = 232.0
wghtCondMax = 193.0

# Set this if using a 6 master setup with equal middle masters
wghtMid = 0.0

# Light Extended and Light Condensed original values
wghtWideMin = 34.0
wghtCondMin = 34.0

# Light Extended master index + Condensed Bold master index (starts from 0)
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
		
		# Find min width at this width
		wghtIntrMin = round(wghtCondMin + ( ((instance.widthValue - wdthMin) / (wdthMax - wdthMin)) * (wghtWideMin - wghtCondMin) ))
		
		# Original weight
		oldWght = instance.weightValue

		newWght = round( wghtCondMin + ( ((instance.weightValue - wghtIntrMin) / (wghtIntrMax - wghtIntrMin)) * (wghtWideMax - wghtCondMin)))

		font.masters[wideLightIndex].weightValue = wghtCondMin
		font.masters[condBoldIndex].weightValue = wghtWideMax
		# font.masters[1].weightValue = wghtMidNew

		instance.weightValue = newWght

		# insert customParameter weightClass 250 for thin instances, to support actual range of standard CSS
		if instance.weightValue == wghtCondMin:
			instance.customParameters['weightClass'] = 250
			
		instance.widthValue = widthDict[instance.widthValue]

		instance.name = re.sub("^\d* ", "", instance.name)

		print "Interp Values:", str(wghtIntrMax) + ", " + str(wghtIntrMin), "     Original Weight", oldWght, "scaled to", newWght
		# print "Renamed as", instance.name, "\n"

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