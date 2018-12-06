from glyphNames import *;

W, H = 1000, 1000

fill(0.1)
rect(0,0,W,H)

fill(0.8)

charSet = FormattedString()

# charSet.font("./EncodeSans-VF.ttf")
charSet.font("../../../fonts/encodesanscondensed/static/EncodeSansCondensed-Bold.ttf")
# charSet.fontVariations(wght=400.0,wdth=100.0)

fontSizing = 32
charSet.fontSize(fontSizing)
charSet.align("justified")
charSet.lineHeight(fontSizing*1.6)
charSet.tracking(0.25)
charSet.fill(1)
# charSet += glyphSet

for glyph in glyphNames:
    # print(glyph)
    charSet.appendGlyph(glyph)
    
padding = 20

stroke(1)

# rect(padding, 0, W-padding*2, H-padding)

# charSet.appendGlyph(listFontGlyphNames())
textBox(charSet, (padding, 0, W-padding*2, H-padding/2-4))
# print(charSet)

saveImage("charset.pdf")


fill(1,0,0)

fontName= FormattedString()

fontSizing = 360

fontName.fill(1,1,1,0.375)
fontName.fontSize(fontSizing)
fontName.tracking(0)
fontName.align("center")
fontName.font("../../../fonts/encodesansexpanded/static/EncodeSansExpanded-Black.ttf")
fontName.lineHeight(fontSizing*.85)
fontName += "EN\n"
fontName += "CO\n"
fontName += "DE"



textBox(fontName, (padding, 0, W-padding*2, H-padding*1.6))


saveImage("charset.pdf")
