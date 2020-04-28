#!/bin/bash

### macOS build script for Encode Sans variable. See repo README for usage details.

# print each line as it executes. Add -e to stop on the first error, for debugging
set -e

#--------------------------------------------#
#----------------- set vars -----------------#

glyphsSource="sources/Encode-Sans.glyphs"
finalLocation="fonts/encodesans"

## if the Glyphs source has a non-rectangular master/instance arrangement, this fixes it (WIP)
fixGlyphsDesignspace=true

#----------------- set vars -----------------#
#--------------------------------------------#

# --------------------------------------------------------------
# Sets up names

# get font name from glyphs source
VFname=`python sources/scripts/helpers/get-font-name.py ${glyphsSource}`
# checking that the name has been pulled out of the source file
echo "VF Name: ${VFname}"


# --------------------------------------------------------------
# Generate Variable Font

## call fontmake to make a varfont
fontmake -o variable -g $glyphsSource

# --------------------------------------------------------------
# SmallCap subsetting

TTFPath="variable_ttf/${VFname}.ttf"
smallCapTTFPath="variable_ttf/${VFname/-VF/SC-VF}.ttf"

# make file with smallcaps frozen in
python sources/scripts/helpers/pyftfeatfreeze.py -f 'smcp' -S -U SC $TTFPath $smallCapTTFPath

# subset with pyftsubset to remove replaced lowercase, also remove unecessary ligatures
python sources/scripts/helpers/subset-glyphs-replaced-by-smallcaps.py $smallCapTTFPath -r "fi f_i f_j f_l fl dotlessi uni0237 o.comb f.short"

# remove feature-frozen font & simplifying name of subset font
mv ${smallCapTTFPath/"VF"/"VF.subset"} $smallCapTTFPath


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
