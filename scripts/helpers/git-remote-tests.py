
from Glyphs import *
import sys
import os
import objc

relPath = sys.argv[-1]
# filename = os.path.split(relPath)[1] # get just the filename
# fileHead = os.path.split(relPath)[0]
directory = os.getcwd()
document = Glyphs.open((str(directory + "/" + relPath)), False)
currentFont = document.font()



# # InterpolatedFont = font.generateInstance_error_(instance, None)
# # print(InterpolatedFont)
# # print(InterpolatedFont.fontMasters())

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

print(currentFont.glyphs()[4]) # GSGlyph <0x7ffcc505d960>: Abrevedotbelow

print(currentFont.glyphs()[4].layers) # <native-selector layers of GSGlyph <0x7ffcc505d960>: Abrevedotbelow>

# print(currentFont.glyphs()[4].layers[0]) # TypeError: 'objc.native_selector' object is not subscriptable

# print(currentFont.glyphs()[4].layers_()) # AttributeError: 'NSDistantObject' object has no attribute 'layers_'

# print(currentFont.glyphs()[4].layers_()[0]) # AttributeError: 'NSDistantObject' object has no attribute 'layers_'

# print(currentFont.glyphs()[4].layers()) # objc.error: NSInternalInconsistencyException - decodeObjectForKey: class "MGOrderedDictionary" not loaded

# print(currentFont.glyphs()[4].layers()[0]) # objc.error: NSInternalInconsistencyException - decodeObjectForKey: class "MGOrderedDictionary" not loaded

print(help(currentFont.glyphs()[4].layers))


# for index,glyph in enumerate(currentFont.glyphs()):
#     print(glyph)
#     print(glyph.layers()[0])
#     print(glyph.layers()[0])
    # for layer in glyph.layers:
    #     print(layer)
        # print(layer.associatedMasterId())
    # # make variable for glyph of interpolated font
	# # currentGlyph = currentFont.glyphs()[glyph.name()]
	# currentGlyph = currentFont.glyphs()[index]

    # ## these need to be layer indexes, it seems
    # # bring glyph data into glyph of new master
	# glyph.layers()[-2] = currentGlyph.layers()[-1]
    # # bring glyph data into glyph of new master
	# glyph.layers()[-2] = currentGlyph.layers()[-1]