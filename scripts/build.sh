### WIP macOS build script for Encode Sans VF, based on a build script by Mike LaGuttuta
### Run in the terminal by entering this file path
### requires a python 2 environment, for now

############################################
################# set vars #################

glyphsSource="sources/Encode-Sans.glyphs"

## Set this. It's probably your font name without spaces, then "-VF"
VFname="EncodeSans-VF"

## if the Glyphs source has a non-rectangular master/instance arrangement, this fixes it (WIP)
fixGlyphsDesignspace=true

## move VF into new folder of dist/ with timestamp and fontbake
timestampAndFontbakeInDist=true

## keep designspace file if you want to check values later
keepDesignspace=true

################# set vars #################
############################################

## make temp glyphs filename with "-build" suffix
tempGlyphsSource=${glyphsSource/".glyphs"/"-Build.glyphs"}

## TODO: grab name from Glyphs source via python & glyphsLib?

## copy Glyphs file into temp file
cp $glyphsSource $tempGlyphsSource

if [ $fixGlyphsDesignspace == true ]
then
    ## call the designspace fixing script
    python2 scripts/fix-designspace.py $tempGlyphsSource
else
    echo "not morphing designspace"
fi

## call fontmake to make a varfont
fontmake -o variable -g $tempGlyphsSource

if [ $keepDesignspace == true ]
then
    echo "designspace in master_ufo folder"
else
    rm -rf master_ufo
fi

## clean up temp glyphs file
rm -rf $tempGlyphsSource

cd variable_ttf

## fix file metadata with gftools
gftools fix-nonhinting ${VFname}.ttf ${VFname}.ttf
gftools fix-dsig --autofix ${VFname}.ttf
gftools fix-gasp ${VFname}.ttf

## sets up temp ttx file to insert correct values into tables
ttx ${VFname}.ttf

rm -rf ${VFname}.ttf
rm -rf ${VFname}-backup-fonttools-prep-gasp.ttf

cd ..

ttxPath="variable_ttf/${VFname}.ttx"


## inserts patch files into temporary ttx to fix export errors
## BE SURE to update these patches for the real values in a given typeface
cat $ttxPath | tr '\n' '\r' | sed -e "s~<name>.*<\/name>~$(cat scripts/NAMEpatch.xml | tr '\n' '\r')~" | tr '\r' '\n' > variable_ttf/${VFname}-name.ttx
cat variable_ttf/${VFname}-name.ttx | tr '\n' '\r' | sed -e "s,<STAT>.*<\/STAT>,$(cat scripts/STATpatch.xml | tr '\n' '\r')," | tr '\r' '\n' > $ttxPath

rm -rf variable_ttf/${VFname}-name.ttx

## copies temp ttx file back into a new ttf file
ttx $ttxPath

# removes temp ttx file
rm -rf $ttxPath

ttfPath=${ttxPath/".ttx"/".ttf"}

# open VF in default program; hopefully you have FontView
open ${ttfPath}

## if you set timestampAndFontbakeInDist variable to true, this creates a new folder in 'dist' to put it into and run fontbake on
if [ $timestampAndFontbakeInDist == true ]
then
    ## move font into folder of dist/, with timestamp, then fontbake the font
    python3 scripts/distdate-and-fontbake.py $ttfPath
    rm -rf variable_ttf
else
    ttx $ttfPath
    echo "font and ttx in variable_ttf folder"
fi
