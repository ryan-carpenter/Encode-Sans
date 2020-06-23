#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

Run this file with [PATH]/add-fontlog.py [PATH]/README.md [PATH]/AUTHORS.txt

Modified version of https://github.com/fonts/skeleton/blob/skeleton/tools/FONTLOG.py

The FONTLOG is SIL’s concept of a chancelog for a font. When doing a release, 
we generate one automatically based on AUTHORS.txt, README.txt and the 
repository history.
An example of a FONTLOG:
http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=OFL-FAQ_web#11bc4f28
(pretty url’s wouldn’t hurt the SIL)
We use a line-width of 82 because I manually wrapped my commit messages to 78, 
and git indents them with 4 spaces. These lines stay like they are, and 
unwrapped commit messages get wrapped to the same width.
"""

from textwrap import fill, TextWrapper
from subprocess import Popen, PIPE
import sys

readmePath = sys.argv[-2]
authorsPath = sys.argv[-1]

# Get the data

README = open(readmePath)

AUTHORS = open(authorsPath)

LOG = Popen(['git','log','--reverse'], stdout=PIPE)

# Setup TextWrap instances

wrapper = TextWrapper(width=82)
commit_msg_wrapper = TextWrapper(subsequent_indent='    ', width=30)

# make/open FONTLOG file
fontlog= open("FONTLOG.txt","w+")

for line in README:
    wrappedText = wrapper.fill(line)
    fontlog.write(wrappedText + "\n")

fontlog.write("\n\n")
fontlog.write("____")
fontlog.write("\n\n")
fontlog.write("Designers:")
fontlog.write("\n\n")

for line in AUTHORS:
    if line[0] != "#":
        fontlog.write(AUTHORS.read().split("with Reserved Font Name")[0]) # Above there, it lists the designers

fontlog.write("\n\n")
fontlog.write("____")
fontlog.write("\n\n")
fontlog.write("Changelog:")
fontlog.write("\n\n")


for line in LOG.stdout:
    fontlog.write(line.decode("utf-8"))

# close file
fontlog.close() 