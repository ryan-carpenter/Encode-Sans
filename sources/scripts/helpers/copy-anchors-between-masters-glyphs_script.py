#MenuTitle: Copy Anchors between Masters
# -*- coding: utf-8 -*-
"""
    Duplicate anchors in glyphs of one master to all others in a GlyphsApp source.

    This helps keep anchors in sync. It is only a tool in the process – you should still adjust final anchor place manually.
"""

# masterToCopyFrom = "Light Extended"

# ================================================

# import json
# font = Glyphs.font

# numMasters = font.masters

# masterIDs = []

# # get id of masterToCopyFrom

# for master in font.masters:
#     masterIDs.append(master.id)
#     if master.name == masterToCopyFrom:
#         masterToCopyFromID = master.id

# print(masterToCopyFromID)

# glyphAnchors = {}

# for glyph in font.glyphs:
#     glyphAnchors[glyph.name] = {}
#     for layer in glyph.layers:
#         if layer.layerId in masterIDs:
#             if len(layer.anchors) >= 1:
#                 glyphAnchors[glyph.name][layer.name] = []
#                 for anchor in layer.anchors:
#                     glyphAnchors[glyph.name][layer.name].append(str(anchor.name))

# # print(glyphAnchors)

# # copy the anchors
# # def duplicateAnchors(glyph):
#     # make anchors in all non-masterToCopyFrom layers
#     # copy x,y pos from masterToCopyFrom
#     # color glyph yellow

# # for index, key in enumerated(sorted(glyphAnchors)):
# for index, (key, value) in enumerate(glyphAnchors.items()):
#     if glyphAnchors[key] == {}:
#         del glyphAnchors[key]
#     # else:
#         # print "%s: %s" % (key, glyphAnchors[key])

#     # if anchors names in all lists are the same
#         # del this dict item
#     else:
#         layersWithAnchors = 0
#         for subKey in key:
#             layersWithAnchors += 1

#         if layersWithAnchors == len(font.masters) - 1:
#             anchorsInAllMasters = True


#         anchorsList = glyphAnchors[key].values()[0]
#         # print(glyphAnchors[key].values()[0])
#         # # # yields True if list of anchor names is equivalent between layers
#         sameAnchors = all(value == anchorsList for value in glyphAnchors[key].values())

#         print(sameAnchors)

#     #     # ("top","_top", "bottom", "_bottom")


#         if anchorsInAllMasters == True and sameAnchors == True:
#             del glyphAnchors[key]

# print(json.dumps(glyphAnchors, indent=4, sort_keys=True))


# ================================================

# singleAnchorAccents = []

# for glyph in font.glyphs:
#     if "comb" in glyph.name and glyph.export == True:
#         for layer in glyph.layers:
#             if len(layer.anchors) <= 1:
#                 singleAnchorAccents.append(glyph.name)
#                 layer.anchors = glyph.layers[masterToCopyFromID].anchors

# for glyphName in set(singleAnchorAccents):
#     print("/" + glyphName)


# ================================================


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
    if "comb" in glyph.name:
        for anchor in layerToChange.anchors:
            print(anchor)
            if anchor.x == 600:
                anchor.x = glyph.width/2
                print(str(anchor), " at ", str(glyph.width/2))

        if layerToChange.width == 800:
            layerToChange.LSB += 200

            

# store width, LSB, and RSB
# make glyph width equal 1200