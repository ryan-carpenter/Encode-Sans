#MenuTitle: Make comb accents zero-width
# -*- coding: utf-8 -*-
"""
    Give combining accents zero-width in Encode Sans.

	UPDATE: this was a bad idea, as the GlyphsApp UI doesn't really work 
	for no-width glyphs due to merged text & edit views.
"""

font = Glyphs.font

for glyph in font.glyphs:
	if "comb" in glyph.name and not any(substring in glyph.name for substring in ["o.comb", "slashcomb"]):
		print(glyph.name)
		if "macron" in glyph.name:
			# loop through layers and make zero width + centered
			for layer in glyph.layers:
				layer.LSB = 0
				layer.RSB = 0
				layer.LSB = -1 * layer.width/2
				layer.width = 0
		