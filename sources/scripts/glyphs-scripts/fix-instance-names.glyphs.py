"""
	Fixed instance stylenames in source. Must be run within GlyphsApp.
"""

font = Glyphs.font

for instance in font.instances:
	if "familyName" in instance.customParameters:
		print instance.customParameters["familyName"]
		instance.customParameters["familyName"] = instance.customParameters["familyName"].replace("Semi ", "Semi")
		instance.name = instance.customParameters["familyName"].replace("Encode Sans ","") + " " + instance.name