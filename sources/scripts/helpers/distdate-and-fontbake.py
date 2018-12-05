import sys
import os
import shutil
from datetime import datetime

fontPath = sys.argv[-1]
fontFile = os.path.split(fontPath)[1]
fontName = fontFile.split(".")[0]

# make timestamped folder in dist, like `SampleFont_2015-10-21-017_03`
currentDatetime = datetime.now().strftime('%Y-%m-%d')
# outputFolder = 'dist/' + GLYPHS_PATH.replace('sources/', '').replace('.glyphs', '-VF-') + currentDatetime + '/'

distPath = sys.argv[-3]
fontType = sys.argv[-2]
# outputFolder = f'dist/{currentDatetime}'
# outputFolder = f'dist/{distPath}-{currentDatetime}/{fontType}'
outputFolder = f'{distPath}/{fontType}'

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

defaultFontPath = fontPath
newFontPath = f'{outputFolder}/{fontFile}'
shutil.move(defaultFontPath, newFontPath)

# run fontbakery check on new font
fontbakeryCommand = f'fontbakery check-googlefonts {newFontPath} --ghmarkdown {outputFolder}/{fontName}-fontbakery-report.md'
print("fontbakeryCommand is " + fontbakeryCommand)

print(os.system(fontbakeryCommand))

ttxCommand = f'ttx {newFontPath}'


# fontbakery check-googlefonts fonts/full_vf/EncodeSans-VF.ttf --ghmarkdown fonts/full_vf/EncodeSans-VF-fontbakery-report.md