"""
Usage: on the command line or in a shell script, use:

python <path>/subset-glyphs-replaced-by-smallcaps.py FONTNAME.ttf --remove "fi fl"

(--remove removes additional glyphs that don't have smallcap versions but are not needed in smallcap font)

This script:

1. uses ttFont to get list glyph names
2. finds all lowercase counterparts to smallcaps glyphs
3. uses pyftsubset to subset font removing lowercase counterparts

"""

import argparse
from fontTools.ttLib import TTFont
from fontTools import subset

def getNewGlyphSet(font_path, removeNames, keepNames, smallCapSuffix):

	ttfont = TTFont(font_path)

	glyphNames = ttfont.getGlyphOrder()

	smallcaps = [name for name in ttfont.getGlyphOrder() if f'.{smallCapSuffix}' in name]

	glyphsReplacedBySmallcaps = [name.replace(f'.{smallCapSuffix}','') for name in smallcaps if name in glyphNames]

	newGlyphNames = [name for name in glyphNames if name not in glyphsReplacedBySmallcaps and name not in removeNames] + [name for name in keepNames]

	return " ".join(newGlyphNames)


if __name__ == "__main__":
	import argparse
	description = """Get glyphnames to use in pyftsubset for font with smcp feature frozen in"""
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument("fontPath",
						help="The path to an otf or ttf file")
	parser.add_argument("-r", "--remove",
						default="",
						help="Glyph names to exclude from the final glyphset")
	parser.add_argument("-k", "--keep",
						default="",
						help="Glyph names to specifically include in the final glyphset, in case they are being dropped")
	parser.add_argument("-s", "--suffix",
						default="sc",
						help="Suffix used to denote smallcaps glyphs. Default is 'sc'.")
		
	args = parser.parse_args()
	font_path = args.fontPath
	removeNames = args.remove.split(" ")
	keepNames = args.keep.split(" ")
	suffix = args.suffix

	newGlyphSet = getNewGlyphSet(font_path, removeNames, keepNames, suffix)

	subset.main([font_path, "--name-IDs=*", "--glyph-names", "--notdef-outline", "--glyphs=%s" % newGlyphSet])