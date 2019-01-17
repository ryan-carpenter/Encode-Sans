#MenuTitle: Split Normal-width Masters, Encode Sans
# -*- coding: utf-8 -*-
"""
    Makes a copy of a GlyphsApp source, with adjustments to designspace by:
    - making masters from interpolated normal-width light and bold instances
    - deleting wide and condensed masters

    Specific to Encode Sans for now. Assumes:
    - "Width" is the second axis
    - Normal-width instances are given "Width" axes value of 500
    - Instances are sorted by weight, with lightest and boldest at each end

    To use, symlink this script into glyphs script folder with:

    ln -s THIS/PATH/sources/scripts/helpers/split-encode-vf-glyphs_script.py GLYPHS/SCRIPTS/PATH/prep-designspace-glyphs_script.py
"""
sourceFont = Glyphs.font

sourcePath = sourceFont.filepath

widthAxisIndex = 1

widthsDict = {}

for instance in sourceFont.instances:
    width = int(instance.axes[widthAxisIndex])
    if width not in widthsDict:
        # make a key for the width, and add the name of that width
        try:
            widthsDict[width] = instance.customParameters["familyName"].replace("Encode Sans ","")
        except AttributeError:
            widthsDict[width] = "normal"

# runs once per width family to save a new, split source
def splitGlyphsSource(widthValue, widthName):

    Glyphs.open(sourcePath)
    font = Glyphs.font

    # ============================================================================
    # delete other width instances ===============================================

    instancesToRemove = []

    for index, instance in enumerate(font.instances):
        if instance.axes[widthAxisIndex] != widthValue:
            instancesToRemove.append(index)

    instancesToRemove = sorted(instancesToRemove)

    for instanceIndex in instancesToRemove[::-1]:
        print(instanceIndex)
        del font.instances[instanceIndex]



    # ============================================================================
    # make masters from instance designspace corners =============================

    print("Making masters from normal-width corner instances:")

    def copyFromInterpolatedFont(instanceIndex):
        instanceFont = font.instances[instanceIndex].interpolatedFont

        instanceFontMasterID = instanceFont.masters[0].id

        font.masters.append(instanceFont.masters[0])
        newMasterID = instanceFontMasterID # these are the same; copying for clarity below

        print("\n=================================")
        print("Instance Weight: " + str(font.instances[instanceIndex].weightValue))

        # copy glyphs from instance font to new master
        for index,glyph in enumerate(font.glyphs): # (you can use font.glyphs()[:10] to do the first 10 glyphs only while making/testing script)
            instanceGlyph = instanceFont.glyphs[index] # make variable for glyph of interpolated font
            glyph.layers[instanceFontMasterID] = instanceGlyph.layers[instanceFontMasterID]

        # bring kerning in from interpolated font # not yet working
        font.kerning[instanceFontMasterID] = instanceFont.kerning[instanceFontMasterID]

    copyFromInterpolatedFont(0)
    copyFromInterpolatedFont(-1)

    # ============================================================================
    # remove old masters and update axis values ==================================

    # deletes masters that aren't the current width – would need more flexibility to be abstracted to other fonts

    mastersToDelete = []

    for index, master in enumerate(font.masters):
        print(master.axes[widthAxisIndex])
        # round this axis value, because it might interpolate to be very slightly different
        if round(master.axes[widthAxisIndex]) != widthValue:
            mastersToDelete.append(index)
    
    # if len(mastersToDelete) == 2:
    #     mastersToDelete.append(2) # add third master to delete list (it's empty)
    #     mastersToDelete.append(3) # add fourth master to delete list (it's empty)

    # check if the incoming masters are (empty) duplicates, as happens in width extremes
    mastersToDeleteByID = []
    for layer in font["a"].layers:
        print(layer.paths)
        if len(layer.paths) == 0:
            print("yo")
            mastersToDeleteByID.append(layer.layerId)
    for index, master in enumerate(font.masters):
        if master.id in mastersToDeleteByID:
            mastersToDelete.append(index)

    for layer in font["a"].layers:
        print(layer)

    # TODO: sort logic to work in expanded masters ... 

    print(mastersToDelete)

    for masterIndex in mastersToDelete[::-1]:
        print(font.masters[masterIndex])
        font.removeFontMasterAtIndex_(masterIndex)

    # ============================================================================
    # update master metadata =====================================================

    # Clean up master names
    for master in font.masters:
        if "Light" in master.name or "Thin" in master.name:
            master.name = "Light"
        if "Bold" in master.name or "Black" in master.name:
            master.name = "Bold"

    # ============================================================================
    # update instance metadata ===================================================

    # remove "familyName" Custom Param
    for instance in font.instances:
        if "familyName" in instance.customParameters:
            del(instance.customParameters['familyName'])

        # set "Width" to "Medium (Normal)"
        instance.width = "Medium (normal)"

    # # ============================================================================
    # # set varfont axes ===========================================================

    fontAxes = [
        {"Name": "Weight", "Tag": "wght"}
    ]
    font.customParameters["Axes"] = fontAxes

    for master in font.masters:
        print("master.axes are " + str(master.axes))

    # for instance in font.instances:
    #     print("instance.axes are " + str(instance.axes))

    # ============================================================================
    # round all coordinates ======================================================

    for glyph in font.glyphs:
        for layer in glyph.layers:
            for path in layer.paths:
                for node in path.nodes:
                    node.position.x = round(node.position.x)
                    node.position.y = round(node.position.y)
            for anchor in layer.anchors:
                anchor.x = round(anchor.x)
                anchor.y = round(anchor.y)
        

    # ============================================================================
    # save as "build" file =======================================================

    buildreadyFolder = 'split'
    buildreadySuffix = widthName.lower()

    fontPath = font.filepath

    if buildreadyFolder not in fontPath:    
        fontPathHead = os.path.split(fontPath)[0] # file folder
        fontPathTail = os.path.split(fontPath)[1] # file name
        buildreadyPathHead = fontPathHead + "/" + buildreadyFolder + "/"

        if os.path.exists(buildreadyPathHead) == False:
            os.mkdir(buildreadyPathHead)

        buildPath = buildreadyPathHead + fontPathTail.replace(".glyphs", "-" + buildreadySuffix + ".glyphs")

    else:
        buildPath = fontPath.replace(".glyphs", "-" + buildreadySuffix + ".glyphs")

    if widthName != "normal":
        print(font.familyName + " " + widthName)
        font.familyName = font.familyName + " " + widthName

    font.save(buildPath)

    # # close original without saving
    font.close()

    Glyphs.open(buildPath)

# call splitter
for key in widthsDict:
    print(key)
    print(widthsDict[key])
    splitGlyphsSource(key, widthsDict[key])

## to produce a specific width only, uncomment one (or more) of these
# splitGlyphsSource(1000, "Expanded")
# splitGlyphsSource(750, "SemiExpanded")
# splitGlyphsSource(500, "normal")
# splitGlyphsSource(250, "SemiCondensed")
# splitGlyphsSource(0, "Condensed")