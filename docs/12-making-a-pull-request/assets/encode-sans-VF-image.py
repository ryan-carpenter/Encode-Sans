from glyphNames import *;

W, H = 800, 1200

newPage(W,H)

# fill(0.1)
fill(0.1,0.1,0.25)
rect(0,0,W,H)

# fill(0.8)

charSet = FormattedString()

# charSet.font("./EncodeSans-VF.ttf")
charSet.font("../../../fonts/encodesanscondensed/static/EncodeSansCondensed-SemiBold.ttf")
# charSet.fontVariations(wght=400.0,wdth=100.0)

# fontSizing = 30
fontSizing = 26

charSet.fontSize(fontSizing)
charSet.align("justified")
charSet.lineHeight(fontSizing*1.78)
# charSet.tracking(0.32)
charSet.tracking(4.5)
charSet.fill(1)
# charSet += glyphSet

for glyph in glyphNames:
    # print(glyph)
    charSet.appendGlyph(glyph)
    
padding = 20

stroke(1)

# rect(padding, 0, W-padding*2, H-padding)

# charSet.appendGlyph(listFontGlyphNames())
textBox(charSet, (padding, -8, W-padding*2, H-padding/2))
# print(charSet)

# saveImage("charset.pdf")


fill(1,0,0)

fontName= FormattedString()

fontSizing = 440

fontName.fill(1,1,1,0.25)
fontName.fontSize(fontSizing)
fontName.tracking(0)
fontName.align("center")
fontName.font("../../../fonts/encodesansexpanded/static/EncodeSansExpanded-Black.ttf")
fontName.lineHeight(fontSizing*.85)
fontName += "EN\n"
fontName += "CO\n"
fontName += "DE"



textBox(fontName, (padding, 0, W-padding*2, H-padding*1.3))


saveImage("charset-tall3.png", imageResolution=144)
