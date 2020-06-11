#!/bin/bash

### macOS build script for Encode Sans variable. See repo README for usage details.

# print each line as it executes. Add -e to stop on the first error, for debugging
set -e

#--------------------------------------------#
#----------------- set vars -----------------#

glyphsSource="sources/Encode-Sans.glyphs"
VFname="EncodeSans-VF.ttf"

# auto-derived vars

TTFPath="fonts/${VFname}"
smallCapTTFPath="fonts/${VFname/-VF/SC-VF}"


# --------------------------------------------------------------
# Generate Variable Font

fontmake -o variable -g $glyphsSource --output-path fonts/$VFname

# --------------------------------------------------------------
# SmallCap subsetting

# make file with smallcaps frozen in
python sources/scripts/helpers/pyftfeatfreeze.py -f 'smcp' -S -U SC $TTFPath $smallCapTTFPath

# subset with pyftsubset to remove replaced lowercase, also remove unecessary ligatures
python sources/scripts/helpers/subset-glyphs-replaced-by-smallcaps.py $smallCapTTFPath -k "less" -r "fi f_i f_j f_l fl dotlessi uni0237 o.comb f.short"

# overwrite frozen font with frozen+subset font
mv ${smallCapTTFPath/"VF"/"VF.subset"} $smallCapTTFPath

# add unicode to dotlessi.sc (pyftfreeze is missing this one)
python sources/scripts/helpers/add-unicode-to-dotlessi_sc.py $smallCapTTFPath

# update OS/2 xAvgCharWidth for new glyph set
python sources/scripts/helpers/set-x_avg_char_width.py $smallCapTTFPath


# --------------------------------------------------------------
# OpenType table fixes

vfs=$(ls fonts/*.ttf)
for vf in $vfs; do

    # add STAT table to font
    python sources/scripts/helpers/add-stat-table.py $vf

    # other table fixes
    gftools fix-dsig -f $vf
    gftools fix-gasp --autofix $vf
    mv ${vf/".ttf"/".ttf.fix"} $vf
    gftools fix-nonhinting $vf $vf.fix
    mv $vf.fix $vf
    rm ${vf/".ttf"/"-backup-fonttools-prep-gasp.ttf"}

    ttx -x MVAR $vf                 # drop mvar table using fonttools/ttx
    ttx ${vf/'.ttf'/'.ttx'}         # convert back to TTF
    rm ${vf/'.ttf'/'.ttx'}          # erase temp TTX 
    mv ${vf/'.ttf'/'#1.ttf'} $vf    # overwrite original TTF with edited copy
done

# --------------------------------------------------------------
# Sort into final folder

mkdir -p fonts/EncodeSans
mkdir -p fonts/EncodeSansSC

mv $TTFPath         "fonts/EncodeSans/EncodeSans[wdth,wght].ttf"
mv $smallCapTTFPath "fonts/EncodeSansSC/EncodeSansSC[wdth,wght].ttf"