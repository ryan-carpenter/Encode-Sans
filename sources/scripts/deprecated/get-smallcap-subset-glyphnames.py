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

import argparse
from fontTools.ttLib import TTFont

def getNewGlyphSet(font_path, removeNames):

	ttfont = TTFont(font_path)

	glyphNames = ttfont.getGlyphOrder()

	smallcaps = [name for name in ttfont.getGlyphOrder() if f'.{smallCapSuffix}' in name]

	glyphsReplacedBySmallcaps = [name.replace(f'.{smallCapSuffix}','') for name in smallcaps if name in glyphNames]

	newGlyphNames = [name for name in glyphNames if name not in glyphsReplacedBySmallcaps and name not in removeNames]
	# newGlyphNames = [name for name in glyphNames if name not in glyphsReplacedBySmallcaps]

	print(" ".join(newGlyphNames))

if __name__ == "__main__":
	import argparse
	description = """Get glyphnames to use in pyftsubset for font with smcp feature frozen in"""
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument("fontPath",
						help="The path to an otf or ttf file")
	parser.add_argument("-r", "--remove",
						help="Glyph names to exclude from the final glyphset")
		
	args = parser.parse_args()
	font_path = args.fontPath
	removeNames = args.remove

	print(removeNames)


	getNewGlyphSet(font_path, removeNames)