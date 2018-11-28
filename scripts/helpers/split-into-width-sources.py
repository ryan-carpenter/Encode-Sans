from Glyphs import *
import sys
import os
import re
import objc

# run on GlyphsApp source with a rectangular designspace (use designspace fix script to do so)

# families must be labeled using instance custom parameter `familyName`

relPath = sys.argv[-1]
filename = os.path.split(relPath)[1] # get just the filename
fileHead = os.path.split(relPath)[0]
directory = os.getcwd()
document = Glyphs.open((str(directory + "/" + relPath)), False)
font = document.font()

# get overall family name

typeFamilyName = font.familyName()

print(typeFamilyName)

# if axes besides Weight & Width exist, get this as a dictionary
for param in font.customParameters():
    if param.name() == "Axes":
        styleAxes = param.value()

# make list for custom-axis families
splitFamilies = []

# go through instances
for instance in font.instances():
    # print(instance)
    # for customParameters
    for param in instance.customParameters():
        # print(param.name(), param.value())
        # if familyName param exists, add param to splitFamilies list
        if param.name() == "familyName":
            splitFamilies.append(param.value())

        # font is default/normal style – add normal family name to list
        else:

            splitFamilies.append(typeFamilyName)


# de-duplicate families list
splitFamilies = set(splitFamilies)

print(splitFamilies)


# make new glyph font doc for each familyName in list
for currentFamilyName in splitFamilies:

    buildFileName = currentFamilyName.replace(" ", "-") + "-build.glyphs"
    buildFilePath = directory + "/" + fileHead + "/" + buildFileName

    # print(buildFilePath)
    font.save((buildFilePath))

    currentDocument = Glyphs.open((buildFilePath), False)

    currentFont = currentDocument.font()

    # TODO: make currentFont family name = currentFamilyName

    # make list of current instances, delete others
    currentInstances = []

    for index, instance in enumerate(currentFont.instances()):

        hasFamilyNameParam = False
        
        for param in instance.customParameters():
            # if it has a "familyName" param
            if param.name() == "familyName":
                hasFamilyNameParam = True
                # and if the value is the currentFamilyName
                if param.value() == currentFamilyName:
                    currentInstances.append(index)

        # if there's not a "familyName" param and the currentFamilyName matches the overall name, it's a default style
        if hasFamilyNameParam == False and currentFamilyName == typeFamilyName:
            currentInstances.append(index)
            # print(instance.interpolationWidth())

    print(currentInstances, currentFamilyName)

    # in each new file, delete instances that don't match the current width

    deleteCounter = 0
    indexCounter = 0

    for instance in currentFont.instances():
        if indexCounter not in currentInstances:
            currentFont.removeObjectFromInstancesAtIndex_(deleteCounter)

        if indexCounter in currentInstances:
            deleteCounter += 1
        
        indexCounter += 1

    currentFont.save((buildFilePath))
    currentDocument.close(True)

    # make masters from each end of that instance for the current secondary axis
        # ~MAKE DEF ABOVE~ make master from instance makeMaster(instance, index) # 
            # get instance.interpolatedFont
            # f.masters.append(instanceFont.masters[index])
            # get new master ID
            # copy in glyphs
            # copy in kerning

    # assumes instances are ordered by weight value (this may need to be an added step above)

    currentLightFont = currentFont.generateInstance_error_(currentFont.instances()[0], None)
    currentBoldFont = currentFont.generateInstance_error_(currentFont.instances()[-1], None)

    print(currentLightFont.fontMasters()[0])
    print(currentBoldFont.fontMasters()[0])

    currentLightFontMasterID = currentLightFont.fontMasters()[0].id()
    currentBoldFontMasterID = currentBoldFont.fontMasters()[0].id()

    # currentFont.fontMasters().append(currentLightFont.fontMasters[0])
    # currentFont.fontMasters().append(currentBoldFont.fontMasters[0])
    # currentFont.insertFontMaster_atIndex_(currentLightFont.fontMasters()[0], 0)
    # currentFont.insertFontMaster_atIndex_(currentBoldFont.fontMasters()[0],1)
    currentFont.addFontMaster_(currentLightFont.fontMasters()[0])
    currentFont.addFontMaster_(currentBoldFont.fontMasters()[0])

    newLightMaster = currentFont.fontMasters()[-2]
    newBoldMaster = currentFont.fontMasters()[-1]
    newLightMasterID = newLightMaster.id()
    newBoldMasterID = newBoldMaster.id()

    for index,glyph in enumerate(currentFont.glyphs()):
        # make variable for glyph of interpolated font
        # currentGlyph = currentFont.glyphs()[glyph.name()]
        currentGlyph = currentFont.glyphs()[index]

        ## these need to be layer indexes, it seems
        # bring glyph data into glyph of new master
        glyph.layers()[newMasterID] = currentGlyph.layers()[currentLightFontMasterID]
        # bring glyph data into glyph of new master
        glyph.layers()[newMasterID] = currentGlyph.layers()[currentBoldFontMasterID]

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