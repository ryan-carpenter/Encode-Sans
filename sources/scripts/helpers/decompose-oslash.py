import sys
from glyphsLib import glyphdata
from glyphsLib import GSFont

filename = sys.argv[-1]
font = GSFont(filename)

for layer in font.glyphs["oslash"].layers:
    print(layer)
