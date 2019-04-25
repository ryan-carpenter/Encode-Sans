# run from the top directory of the Encode Sans project

set -e

testDir="docs/16-autohint-settings-test"

# fontmake -o "variable" -g "sources/split/Encode-Sans-normal.glyphs" --output-dir $testDir

fontBefore="$testDir/EncodeSans-Regular-from_GF_april_22_2019.ttf"
fontFile="EncodeSans-VF.ttf"
vf=$testDir/$fontFile



hintedDir=$testDir/hintedFonts
mkdir -p $hintedDir
# default autohint

hintedFile=$hintedDir/${fontFile/"VF"/"VF-autohint-defaults"}
echo $hintedFile
ttfautohint-vf -I $vf $hintedFile

for i in {8..16}
do
    # --stem-width-mode qsq is apparently the default

    hintedFile=$hintedDir/${fontFile/"VF"/"VF-autohint-xht_$i-stem_qsq"}
    echo $hintedFile
    ttfautohint-vf -I $vf $hintedFile  --increase-x-height $i --stem-width-mode qsq

    # --stem-width-mode nnn was recommended by Marc in the Signika VF upgrade

    hintedFile=$hintedDir/${fontFile/"VF"/"VF-autohint-xht_$i-stem_nnn"}
    echo $hintedFile
    ttfautohint-vf -I $vf $hintedFile  --increase-x-height $i --stem-width-mode nnn
done

# --increase-x-height 0 turns off this option

hintedFile=$hintedDir/${fontFile/"VF"/"VF-autohint-xht_0-stem_qsq"}
echo $hintedFile
ttfautohint-vf -I $vf $hintedFile  --increase-x-height 0 --stem-width-mode qsq

# trying stem width mode without changing --increase-x-height

hintedFile=$hintedDir/${fontFile/"VF"/"VF-autohint-stem_nnn"}
echo $hintedFile
ttfautohint-vf -I $vf $hintedFile --stem-width-mode nnn

# TODO?: use old file as a blue zones "reference" file