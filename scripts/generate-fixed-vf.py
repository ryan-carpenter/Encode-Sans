
__doc__="""
This script fixes several errors in variable fonts generated via FontMake from a Glyphs source with a non-rectangular designspace. It does the following:

1. Makes a temporary duplicate of the Glyphs
2. Decomposes components to avoid a macOS CoreText error
3. Morphs values to make a rectangular designspace
4. Generates the variable font with FontMake
5. Deletes temporary duplicate file
"""

import os
import shutil
from shutil import copyfile
import glyphsLib
from glyphsLib import GSFont

######################################
##### DEFINE THE VARIABLE BELOW #####

glyphsSourcePath = "sources/Encode-Sans.glyphs"

##### DEFINE THE VARIABLE ABOVE #####
######################################

tempGlyphsPath = glyphsSourcePath.replace(".glyphs", "-temp.glyphs")

def makeTempCopy(glyphsSourcePath, tempGlyphsPath):
    
    copyfile(glyphsSourcePath, tempGlyphsPath)
    return(tempGlyphsPath)

def deleteTempCopy(tempGlyphsPath):
    if os.path.isfile(tempGlyphsPath):
        os.remove(tempGlyphsPath)
    else:    ## Show an error ##
        print("Error: %s file not found" % tempGlyphsPath)

# makeTempCopy(glyphsSourcePath)
# deleteTempCopy(glyphsSourcePath.replace(".glyphs", "-temp.glyphs"))

def loadGlyphsFile(glyphsFile):
    font = GSFont(glyphsFile)

    font.save(glyphsFile)

def decomposeAllGlyphs(glyphsFile):
    font = GSFont(glyphsFile)
    for glyph in font.glyphs:
        for layer in glyph.layers:
            if len(layer.components) >= 0:
                # layer.decomposeComponents()
                print(".", end='')
                for component in layer.components:
                    component.decompose() # not available in glyphsLib?
                    print(".", end='')
                    print(glyph.name, component)

decomposeAllGlyphs(makeTempCopy(glyphsSourcePath, tempGlyphsPath))
deleteTempCopy(tempGlyphsPath)

# 