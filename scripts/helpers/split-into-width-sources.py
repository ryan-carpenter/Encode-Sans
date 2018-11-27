from Glyphs import *
import sys
import os
import re
import objc

# run on GlyphsApp source with a rectangular designspace (use designspace fix script to do so)

filename = sys.argv[-1]
directory = os.getcwd()
document = Glyphs.open((str(directory + "/" + filename)), False)
font = document.font()

# check axes
    # if axis besides "Weight" exists, continue
    # make list of axes

# splitFamilies = []

# go through instances
    # for customParameters
        # if param == familyName
            # add param to list
            # splitFamilies.append(param.familyName)

        ## font is default/normal style
        # else
            # set param = font.familyName (e.g. Encode Sans normal width gets familyName = "Encode Sans")
            # add normal family name to list

# make new glyph font doc for each familyName in list
# for currentFamilyName in splitFamilies:
    # buildFileName as familyName.replace(" ", "-") + "-build"
    # font.save((str(directory + "/" + buildFileName)))

    # document = Glyphs.open((str(directory + "/" + buildFileName)), False)

    # font = document.font()

    # font.familyName() = familyName

    # make list of current instances, delete others
        # currentInstances = []
        # if instance customParameters familyName = currentFamilyName:
            # currentInstances.append(instance)
        # else:
            # delete instance (it'll be used in other build fonts)

        # ? sort currentInstances by weight value ?

    # make masters from each end of that instance for the current secondary axis
        # ~MAKE DEF ABOVE~ make master from instance makeMaster(instance, index) # 
            # get instance.interpolatedFont
            # f.masters.append(instanceFont.masters[index])
            # get new master ID
            # copy in glyphs
            # copy in kerning

        # if instance is instances[0]:
            # makeMaster(instance, index)
        # if instance is instances[-1]:
            # makeMaster(instance, index)

    # delete previous masters
        # for index, master in enumerate(masters):
            # if index != or index == len(masters):
                # delete master

    # delete secondary axis 
        # for axis in font.axes
            # if axis.name != "Weight"
                # del axis

    # font.save((str(directory + "/" + buildFileName)))
    # document.close(True)

# result: should be several fonts, each with just 









## assuming there aren't middle masters for weight

# get lightest and boldest masters

#  


# for instance in font.instances():
#     for param in instance.customParameters():
#         print(param)
#     # print(instance.customParameters)
#     print(instance.interpolatedFont)
    # print(instance.interpolatedFont().font().fontMasters()[0].name())
    # if re.match('^Light$', instance.name()) != None or re.match('^Black$', instance.name()) != None:
    #     print(instance.interpolatedFont().font().fontMasters()[0].name())
    #     font.addFontMaster_(instance.interpolatedFont().font().fontMasters()[0])

# for master in font.fontMasters():
#    print(master.name())


font.save((str(directory + "/" + filename)))
document.close(True)