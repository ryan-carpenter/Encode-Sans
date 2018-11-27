from Glyphs import *
import sys
import os
import re
import objc

filename = sys.argv[-1]
directory = os.getcwd()
document = Glyphs.open((str(directory + "/" + filename)), False)
font = document.font()

for instance in font.instances():
   if re.match('^Light$', instance.name()) != None or re.match('^Black$', instance.name()) != None:
       print instance.interpolatedFont().font().fontMasters()[0].name()
       font.addFontMaster_(instance.interpolatedFont().font().fontMasters()[0])

for master in font.fontMasters():
   print master.name()


font.save((str(directory + "/" + filename + "-test")))
font.close(False)