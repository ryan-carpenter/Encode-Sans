import argparse
from fontTools.ttLib import TTFont

def keepDotlessi(font_path):
    """
        Necessary to assign unicode for lowercase dotlessi to smallcap version.
        Slightly hacky solution.
    """

    ttfont = TTFont(font_path)

    for table in ttfont['cmap'].tables:
        table.cmap[305] = "dotlessi.sc"

    ttfont.save(font_path)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("fontPath",
                        help="The path to an otf or ttf file")

    args = parser.parse_args()
    font_path = args.fontPath

    keepDotlessi(font_path)
