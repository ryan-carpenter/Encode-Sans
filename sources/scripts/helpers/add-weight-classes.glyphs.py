"""
	Set correct weightClass values for instances in Glyphs source.
"""

WEIGHTS = {
	"Thin": 		100,
	"ExtraLight": 	200,
	"Light":		300,
	"Regular":		400,
	"Medium":		500,
	"SemiBold":		600,
	"Bold":			700,
	"ExtraBold":	800,
	"Black":		900
}


font = Glyphs.font

for instance in font.instances:
	for weightName in WEIGHTS.keys():
		if weightName in instance.name.split(" "):
			instance.customParameters["weightClass"] = WEIGHTS[weightName]
			# print instance.name, WEIGHTS[weightName]
