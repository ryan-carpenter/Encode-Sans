import os
rect(0,0,1000,1000)

testString="Lorem \nTestem \n845"


font("../google-fonts-static/Encode_Sans/EncodeSans-Regular.ttf", 250)
# # also tried using OS tools to see if it might help
# os.chdir("..")
# font("google-fonts-static/Encode_Sans/EncodeSans-Regular.ttf", 250)

# sometimes an error says LucidaGrande is subbing in, but this looks different...
# font("Ludida Grande", 250) 

# fill(1,0,1)
fill(1)
text(testString, (100, 700))

font("EncodeSans-mathfix-normal_wdth-VF.ttf", 250)

# font("var_vs_static-2018-10-08-18_15/EncodeSans-mathfix-normal_wdth-VF.ttf", 250)

# font("RecursiveSans-GothicA", 250) # testing another varfont on my system

for axis, data in listFontVariations().items():
    print((axis, data))

fontVariations(wght=400.0,wdth=500.0)

# # fontVariations(wdth=500.1, wght=400.1)

# # fontVariations(wght=600.0)

# fill(0,.75,1)
fill(0.075)
text(testString, (100, 700))