"""
Sets the OS/2 xAvgCharWidth of a font.

Assumes the OS/2 table is version 3 or 4. 

Usage: on the command line or in a shell script, use:

python <path>/set-x_avg_char_width.py FONTNAME.ttf

"""

import argparse
from fontTools.ttLib import TTFont
from fontTools import subset

def setOS2avgWidth(font_path):

    ttFont = TTFont(font_path)

    # code from https://font-bakery.readthedocs.io/en/latest/_modules/fontbakery/profiles/os2.html#com_google_fonts_check_xavgcharwidth

    width_sum = 0
    count = 0
    for glyph_id in ttFont['glyf'].glyphs:  # At least .notdef must be present.
      width = ttFont['hmtx'].metrics[glyph_id][0]
      # The OpenType spec doesn't exclude negative widths, but only positive
      # widths seems to be the assumption in the wild?
      if width > 0:
        count += 1
        width_sum += width

    avg_value = int(round(width_sum / count))

    print(ttFont['OS/2'].xAvgCharWidth)

    ttFont['OS/2'].xAvgCharWidth = avg_value
        
    print(ttFont['OS/2'].xAvgCharWidth)

    ttFont.save(font_path)


if __name__ == "__main__":
    import argparse
    description = """Get glyphnames to use in pyftsubset for font with smcp feature frozen in"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("fontPath",
                        help="The path to an otf or ttf file")
        
    args = parser.parse_args()
    font_path = args.fontPath

    setOS2avgWidth(font_path)