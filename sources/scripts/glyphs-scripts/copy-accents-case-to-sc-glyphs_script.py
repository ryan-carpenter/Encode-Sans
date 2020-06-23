#MenuTitle: Copy Anchors from case to SC accents
# -*- coding: utf-8 -*-
"""
    Duplicate anchors in glyphs from `.case` comb accents to `.sc` comb accents.

    Only helpful when SC accents are very similar to cap accents.
"""

font = Glyphs.font

for glyph in font.glyphs:
    # if glyph is a "comb" accent, will export, and is not slashshort or ogonek
    if "comb" in glyph.name and ".sc" in glyph.name and glyph.export == True and "slashshort" not in glyph.name and "ogonek" not in glyph.name:
        # get cap version glyph name
        caseGlyphName = glyph.name.replace('.sc','.case')

        # make sc anchors the same as cap version anchors (if the accents are very similar)
        for layer in glyph.layers:
            thisLayer = layer.layerId
            if font[caseGlyphName] in font.glyphs:
                layer.anchors = font[caseGlyphName].layers[thisLayer].anchors

            # # TODO: get this working ... it current increases y pos of both .sc AND .case glyphs
            # for anchor in layer.anchors:
            #     # only if the the anchor is "top" and the glyph is combined (e.g. "dieresiscomb_macroncomb") and ".sc"
            #     if anchor.name == "top" and "_" in glyph.name and ".sc" in glyph.name:
            #         # get y pos of "top" in cap accent, then add 40 units
            #         newYPos = font[caseGlyphName].layers[thisLayer].anchors["top"].position.y + 40
            #         # update position of sc top anchor
            #         anchor.position = NSPoint(anchor.position.x, newYPos)
