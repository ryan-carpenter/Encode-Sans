__doc__ = """
    Use to go through TTF/OTF files in a given directory and shorten their name IDs 4 & 6 to abbreviated names.

    Requires Python 3, TTX, & xmlStarlet.

    Assumes there are not any ttx files lurking in the directory you provide.

    Usage:
    - Add to the "abbreviations" dictionary if you have other long words (or partial words) in your font's style name
    - Run on the command line (or from a shell script) with the following syntax:

    python SCRIPT/PATH/shorten-nameID-4-6.py FONT/PATH/font.otf

    ...or for a folder of fonts:

    python SCRIPT/PATH/shorten-nameID-4-6.py FONT/PATH

"""

import sys
import os
import subprocess

path = sys.argv[-1]

print('------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------')
print('abbreviating nameIDs 4 & 6 in ' + path)
print('------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------')

abbreviations = {
    "Condensed": "Cond",
    "Expanded": "Expd",
    "Extra": "X",
    "Light": "Lght",
    "Regular": "Reg",
    "Medium": "Med"
}

def abbreviate(name):
    # print(name)
    # name = name.replace("'","")
    name = name.replace("b","").replace("'","")

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

    # get name of TTX file
    if path.lower().endswith('.ttf'):
       tmpPath = path.replace(".ttf",".ttx")
    elif path.lower().endswith('.otf'):
       tmpPath = path.replace(".otf",".ttx")

    # make command to select nameID 4, then abbreviate it and make it a variable
    command = 'xml sel -t -v "//*/namerecord[@nameID=\'4\']" ' + tmpPath
    print('')
    print('----------')
    print('checking → ', command)
    print('----------')
    output = str(subprocess.check_output(command, shell=True))
    newName4 = abbreviate(output)

    # repeat for nameID 6
    command = 'xml sel -t -v "//*/namerecord[@nameID=\'6\']" ' + tmpPath
    print('')
    print('----------')
    print('checking → ', command)
    print('----------')
    output = str(subprocess.check_output(command, shell=True))
    newName6 = abbreviate(output)

    print('')
    print("newName4 is ", newName4)
    print("newName6 is ", newName6)
    print('')

    # tmpPath1 = tmpPath.replace(".ttx","-fix.ttx")

    # insert new names 4 into ttx
    command = "xml ed --inplace -u '//*/namerecord[@nameID=\"4\"]' -v '" + newName4 + "' " + tmpPath
    print('')
    print('----------')
    print('running  → ', command)
    print('----------')
    subprocess.call(command, shell=True)

    # tmpPath2 = tmpPath1.replace(".ttx","-fix.ttx")

    # insert new name 6 into ttx
    command = "xml ed --inplace -u '//*/namerecord[@nameID=\"6\"]' -v '" + newName6 + "' " + tmpPath
    print('')
    print('----------')
    print('running  → ', command)
    print('----------')
    subprocess.call(command, shell=True)


    os.remove(path)
    # os.remove(tmpPath1)
    # os.remove(tmpPath2)

    # make tmpPath back into font file
    # command = "ttx " + tmpPath2
    command = "ttx " + tmpPath
    print('')
    print('----------')
    print('running  → ', command)
    print('----------')
    subprocess.call(command, shell=True)

    os.remove(tmpPath)

# check if path is file
if os.path.isfile(path):
    ttxAndFix(path)

if os.path.isdir(path):
    print("is dir")
    for file in os.listdir(path):
        ttxAndFix(path + "/" + file)
