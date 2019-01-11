#MenuTitle: Copy Anchors from case to SC accents
# -*- coding: utf-8 -*-
"""
    Duplicate anchors in glyphs from `.case` comb accents to `.sc` comb accents.
"""

font = Glyphs.font

for glyph in font.glyphs:
    if "comb" in glyph.name and ".sc" in glyph.name and glyph.export == True and "slashshortcomb" not in glyph.name and "ogonek" not in glyph.name:
            caseGlyphName = glyph.name.replace('.sc','.case')
            print(caseGlyphName)
            for layer in glyph.layers:
                thisLayer = layer.layerId
                if font[caseGlyphName] in font.glyphs:
                    layer.anchors = font[caseGlyphName].layers[thisLayer].anchors

                # TODO: get this working? It current increase y pos of .sc AND .case glyphs
                for anchor in layer.anchors:
                    if "_" in glyph.name and ".sc" in glyph.name and anchor.name == "top":
                        anchor.position = NSPoint(anchor.position.x, anchor.position.y+40)
