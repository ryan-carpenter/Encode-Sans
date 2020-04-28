#!/bin/bash

### macOS build script for Encode Sans variable. See repo README for usage details.

# print each line as it executes. Add -e to stop on the first error, for debugging
set -e

#--------------------------------------------#
#----------------- set vars -----------------#

glyphsSource="sources/Encode-Sans.glyphs"
finalLocation="fonts"
VFname="EncodeSans-VF.ttf"


# --------------------------------------------------------------
# Generate Variable Font

fontmake -o variable -g $glyphsSource --output-path $finalLocation/$VFname

# --------------------------------------------------------------
# SmallCap subsetting

TTFPath="variable_ttf/${VFname}"
smallCapTTFPath="variable_ttf/${VFname/-VF/SC-VF}"

echo $TTFPath
echo $smallCapTTFPath

# make file with smallcaps frozen in
python sources/scripts/helpers/pyftfeatfreeze.py -f 'smcp' -S -U SC $TTFPath $smallCapTTFPath

# subset with pyftsubset to remove replaced lowercase, also remove unecessary ligatures
python sources/scripts/helpers/subset-glyphs-replaced-by-smallcaps.py $smallCapTTFPath -r "fi f_i f_j f_l fl dotlessi uni0237 o.comb f.short"

# overwrite frozen font with frozen+subset font
mv ${smallCapTTFPath/"VF"/"VF.subset"} $smallCapTTFPath


# # --------------------------------------------------------------
# # OpenType table fixes

vfs=$(ls variable_ttf/*.ttf)
for vf in $vfs; do
    # # TODO: STAT fixes
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

# TODO: sort into encodesans vs encodesanssc
vfs=$(ls variable_ttf/*.ttf)
for vf in $vfs; do
    cp $vf $finalLocation/$(basename $vf)
done