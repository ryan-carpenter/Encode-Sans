#!/bin/bash

### macOS build script for Encode Sans static fonts. See repo README for usage details.

# print each line as it executes. Add -e to stop on the first error, for debugging
set -e

#--------------------------------------------#
#----------------- set vars -----------------#

glyphsSource="sources/Encode-Sans.glyphs"


# --------------------------------------------------------------
# Generate Static Fonts

fontmake -g $glyphsSource --output ttf --interpolate --overlaps-backend booleanOperations


# --------------------------------------------------------------
# SmallCap subsetting

for file in instance_ttf/*; do 
if [[ -f "$file" && $file == *".ttf" ]]; then 

    smallCapTTFPath="${file/.ttf/SC.ttf}"

    # make file with smallcaps frozen in
    python sources/scripts/helpers/pyftfeatfreeze.py -f 'smcp' -S -U SC $file $smallCapTTFPath

    # subset with pyftsubset to remove replaced lowercase, also remove unecessary ligatures
    python sources/scripts/helpers/subset-glyphs-replaced-by-smallcaps.py $smallCapTTFPath -r "fi f_i f_j f_l fl dotlessi uni0237 o.comb f.short"

    # overwrite frozen font with frozen+subset font
    mv ${smallCapTTFPath/"SC.ttf"/"SC.subset.ttf"} $smallCapTTFPath
fi 
done


# --------------------------------------------------------------
# Abbreviate names

for file in instance_ttf/*; do 
if [[ -f "$file" && $file == *".ttf" ]]; then
    python sources/scripts/helpers/shorten-nameID-4-6.py $file
fi
done


# --------------------------------------------------------------
# Autohinting

for file in instance_ttf/*; do 
if [[ -f "$file" && $file == *".ttf" ]]; then 
    echo "TTFautohint " ${file}
    # autohint with detailed info
    hintedFile=${file/".ttf"/"-hinted.ttf"}
    ttfautohint -I ${file} ${hintedFile} --stem-width-mode nnn
    cp ${hintedFile} ${file}
    rm -rf ${hintedFile}
fi 
done


# --------------------------------------------------------------
# OpenType table fixes

echo "Post processing statics"
ttfs=$(ls instance_ttf/*.ttf)
for ttf in $ttfs
do
	gftools fix-dsig -f $ttf

	gftools fix-hinting $ttf
	[ -f $ttf.fix ] && mv  $ttf.fix $ttf # correct filename if ".fix" version exists
done


# --------------------------------------------------------------
# Sort into final folder

mkdir -p fonts/EncodeSans/static
mkdir -p fonts/EncodeSansSC/static

for file in instance_ttf/*; do 
    if [[ $file == *"SC.ttf" ]]; then 
        mv $file fonts/EncodeSansSC/static/$(basename $file)
    else
        mv $file fonts/EncodeSans/static/$(basename $file)
    fi
done
