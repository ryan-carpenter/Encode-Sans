#MenuTitle: Copy Anchors between Masters
# -*- coding: utf-8 -*-
"""
    Duplicate anchors in glyphs of one master to all others in a GlyphsApp source.

    This helps keep anchors in sync. It is only a tool in the process – you should still adjust final anchor place manually.
"""

# masterToCopyFrom = "Light Extended"

# ================================================

# import json
font = Glyphs.font

# ================================================

singleAnchorAccents = []

for glyph in font.glyphs:
    if "comb" in glyph.name and glyph.export == True:
        for layer in glyph.layers:
            if len(layer.anchors) <= 1:
                singleAnchorAccents.append(glyph.name)
                layer.anchors = glyph.layers[masterToCopyFromID].anchors

for glyphName in set(singleAnchorAccents):
    print("/" + glyphName)


# ================================================
# set non-1200-unit combining marks to 1200 units

masterToAdjustAccentWidthsIn = "Light Condensed"


# import json
font = Glyphs.font

numMasters = font.masters

masterIDs = []

# get id of masterToCopyFrom

for master in font.masters:
    masterIDs.append(master.id)
    if master.name == masterToAdjustAccentWidthsIn:
        masterToAdjustAccentWidthsIn = master.id

# move anchors to midpoint
for glyph in font.glyphs:
    layerToChange = glyph.layers[masterToAdjustAccentWidthsIn]
    if "comb" in glyph.name and "o.comb" not in glyph.name:
    # if "dotaccentcomb.sc" == glyph.name and "o.comb" not in glyph.name:
        widthAndSides = [layerToChange.width, layerToChange.LSB, layerToChange.RSB]
        print(glyph.name, layer.name)
        print(widthAndSides)
        newWidth = 1200

        # if the layer isn't the desired width, AND if it has zero components
        if layerToChange.width != newWidth and len(layerToChange.components) == 0:

            # get current total margins
            marginOld = widthAndSides[0] - (widthAndSides[0] - widthAndSides[1] -  widthAndSides[2])
            # get the portion of the margin that is on the left
            leftPortionOfFreeSpace = widthAndSides[1] / marginOld

            # set the width of the layer initially
            layerToChange.width = newWidth

            # calculate new total margin
            marginNew = newWidth - (newWidth - layerToChange.LSB - layerToChange.RSB)
            # set new left margin
            layerToChange.LSB = marginNew * leftPortionOfFreeSpace
            # then reset the width again (this will have changed)
            layerToChange.width = newWidth

        if layerToChange.width != newWidth and len(layerToChange.components) != 0:
            layerToChange.width = newWidth

        for anchor in layerToChange.anchors:
            print(anchor)
            if anchor.x == widthAndSides[0]/2:
                anchor.x = newWidth/2
                print(str(anchor), " at ", str(newWidth/2))

# ====================================================


