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


# print("seeking /oslash to decompose")

def oslashIndexer():
    oslashIndex = 0
    for index,glyph in enumerate(font.glyphs()):
        if glyph.name() == "oslash":
            oslashIndex = index
            return oslashIndex

oslashIndex = oslashIndexer()
print(oslashIndex)

# glyph = font.glyphs()[oslashIndex]
# print(font.fontMasterAtIndex_(0))


for index,master in enumerate(font.fontMasters()):
    print(master)
    print(index)
    master = font.fontMasterAtIndex_(index)
    print(glyph.layerForKey_(master.id()))
    glyph.layerForKey_(master.id()).decomposeComponents()


# for index in range(1,font.countOfFontMasters()):
#     print(index)
#     master = font.fontMasterAtIndex_(index)
#     print(glyph.layerForKey_(master.id()))
#     glyph.layerForKey_(master.id()).decomposeComponents()


oslashDecompFile = fullPath.replace(".glyphs","-oslash_decomp.glyphs")

font.save(oslashDecompFile)