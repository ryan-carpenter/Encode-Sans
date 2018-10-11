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
wdthMax = 400.0
wdthMin = 100.0

# Bold Extended and Bold Condensed original values
wghtWideMax = 230.0
wghtCondMax = 176.0

# Light Extended and Light Condensed original values
wghtWideMin = 44.0
wghtCondMin = 40.0

# Light Extended master index + Condensed Bold master index (starts from 0)
wideLightIndex = 3
condBoldIndex = 2

# Set this if using a 6 master setup with equal middle masters
wghtMid = 130.0
wghtMidNew = wghtCondMin + ((wghtMid - wghtCondMin) / (wghtCondMax - wghtCondMin)) * (wghtWideMax - wghtCondMin)

widthDict = {100.0 : 70.0, 200.0 : 85.0, 300.0 : 100.0, 400.0 : 115.0}

for instance in font.instances:
	if instance.active == True:
		# Find max weight at this width
		wghtIntrMax = evenRound(wghtCondMax + ( ((instance.widthValue - wdthMin) / (wdthMax - wdthMin)) * (wghtWideMax - wghtCondMax) ))
		
		# Find min width at this width
		wghtIntrMin = evenRound(wghtCondMin + ( ((instance.widthValue - wdthMin) / (wdthMax - wdthMin)) * (wghtWideMin - wghtCondMin) ))
		
		# Original weight
		oldWght = instance.weightValue

		newWght = round( wghtCondMin + ( ((instance.weightValue - wghtIntrMin) / (wghtIntrMax - wghtIntrMin)) * (wghtWideMax - wghtCondMin)))

		font.masters[wideLightIndex].weightValue = wghtCondMin
		font.masters[condBoldIndex].weightValue = wghtWideMax
		font.masters[1].weightValue = wghtMidNew

		instance.weightValue = newWght
		instance.widthValue = widthDict[instance.widthValue]

		instance.name = re.sub("^\d* ", "", instance.name)

		print "Interp Values:", str(wghtIntrMax) + ", " + str(wghtIntrMin), "     Original Weight", oldWght, "scaled to", newWght
		# print "Renamed as", instance.name, "\n"

for master in font.masters:
	master.widthValue = widthDict[master.widthValue]
			
if nonDestructive == False:		
	print "\nScaled file to a rectangular designspace"

for instance in font.instances:
	if instance.active:
		if instance.weightValue < 71.0 + 5 and instance.weightValue > 71.0 - 5:
			instance.weightValue = 71.0
		elif instance.weightValue < 120.0 + 5 and instance.weightValue > 120.0 - 5:
			instance.weightValue = 120.0
		elif instance.weightValue < 177.0 + 5 and instance.weightValue > 177.0 - 5:
			instance.weightValue = 177.0


font.save(filename)