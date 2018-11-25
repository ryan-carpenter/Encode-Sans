__doc__ = """
    Use to go through TTF/OTF files in a given directory and shorten their name IDs 4 & 6 to abbreviated names.

    Requires TTX & xmlStarlet.

    Assumes there are not any ttx files lurking in the directory you provide.
"""

import sys
import os
import subprocess

path = sys.argv[-1]

abbreviations = {
    "Condensed": "Cond",
    "SemiCondensed": "SemiCond",
    "Expanded": "Expd",
    "SemiExpanded": "SemiExpd",
    "ExtraLight": "ExLght",
    "Light": "Lght",
    "Regular": "Reg",
    "Medium": "Med",
    "SemiBold": "SemiBold",
    "ExtraBold": "ExBold",
}

def abbreviate(name):
    # print(name)
    name = name.replace("b","")
    name = name.replace("'","")

    for key in abbreviations.keys():
        if key in name:
            name = name.replace(key, abbreviations[key])

    # print(name)

    name = name.replace("\\n","")

    return(name)

def ttxAndFix(path):

    # make temp ttx of input file
    command = "ttx " + path
    print(subprocess.check_output(command, shell=True))
    tmpPath = path.replace(".ttf",".ttx")

    # make command to select nameID 4, then abbreviate it and make it a variable
    command = 'xml sel -t -v "//*/namerecord[@nameID=\'4\']" ' + tmpPath
    output = str(subprocess.check_output(command, shell=True))
    newName4 = abbreviate(output)

    # repeat for nameID 6
    command = 'xml sel -t -v "//*/namerecord[@nameID=\'6\']" ' + tmpPath
    output = str(subprocess.check_output(command, shell=True))
    newName6 = abbreviate(output)

    print(newName4,newName6)

    tmpPath1 = tmpPath.replace(".ttx","-fix.ttx")

    # insert new names 4 into ttx
    command = "xml ed -u '//*/namerecord[@nameID=\"4\"]' -v '" + newName4 + "' " + tmpPath + " > " + tmpPath1
    print(subprocess.check_output(command, shell=True))

    tmpPath2 = tmpPath1.replace(".ttx","-fix.ttx")

    # insert new name 6 into ttx
    command = "xml ed -u '//*/namerecord[@nameID=\"6\"]' -v '" + newName6 + "' " + tmpPath1 + " > " + tmpPath2
    print(subprocess.check_output(command, shell=True))

    # make tmpPath back into font file
    command = "ttx " + tmpPath2
    print(subprocess.check_output(command, shell=True))

    os.remove(path)
    os.remove(tmpPath)
    os.remove(tmpPath1)
    os.remove(tmpPath2)

    os.rename(path.replace(".ttf","-fix-fix.ttf"),path)

# check if path is file
if os.path.isfile(path):
    ttxAndFix(path)

if os.path.isdir(path):
    print("is dir")
    for file in os.listdir(path):
        ttxAndFix(path + "/" + file)
