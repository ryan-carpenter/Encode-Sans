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

    # make list of current instances, delete others
    currentInstances = []
    # if instance customParameters familyName = currentFamilyName:

    

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
            # print(instance.interpolationWidth())
            currentInstances.append(index)

        # if index not in currentInstances:
        #     print("remove instance " + str(index))
        #     # currentFont.removeObjectFromInstancesAtIndex(index)
        #     # del currentFont.instances()[index]
        #     currentFont.removeObjectFromInstancesAtIndex_(index)


    print(currentInstances, currentFamilyName)

    delCounter = 0
    idxCounter = 0

    for instance in currentFont.instances():
        if idxCounter not in currentInstances:
            # if i in currentFont.instances():
            currentFont.removeObjectFromInstancesAtIndex_(delCounter)
            
        if idxCounter in currentInstances:
            delCounter += 1
        
        idxCounter += 1
            


    #     if index not in currentInstances:
    #         print("remove instance " + str(index))
    #         # currentFont.removeObjectFromInstancesAtIndex(index)
    #         # del currentFont.instances()[index]
    #         currentFont.removeObjectFromInstancesAtIndex_(index)


    currentFont.save((buildFilePath))
    currentDocument.close(True)

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