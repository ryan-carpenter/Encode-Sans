__doc__ = """
    Use to go through TTF/OTF files in a given directory and shorten their name IDs 4 & 6 to abbreviated names.

    Requires Python 3 & FontTools.

    Usage:
    - Add to the "abbreviations" dictionary if you have other long words (or partial words) in your font's style name
    - Run on the command line (or from a shell script) with the following syntax:

    python SCRIPT/PATH/shorten-nameID-4-6.py FONT/PATH/font.otf

    ...or for a folder of fonts:

    python SCRIPT/PATH/shorten-nameID-4-6.py FONT/PATH

"""

import sys
import os
from fontTools.ttLib import TTFont

path = sys.argv[-1]

print('------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------')
print('fixing SC nameIDs 1, 3, 4, & 6 in ' + path)
print('------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------')


# GET / SET NAME HELPER FUNCTIONS

def getFontNameID(font, ID, platformID=3, platEncID=1):
	name = str(font['name'].getName(ID, platformID, platEncID))
	return name

def setFontNameID(font, ID, newName):
	
	print(f"\n\t• name {ID}:")
	macIDs = {"platformID": 3, "platEncID": 1, "langID": 0x409}
	winIDs = {"platformID": 1, "platEncID": 0, "langID": 0x0}

	oldMacName = font['name'].getName(ID, *macIDs.values())
	oldWinName = font['name'].getName(ID, *winIDs.values())

	if oldMacName != newName:
		print(f"\n\t\t Mac name was '{oldMacName}'")
		font['name'].setName(newName, ID, *macIDs.values())
		print(f"\n\t\t Mac name now '{newName}'")

	if oldWinName != newName:
		print(f"\n\t\t Win name was '{oldWinName}'")
		font['name'].setName(newName, ID, *winIDs.values())
		print(f"\n\t\t Win name now '{newName}'")


def abbreviate(name):

    for key in abbreviations.keys():
        if key in name:
            name = name.replace(key, abbreviations[key])

    return(name)

def abbreviateNames(path):

    font = TTFont(path)

    # name 16
    name16 = getFontNameID(font, 16)
    if name16 != 'None':
        newName16 = name16 + ' SC'
        setFontNameID(font, 16, newName16)

    # name 6
    name6 = getFontNameID(font, 6)
    newName6 = name6.replace("-", "SC-")
    setFontNameID(font, 6, newName6)

    # name 4
    name4 = getFontNameID(font, 4)
    newName4 = name4.replace(" SC","").replace("Encode Sans", "Encode Sans SC")
    if "Regular" not in name6:
        newName4 = newName4.replace(" Regular","") # remove "Regular" in font name if not in postscript name (and therefore the style is not a Regular)
    setFontNameID(font, 4, newName4)

    # name 3
    name3 = getFontNameID(font, 3)
    newName3 = name3.replace("-", "SC-")
    setFontNameID(font, 3, newName3)

    # name 1
    name1 = getFontNameID(font, 1)
    newName1 = name1.replace(" SC","").replace("Encode Sans", "Encode Sans SC")
    setFontNameID(font, 1, newName1)

    print("Font saved with abbreviated names!")
    font.save(path)

# check if path is file
if os.path.isfile(path):
    abbreviateNames(path)

if os.path.isdir(path):
    print("is dir")
    for file in os.listdir(path):
        abbreviateNames(path + "/" + file)
