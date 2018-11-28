
from Glyphs import *
import sys
import os
# import re
import objc

relPath = sys.argv[-1]
# filename = os.path.split(relPath)[1] # get just the filename
# fileHead = os.path.split(relPath)[0]
directory = os.getcwd()
document = Glyphs.open((str(directory + "/" + relPath)), False)
currentFont = document.font()


# instance = font.instances()[2]
# InterpolatedFont = font.generateInstance_error_(instance, None)
# print(InterpolatedFont)
# print(InterpolatedFont.fontMasters())

# currentLightFont = currentFont.generateInstance_error_(currentFont.instances()[0], None)
# currentBoldFont = currentFont.generateInstance_error_(currentFont.instances()[-1], None)

# print(currentLightFont.fontMasters()[0])
# print(currentBoldFont.fontMasters()[0])

# currentLightFontMasterID = currentLightFont.fontMasters()[0].id()
# currentBoldFontMasterID = currentBoldFont.fontMasters()[0].id()

# # currentFont.fontMasters().append(currentLightFont.fontMasters[0])
# # currentFont.fontMasters().append(currentBoldFont.fontMasters[0])
# # currentFont.insertFontMaster_atIndex_(currentLightFont.fontMasters()[0], 0)
# # currentFont.insertFontMaster_atIndex_(currentBoldFont.fontMasters()[0],1)
# currentFont.addFontMaster_(currentLightFont.fontMasters()[0])
# currentFont.addFontMaster_(currentBoldFont.fontMasters()[0])

# newLightMaster = currentFont.fontMasters()[-2]
# newBoldMaster = currentFont.fontMasters()[-1]
# newLightMasterID = newLightMaster.id()
# newBoldMasterID = newBoldMaster.id()

# print(currentFont.layers())

for index,glyph in enumerate(currentFont.glyphs()):
    print(glyph)
    print(glyph.layers())
    # for layer in glyph.layers():
    #     print(layer.associatedMasterId())
    # # make variable for glyph of interpolated font
	# # currentGlyph = currentFont.glyphs()[glyph.name()]
	# currentGlyph = currentFont.glyphs()[index]

    # ## these need to be layer indexes, it seems
    # # bring glyph data into glyph of new master
	# glyph.layers()[-2] = currentGlyph.layers()[-1]
    # # bring glyph data into glyph of new master
	# glyph.layers()[-2] = currentGlyph.layers()[-1]