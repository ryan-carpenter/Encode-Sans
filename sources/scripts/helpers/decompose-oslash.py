from Glyphs import *
import sys
import os
import objc

relPath = sys.argv[-1]
# font = GSFont(filename)
directory = os.getcwd()
fullPath = str(directory + "/" + relPath)
document = Glyphs.open((fullPath), False)
font = document.font()

# for glyph in enumerate(font.glyphs()[34].layers()):
# for glyph in font.glyphs():
#     print(glyph)
#     print(glyph.layers_())


# print(font.glyphs()[1].layers())


def oslashIndexer():
    oslashIndex = 0
    for index,glyph in enumerate(font.glyphs()):
        print(".",end=' ')
        if glyph.name() == "oslash":
            oslashIndex = index
            return oslashIndex

oslashIndex = oslashIndexer()
print(oslashIndex)

glyph = font.glyphs()[oslashIndex]

for index,master in enumerate(font.fontMasters()):
    print(index)
    master = font.fontMasterAtIndex_(index)
    print(glyph.layerForKey_(master.id()))
    glyph.layerForKey_(master.id()).decomposeComponents()


testFile = fullPath.replace(".glyphs","-test.glyphs")

font.save(testFile)