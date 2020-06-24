#!/bin/bash

### macOS build script for Encode Sans static fonts. See repo README for usage details.

# print each line as it executes. Add -e to stop on the first error, for debugging
set -e

#--------------------------------------------#
#----------------- set vars -----------------#

glyphsSource="sources/Encode-Sans.glyphs"

# --------------------------------------------------------------
# Clean out old builds

rm -rf fonts/EncodeSans/static
rm -rf fonts/EncodeSansSC/static

# --------------------------------------------------------------
# Generate Static Fonts

fontmake -g $glyphsSource --output ttf --interpolate --overlaps-backend booleanOperations
# fontmake -g $glyphsSource --output ttf -i ".* SemiCondensed ExtraBold.*" --overlaps-backend booleanOperations # to test just one style
# fontmake -g $glyphsSource --output ttf -i ".* Regular.*" --overlaps-backend booleanOperations # to test just regular styles


# --------------------------------------------------------------
# SmallCap subsetting

for file in instance_ttf/*; do 
if [[ -f "$file" && $file == *".ttf" ]]; then 

    smallCapTTFPath="${file/Sans-/SansSC-}"

    # make file with smallcaps frozen in
    python sources/scripts/build-helpers/pyftfeatfreeze.py -f 'smcp' $file $smallCapTTFPath

    # fix name suffixing because pyftfreeze doesn’t do it properly
    python sources/scripts/build-helpers/fix-name-SC_suffixing.py $smallCapTTFPath

    # subset with pyftsubset to remove replaced lowercase, also remove unecessary ligatures
    python sources/scripts/build-helpers/subset-glyphs-replaced-by-smallcaps.py $smallCapTTFPath -r "fi f_i f_j f_l fl dotlessi uni0237 o.comb f.short"

    # overwrite frozen font with frozen+subset font
    mv ${smallCapTTFPath/".ttf"/".subset.ttf"} $smallCapTTFPath

    # add unicode to dotlessi.sc (pyftfreeze is missing this one)
    python sources/scripts/build-helpers/add-unicode-to-dotlessi_sc.py $smallCapTTFPath

    # update OS/2 xAvgCharWidth for new glyph set
    python sources/scripts/build-helpers/set-x_avg_char_width.py $smallCapTTFPath

fi
done


# # --------------------------------------------------------------
# # Abbreviate names

for file in instance_ttf/*; do 
if [[ -f "$file" && $file == *".ttf" ]]; then
    python sources/scripts/build-helpers/fix-name-lengths.py $file
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
    if [[ $file == *"SansSC-"* ]]; then 
        mv $file fonts/EncodeSansSC/static/$(basename $file)
    else
        mv $file fonts/EncodeSans/static/$(basename $file)
    fi
done
