
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

######################################
##### DEFINE THE VARIABLE BELOW #####

glyphsSourcePath = "sources/Encode-Sans.glyphs"

##### DEFINE THE VARIABLE ABOVE #####
######################################

def makeTempCopy(glyphsSourcePath):
    copyfile(glyphsSourcePath, glyphsSourcePath.replace(".glyphs", "-temp.glyphs"))

def deleteTempCopy(tempSourcePath):
    if os.path.isfile(tempSourcePath):
        os.remove(tempSourcePath)
    else:    ## Show an error ##
        print("Error: %s file not found" % tempSourcePath)

# makeTempCopy(glyphsSourcePath)
deleteTempCopy(glyphsSourcePath.replace(".glyphs", "-temp.glyphs"))