############################################################
# Simple visual font comparison
# Fonts will show in color where they do not overlap
############################################################

W,H = 860*2, 340*2

resolution = 2

newPage(W,H)

rect(0,0,W,H)

testString = "In statistical modeling, regression analysis is a set of statistical processes for estimating the relationships among variables. It includes many techniques for modeling and analyzing several variables, when the focus is on the relationship between a dependent variable and one or more independent variables (or 'predictors'). More specifically, regression analysis helps one understand how the typical value of the dependent variable (or 'criterion variable') changes when any one of the independent variables is varied, while the other independent variables are held fixed. \n \nMost commonly, regression analysis estimates the conditional expectation of the dependent variable given the independent variables – that is, the average value of the dependent variable when the independent variables are fixed. Less commonly, the focus is on a quantile, or other location parameter of the conditional distribution of the dependent variable given the independent variables. In all cases, a function of the independent variables called the regression function is to be estimated. In regression analysis, it is also of interest to characterize the variation of the dependent variable around the prediction of the regression function using a probability distribution. A related but distinct approach is Necessary Condition Analysis[1] (NCA), which estimates the maximum (rather than average) value of the dependent variable for a given value of the independent variable (ceiling line rather than central line) in order to identify what value of the independent variable is necessary but not sufficient for a given value of the dependent variable."
setLineHeight = 18*resolution
setFontSize = 16*resolution
xPos, yPos = W/20,H/20 
txtW, txtH =  W-(W/10),H-(H/10)


lineHeight(setLineHeight)

# linking a specific font file for testing
font("../google-fonts-static/Encode_Sans/EncodeSans-Regular.ttf", setFontSize)
fill(1,0,1)
 
textBox(testString, (xPos, yPos, txtW, txtH))

# newly generated static font
font("./EncodeSans-Regular.ttf", setFontSize)


for axis, data in listFontVariations().items():
    print((axis, data))


blendMode("screen")
fill(0,1,0)

textBox(testString, (xPos, yPos, txtW, txtH))

rotate(90)
fontSize(12*resolution)
fill(0.6)
tracking(1)

text(f"old static vs new static TTF (no visible difference)", (H-(H/17), -(W/34)), align="right")

# saveImage(f"image-exports/encode-diff_test-{testFont}-wght_{varWght}-2018_10_09-14_28.png")
