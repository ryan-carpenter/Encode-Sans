"""
	Glyphs script to add wght axis mapping to font.

	WARNING: As of Apr 29, 2020, adding this axis mapping doesn't help 
	glyphsLib to produce an accurate <map> in a designspace.
"""

font = Glyphs.font

MAPPING = {
	"wght": {
		
	}
}

for instance in font.instances:
	if instance.weightValue not in MAPPING['wght'].keys():
		MAPPING['wght'][instance.weightValue] = instance.customParameters["weightClass"]

font.customParameters["Axis Mappings"] = MAPPING

print(font.customParameters["Axis Mappings"])