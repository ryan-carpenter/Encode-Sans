__doc__ = """
    Use to go through TTF/OTF files in a given directory and shorten their name IDs 4 & 6 to abbreviated names.

    Requires TTX & xmlStarlet.
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
    "SemiBold": "SemiBld",
    "Bold": "Bold",
    "ExtraBold": "ExBold",
    "Black": "Blck",
}


# xml ed -u "//*/namerecord[@nameID='4']" -v "
#       ${updatedNameID4}
#     " ${path} > ${path}

# xml ed -u "//*/namerecord[@nameID='6']" -v "
#       ${updatedNameID6}
#     " ${path} > ${path}

def abbreviate(name):
    print(name)

    for key in abbreviations.keys():
        if key in name:
            name = name.replace(key, abbreviations[key])

    print(name)

# check if path is file or dir

if os.path.isfile(path):
    print("is file")

    command = 'xml sel -t -v "//*/namerecord[@nameID=\'4\']" ' + path

    output = str(subprocess.check_output(command, shell=True))

    abbreviate(output)

    # print(output)

    # for key in abbreviations.keys():
    #     if key in output:
    #         print(key, abbreviations[key])
    #         output = output.replace(key, abbreviations[key])

    # print(output)

# if file:
    # do function to edit name id 4 and 6

if os.path.isdir(path):
    print("is dir")
# if dir:
    # for file in dir:
        # do function to edit name id 4 and 6