__doc__ = """
    Use to add a suffix to the family name of a font that has has an opentype feature "frozen" with pyftfeatfreeze.py

    Adds a suffix to names 1, 3, 4, and 6.

    USAGE

    From the command line or a shell script, run:

    python SCRIPT/PATH/add-smallcaps-suffix.py [FONT/PATH/font.ttf] [suffix]
"""

import sys
import os
import subprocess

# ---------------------------------------------------------------------
# capture args from command line cue ----------------------------------

path = sys.argv[-2]
suffix = sys.argv[-1]

# ---------------------------------------------------------------------
# make command line calls more convenient -----------------------------

# run command without grabbing the output
def run(command):
    print('----------')
    print('running  → ', command)
    print('----------')
    return subprocess.call(command, shell=True)

# run command and return the output
def get(command):
    print('----------')
    print('checking → ', command)
    print('----------')
    # also strips out xml junk
    return str(subprocess.check_output(command, shell=True)).replace("b'","").replace("'","").replace('\\n','').replace('  ','')

# ---------------------------------------------------------------------
# TTX the input TTF file ----------------------------------------------

ttxPath = path.replace('.ttf', '.ttx')
run("ttx " + path)

# ---------------------------------------------------------------------
# get nameID values ----------------------------------------------

def getNameId(num):
    return get('xml sel -t -v "//*/namerecord[@nameID=\''+ str(num) + '\']" ' + ttxPath)

namesToEdit = {}

def getNameIdValues(*args):
    for arg in args:
        namesToEdit[arg] = (getNameId(arg))

getNameIdValues(1,3,4,6)

print(namesToEdit)