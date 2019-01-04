"""
Usage: on the command line or in a shell script, use:

python get-smallcap-subset-glyphnames.py FONTNAME.ttx

(be sure to use a TTX file)

"""

smallCapSuffix = "sc"

import sys
import xml.etree.ElementTree as ET

ttxFile = sys.argv[-1]

tree = ET.parse(ttxFile)
root = tree.getroot()

glyphsInFont = []

for hmtx in root.findall('hmtx'):
    for mtx in hmtx.findall('mtx'):
        glyphName = mtx.get('name')
        glyphsInFont.append(glyphName)

glyphsToRemove = []

for index, glyphName in enumerate(glyphsInFont):
    if f'.{smallCapSuffix}' in glyphName:
        rootName = glyphName.replace(f'.{smallCapSuffix}', '')

        if rootName in glyphsInFont:
            glyphsToRemove.append(rootName)

for glyphName in glyphsToRemove[::-1]:
    glyphsInFont.remove(glyphName)

# print(glyphsInFont)
# print(glyphsToRemove)

# print space-separated list
for glyphName in set(glyphsInFont):
    print(glyphName, " ", end="")
