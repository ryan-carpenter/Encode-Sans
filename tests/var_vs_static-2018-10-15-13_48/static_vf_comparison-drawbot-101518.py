__doc__= """
    This is a simple tester to overlap two fonts in order 
    to check whether they share the same outlines and metrics.
    
    It is meant to be used in DrawBot (http://www.drawbot.com),
    and to pull fonts from its same or parent folder, 
    in order to keep font versions in sync with testing. 
    
    Edit the variables to test different things: 
        - `testString` for your test string
        - `currentTest` to choose from test conditions 
        - `tests` dictionary of test conditions – add some!
        - `setFontSize` to change the font size
    
    Sometimes, DrawBot gives unexpected results (e.g. it shows a 
    Condensed font when a normal-width font has been called). If 
    this happens, quit and reopen DrawBot. This may be due to 
    font metadata issues, and I will know more once I work through
    open issues reported by fontbakery QA.
    
"""

resolution = 2
W,H = 860*resolution, 340*resolution

newPage(W,H)

rect(0,0,W,H)

testString = "In statistical modeling, regression analysis is a set of statistical processes for estimating the relationships among variables. It includes many techniques for modeling and analyzing several variables, when the focus is on the relationship between a dependent variable and one or more independent variables (or 'predictors'). More specifically, regression analysis helps one understand how the typical value of the dependent variable (or 'criterion variable') changes when any one of the independent variables is varied, while the other independent variables are held fixed. \n \nMost commonly, regression analysis estimates the conditional expectation of the dependent variable given the independent variables – that is, the average value of the dependent variable when the independent variables are fixed. Less commonly, the focus is on a quantile, or other location parameter of the conditional distribution of the dependent variable given the independent variables. In all cases, a function of the independent variables called the regression function is to be estimated. In regression analysis, it is also of interest to characterize the variation of the dependent variable around the prediction of the regression function using a probability distribution. A related but distinct approach is Necessary Condition Analysis[1] (NCA), which estimates the maximum (rather than average) value of the dependent variable for a given value of the independent variable (ceiling line rather than central line) in order to identify what value of the independent variable is necessary but not sufficient for a given value of the dependent variable."

# testString = """nnniiinnniiinnn
# nininini
# llllllllll
# iiiiiiiiii
# lilililili
# oooooooooo
# oioioioioi
# pppppppppp
# gggggggggg
# tytytytyty
# dididididi
# """

########### Set Test ###########

currentTest = "test1"

################################

tests = {
    "test1": {
        "testName": "fontmake_VF_vs_gfonts_static",
        "font1": "./EncodeSans-VF.ttf", # magenta
        "font2": "../google-fonts-static/Encode_Sans/EncodeSans-Regular.ttf" # green
        },
    "test2": {
        "testName": "fontmake_VF_glyphs_VF",
        "font1": "./EncodeSans-VF.ttf", # magenta
        "font2": "./glyphs-generated/EncodeSansGX.ttf" # green
        },
    }
    
setFontSize = 16*resolution
setLineHeight = (setFontSize*1.125)
xPos, yPos = W/20,H/20 
txtW, txtH =  W-(W/10),H-(H/10)

lineHeight(setLineHeight)

blendMode("screen") # makes overlapping areas show in white

################################
#### First layer font       ####
################################

font(tests[currentTest]['font1'], setFontSize)

# if the font above is variable, this will print axes and values
# if len(listFontVariations().items()) >= 1:
for axis, data in listFontVariations().items():
    print((axis, data))
    
# when I set the fontVariations, the following text() method fails with NSInvalidArgumentException
fontVariations(wght=400,wdth=100.0)

fill(1,0,1) # magenta
 
textBox(testString, (xPos, yPos, txtW, txtH))
# textBox(tests[currentTest]['font1'], (xPos, 30, txtW, 40))

################################
#### Second layer font      ####
################################

font(tests[currentTest]['font2'], setFontSize)

# if the font above is variable, this will print axes and values
# if len(listFontVariations().items()) >= 1:
for axis, data in listFontVariations().items():
    print((axis, data))
    
# because I'm not sure if it's possible to do AVAR from Glyphs App yet
if currentTest == "test4" or currentTest == "test5":
    fontVariations(wght=85.0,wdth=500.0)

fill(0,1,0) # lime green

textBox(testString, (xPos, yPos, txtW, txtH))
# textBox(tests[currentTest]['font2'], (xPos+400, 30, txtW, 40))

################################
#### Test title             ####
################################

rotate(90)
fontSize(12*resolution)
fill(0.8)
tracking(1)

text(tests[currentTest]['testName'].replace("_", " "), (H-(H/17), -(W/32)), align="right")

################################
#### Save image             ####
################################

# saveImage(f"image-exports/encode-diff_test-{font(tests[currentTest]['testName'])}-2018_10_10.png")
