from Glyphs import *
import sys
import os
import re
import objc

# run on GlyphsApp source with a rectangular designspace (use designspace fix script to do so)

# families must be labeled using instance custom parameter `familyName`

relPath = sys.argv[-1]
filename = os.path.split(relPath)[1] # get just the filename
fileHead = os.path.split(relPath)[0]
directory = os.getcwd()
document = Glyphs.open((str(directory + "/" + relPath)), False)
font = document.font()

# font.removeObjectFromInstancesAtIndex_(0)

del(font.instances[0])