"""
Usage: on the command line or in a shell script, use:

python get-smallcap-subset-glyphnames.py FONTNAME.ttf

This script:

1. uses ttFont to get list glyph names
2. finds all lowercase counterparts to smallcaps glyphs
3. outputs a list of all glyphnames, minus lowercase counterparts

The output list can then be used in pyftsubset to subset the old lowercase out of the font.

"""

# set this if different
smallCapSuffix = "sc"

import sys
from fontTools.ttLib import TTFont

font_path = sys.argv[1]

ttfont = TTFont(font_path)

glyphNames = ttfont.getGlyphOrder()

smallcaps = [name for name in ttfont.getGlyphOrder() if smallCapSuffix in name]

glyphsReplacedBySmallcaps = [name.replace(smallCapSuffix,'') for name in smallcaps if name in glyphNames]

newGlyphNames = [name for name in glyphNames if name not in glyphsReplacedBySmallcaps]

print(" ".join(newGlyphNames))
