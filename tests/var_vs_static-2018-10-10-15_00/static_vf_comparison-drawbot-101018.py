W,H = 860*2, 340*2

resolution = 2

newPage(W,H)

rect(0,0,W,H)

testString = "In statistical modeling, regression analysis is a set of statistical processes for estimating the relationships among variables. It includes many techniques for modeling and analyzing several variables, when the focus is on the relationship between a dependent variable and one or more independent variables (or 'predictors'). More specifically, regression analysis helps one understand how the typical value of the dependent variable (or 'criterion variable') changes when any one of the independent variables is varied, while the other independent variables are held fixed. \n \nMost commonly, regression analysis estimates the conditional expectation of the dependent variable given the independent variables – that is, the average value of the dependent variable when the independent variables are fixed. Less commonly, the focus is on a quantile, or other location parameter of the conditional distribution of the dependent variable given the independent variables. In all cases, a function of the independent variables called the regression function is to be estimated. In regression analysis, it is also of interest to characterize the variation of the dependent variable around the prediction of the regression function using a probability distribution. A related but distinct approach is Necessary Condition Analysis[1] (NCA), which estimates the maximum (rather than average) value of the dependent variable for a given value of the independent variable (ceiling line rather than central line) in order to identify what value of the independent variable is necessary but not sufficient for a given value of the dependent variable."
setLineHeight = 18*resolution
setFontSize = 16*resolution
# xPos, yPos = 80, 664
xPos, yPos = W/20,H/20 
txtW, txtH =  W-(W/10),H-(H/10)

testName = "glyphs_decomp_VF_vs_static"

varWght = 400.0

lineHeight(setLineHeight)

# linking a specific font file for testing
# font("../google-fonts-static/Encode_Sans/EncodeSans-Regular.ttf", setFontSize)
font("./EncodeSans-Regular.ttf", setFontSize)
fill(1,0,1)
 
textBox(testString, (xPos, yPos, txtW, txtH))

# Linking a specific font file for testing. The text() method fails for this font, even though the font works as expected in FontView and on Axis-Praxis.org
font("./glyphs/EncodeSansGX-decomposed.ttf", setFontSize)



# # It *does* work if I link to another variable font, such as Avenir Next Variable.
# font("AvenirNext_Variable.ttf", setFontSize)


for axis, data in listFontVariations().items():
    print((axis, data))

# when I set the fontVariations, the following text() method fails with NSInvalidArgumentException
fontVariations(wght=varWght,wdth=500.0)

blendMode("screen")
fill(0,1,0)

# I recieve a NSInvalidArgumentException here, which Apple describes as "Name of an exception that occurs when you pass an invalid argument to a method, such as a nil pointer where a non-nil object is required." However, I only receive this error when I set the font variations of the above variable font. So, the arguments should be valid.
# text(testString, (xPos, yPos))
textBox(testString, (xPos, yPos, txtW, txtH))

rotate(90)
fontSize(12*resolution)
fill(0.8)
tracking(1)

text(testName.replace("_", " "), (H-(H/17), -(W/32)), align="right")

saveImage(f"image-exports/encode-diff_test-{testName}-2018_10_10.png")
