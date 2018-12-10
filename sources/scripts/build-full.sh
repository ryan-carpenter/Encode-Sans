### WIP macOS build script for Encode Sans VF, based on a build script by Mike LaGuttuta
### Run in the terminal by entering this file path (must be given execute permissions with chmod)
### requires a python 3 environment


############################################
################# set vars #################

glyphsSource="sources/Encode-Sans.glyphs"

## Set this. It's probably your font name without spaces, then "-VF"
# VFname="EncodeSans-VF"

## if the Glyphs source has a non-rectangular master/instance arrangement, this fixes it (WIP)
fixGlyphsDesignspace=true

## move VF into new folder of dist/ with timestamp and fontbake
timestampAndFontbakeInDist=true

## keep designspace file if you want to check values later
keepDesignspace=false

################# set vars #################
############################################

## make temp glyphs filename with "-build" suffix
tempGlyphsSource=${glyphsSource/".glyphs"/"-Build.glyphs"}

# get font name from glyphs source
VFname=`python sources/scripts/helpers/get-font-name.py ${glyphsSource}`
# checking that the name has been pulled out of the source file
echo "VF Name: ${VFname}"

## copy Glyphs file into temp file
cp $glyphsSource $tempGlyphsSource

if [ $fixGlyphsDesignspace == true ]
then
    ## call the designspace fixing script
    python sources/scripts/helpers/fix-designspace.py $tempGlyphsSource
else
    echo "Not morphing designspace."
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
echo "fix DSIG in " ${VFname}
gftools fix-dsig --autofix ${VFname}.ttf

## sets up temp ttx file to insert correct values into tables
ttx ${VFname}.ttf

rm -rf ${VFname}.ttf
rm -rf ${VFname}-backup-fonttools-prep-gasp.ttf

cd ..

ttxPath="variable_ttf/${VFname}.ttx"

patchPath="variable_ttf/${VFname}-patch.ttx"

# ## inserts patch files into temporary ttx to fix export errors
# ## BE SURE to update these patches for the real values in a given typeface
cp $ttxPath $patchPath
cat $patchPath | tr '\n' '\r' | sed -e "s~<name>.*<\/name>~$(cat sources/scripts/helpers/NAMEpatch.xml | tr '\n' '\r')~" | tr '\r' '\n' > $ttxPath
rm -rf $patchPath

cp $ttxPath $patchPath
cat $patchPath | tr '\n' '\r' | sed -e "s,<STAT>.*<\/STAT>,$(cat sources/scripts/helpers/STATpatch.xml | tr '\n' '\r')," | tr '\r' '\n' > $ttxPath
rm -rf $patchPath

## copies temp ttx file back into a new ttf file
ttx $ttxPath

# removes temp ttx file
rm -rf $ttxPath

ttfPath=${ttxPath/".ttx"/".ttf"}
hintedPath=${ttxPath/".ttx"/"-hinted.ttf"}

# Hint with TTFautohint-VF 
# currently janky – I need to find how to properly add this dependency
# https://groups.google.com/forum/#!searchin/googlefonts-discuss/ttfautohint%7Csort:date/googlefonts-discuss/WJX1lrzcwVs/SIzaEvntAgAJ
# ./Users/stephennixon/Environments/gfonts3/bin/ttfautohint-vf ${ttfPath} ${ttfPath/"-unhinted.ttf"/"-hinted.ttf"}
echo "================================================"
echo ttfautohint-vf $ttfPath $hintedPath
echo "================================================"
ttfautohint-vf -I $ttfPath $hintedPath

finalFilePath=${hintedPath/"-hinted"/""}
cp $hintedPath $finalFilePath

# open VF in default program; hopefully you have FontView
open ${finalFilePath}

# ## if you set timestampAndFontbakeInDist variable to true, this creates a new folder in 'dist' to put it into and run fontbake on
if [ $timestampAndFontbakeInDist == true ]
then
    ## move font into folder of dist/, with timestamp, then fontbake the font
    python3 sources/scripts/helpers/distdate-and-fontbake.py "fonts" "full_vf" $finalFilePath
    rm -rf variable_ttf
else
    ttx $finalFilename
    echo "font and ttx in variable_ttf folder"
fi
