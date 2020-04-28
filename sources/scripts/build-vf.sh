#!/bin/bash

### macOS build script for Encode Sans variable. See repo README for usage details.

# print each line as it executes. Add -e to stop on the first error, for debugging
set -e

#--------------------------------------------#
#----------------- set vars -----------------#

glyphsSource="sources/Encode-Sans.glyphs"
finalLocation="fonts/encodesans/full_vf"

## if the Glyphs source has a non-rectangular master/instance arrangement, this fixes it (WIP)
fixGlyphsDesignspace=true

#----------------- set vars -----------------#
#--------------------------------------------#

# if varfont folder exists, clean it up
if [[ -d "variable_ttf" ]]; then
  rm -rf variable_ttf
fi

# --------------------------------------------------------------
# Sets up names

## make temp glyphs filename with "-build" suffix
tempGlyphsSource=${glyphsSource/".glyphs"/"-Build.glyphs"}

# get font name from glyphs source
VFname=`python sources/scripts/helpers/get-font-name.py ${glyphsSource}`
# checking that the name has been pulled out of the source file
echo "VF Name: ${VFname}"

# --------------------------------------------------------------
# Fix non-rectangular designspace

## copy Glyphs file into temp file
cp $glyphsSource $tempGlyphsSource

if [ $fixGlyphsDesignspace == true ]
then
    ## call the designspace fixing script
    python sources/scripts/helpers/fix-designspace.py $tempGlyphsSource
else
    echo "Not morphing designspace."
fi

# --------------------------------------------------------------
# Generate Variable Font

## call fontmake to make a varfont
fontmake -o variable -g $tempGlyphsSource

if [ $keepDesignspace == true ]
then
    echo "designspace in master_ufo folder"
else
    rm -rf master_ufo
fi

## clean up temp glyphs file
# rm -rf $tempGlyphsSource

# --------------------------------------------------------------
# SmallCap subsetting

# smallCapFontName, e..g 'SignikaSC-VF'
smallCapFontName=${VFname/"-VF"/"SC-VF"}
ttfPath="variable_ttf/${VFname}.ttf"
echo $ttfPath

subsetSmallCaps()
{
    FILE=$1
    SC_FILE=$2

    # make file with smallcaps frozen in
    python sources/scripts/helpers/pyftfeatfreeze.py -f 'smcp' -S -U SC $FILE $SC_FILE

    # subset with pyftsubset to remove replaced lowercase, also remove unecessary ligatures
    python sources/scripts/helpers/subset-glyphs-replaced-by-smallcaps.py $SC_FILE -r "fi f_i f_j f_l fl dotlessi uni0237 o.comb f.short"

    # remove feature-frozen font & simplifying name of subset font

    # rm -rf $SC_FILE

    mv ${SC_FILE/"VF"/"VF.subset"} $SC_FILE
}

# subsetSmallCaps variable_ttf/${VFname}.ttf variable_ttf/${smallCapFontName}.ttf
subsetSmallCaps $ttfPath variable_ttf/${smallCapFontName}.ttf

# --------------------------------------------------------------
# OpenType table fixes

for file in variable_ttf/*; do 
if [ -f "$file" ]; then 
    # fileName=$(basename $file)

    echo "fix DSIG in " $file
    gftools fix-dsig --autofix $file

    ## sets up temp ttx file to insert correct values into tables # also drops MVAR table to fix vertical metrics issue
    ttx -x "MVAR" $file

    rm -rf $file

    ttxPath=${file/".ttf"/".ttx"}
    patchPath=${file/".ttf"/"-patch.ttx"}

    # ## inserts patch files into temporary ttx to fix export errors
    # ## BE SURE to update these patches for the real values in a given typeface
    if [[ $file != *"SC"* ]]; then
        cp $ttxPath $patchPath
        cat $patchPath | tr '\n' '\r' | sed -e "s~<name>.*<\/name>~$(cat sources/scripts/helpers/patches/NAMEpatch-wdth_wght.xml | tr '\n' '\r')~" | tr '\r' '\n' > $ttxPath
        rm -rf $patchPath
    fi
    if [[ $file == *"SC"* ]]; then
        cp $ttxPath $patchPath
        cat $patchPath | tr '\n' '\r' | sed -e "s~<name>.*<\/name>~$(cat sources/scripts/helpers/patches/NAMEpatch-wdth_wght_SC.xml | tr '\n' '\r')~" | tr '\r' '\n' > $ttxPath
        rm -rf $patchPath
    fi
    # same for either
    cp $ttxPath $patchPath
    cat $patchPath | tr '\n' '\r' | sed -e "s,<STAT>.*<\/STAT>,$(cat sources/scripts/helpers/patches/STATpatch-wdth_wght.xml | tr '\n' '\r')," | tr '\r' '\n' > $ttxPath
    rm -rf $patchPath

    ## copies temp ttx file back into a new ttf file
    ttx $ttxPath

    rm -rf $ttxPath

    ## Marc's solution to fix ppem bit 3
    gftools fix-hinting $file
    mv "$file.fix" $file

fi
done

# --------------------------------------------------------------
# Sort into final folder

cp $file $finalLocation/$fileName