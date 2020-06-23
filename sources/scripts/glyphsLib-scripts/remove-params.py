# import sys
from glyphsLib import CustomParametersProxy
# from glyphsLib import GSFont

font = Glyphs.font

for instance in font.instances:
	
# 	del instance.customParameters[:]
# 	help(instance.customParameters)
	print(len(instance.customParameters))
	if len(instance.customParameters) > 0:
		params = []
		for param in instance.customParameters:
			params.append(param.name)
			print(param.name)
		for name in params:
			del(instance.customParameters[name])
	# 		break
	print(instance.customParameters)
# 	break
# 	break
		