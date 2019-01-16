### WIP macOS build script for Encode Sans VF, based on a build script by Mike LaGuttuta
### Run in the terminal by entering this file path (must be given execute permissions with chmod)
### requires a python 3 environment

# print each line as it executes, and stop on the first error
set -x -e 

while [ ! $# -eq 0 ]
    do
    case "$1" in
        --condensed | -c)
            glyphsSource="sources/split/Encode-Sans-condensed.glyphs"
            finalLocation="fonts/encodesanscondensed"
            scFinalLocation="fonts/encodesanscondensed_sc"
        ;;
        --semicondensed | -sc)
            glyphsSource="sources/split/Encode-Sans-semicondensed.glyphs"
            finalLocation="fonts/encodesanssemicondensed"
            scFinalLocation="fonts/encodesanssemicondensed_sc"
        ;;
        --normal | -n)
            glyphsSource="sources/split/Encode-Sans-normal.glyphs"
            finalLocation="fonts/encodesans"
            scFinalLocation="fonts/encodesans_sc"
        ;;
        --semiexpanded | -se)
            glyphsSource="sources/split/Encode-Sans-semiexpanded.glyphs"
            finalLocation="fonts/encodesanssemiexpanded"
            scFinalLocation="fonts/encodesanssemiexpanded_sc"
        ;;
        --expanded | -e)
            glyphsSource="sources/split/Encode-Sans-expanded.glyphs"
            finalLocation="fonts/encodesansexpanded"
            scFinalLocation="fonts/encodesansexpanded_sc"
        ;;
        *) 
            echo "Error: please supply an argument of --condensed (-c), --semicondensed (-sc), --normal (-c), --semiexpanded (-se), or --expanded (-e)"
    esac
    shift
done

# if varfont folder exists, clean it up
if [ -d "variable_ttf" ]; then
  rm -rf variable_ttf
fi

# ============================================================================
# Set up names ===============================================================

# get font name from glyphs source
VFname=`python sources/scripts/helpers/get-font-name.py ${glyphsSource}`
# checking that the name has been pulled out of the source file
echo "VF Name: ${VFname}"

# ============================================================================
# Generate Variable Font =====================================================

# ## call fontmake to make a varfont
fontmake -o variable -g $glyphsSource

# ============================================================================
# SmallCap subsetting ========================================================

# smallCapFontName, e..g 'SignikaSC-VF'
# smallCapFontName=${VFname/"-VF"/"SC-VF"}
# ttfPath="variable_ttf/${VFname}.ttf"

subsetSmallCaps()
{
    FILE=$1
    SC_NAME=$2

    echo making ${smallCapFontName}.ttf

    pyftfeatfreeze.py -f 'smcp' -S -U SC $FILE $SC_NAME

    ttx $FILE
    # ttxPath="variable_ttf/${VFname}.ttx"
    ttxPath=${FILE/".ttf"/".ttx"}

    #get glyph names, minus .smcp glyphs
    subsetGlyphNames=`python sources/scripts/helpers/get-smallcap-subset-glyphnames.py $ttxPath`

    # echo $subsetGlyphNames
    echo "subsetting smallcap font"

    # subsetting with subsetGlyphNames list
    pyftsubset $SC_NAME ${subsetGlyphNames} --glyph-names

    # remove feature-frozen font & simplifying name of subset font

    subsetSmallCapFontName=${SC_NAME/"VF"/"VF.subset"}

    rm -rf $SC_NAME

    mv ${subsetSmallCapFontName} $SC_NAME

    # removes temp ttx file
    rm -rf $ttxPath
}


for file in variable_ttf/*; do
    # subsetSmallCaps $ttfPath variable_ttf/${smallCapFontName}.ttf
    smallCapFontName=${file/"-VF"/"SC-VF"}
    subsetSmallCaps $file ${smallCapFontName}
done


# ============================================================================
# Autohinting ================================================================

for file in variable_ttf/*; do 
if [ -f "$file" ]; then 
    echo "TTFautohint " ${file}
    # autohint with detailed info
    hintedFile=${file/".ttf"/"-hinted.ttf"}
    
    # Hint with TTFautohint-VF ... currently janky – it would be better to properly add this dependency
    # https://groups.google.com/forum/#!searchin/googlefonts-discuss/ttfautohint%7Csort:date/googlefonts-discuss/WJX1lrzcwVs/SIzaEvntAgAJ
    # ./Users/stephennixon/Environments/gfonts3/bin/ttfautohint-vf ${ttfPath} ${ttfPath/"-unhinted.ttf"/"-hinted.ttf"}
    echo "------------------------------------------------"
    echo ttfautohint-vf $file $hintedFile  --increase-x-height 9 --stem-width-mode nnn
    echo "------------------------------------------------"
    ttfautohint-vf -I $file $hintedFile  --increase-x-height 9 --stem-width-mode nnn

    cp ${hintedFile} ${file}
    rm -rf ${hintedFile}
fi 
done

# ============================================================================
# OpenType table fixes =======================================================

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
    # if [[ $file != *"SC"* ]]; then
    #     cp $ttxPath $patchPath
    #     cat $patchPath | tr '\n' '\r' | sed -e "s~<name>.*<\/name>~$(cat sources/scripts/helpers/patches/NAMEpatch-normal_width_VF.xml | tr '\n' '\r')~" | tr '\r' '\n' > $ttxPath
    #     rm -rf $patchPath
    # fi
    # if [[ $file == *"SC"* ]]; then
    #     cp $ttxPath $patchPath
    #     cat $patchPath | tr '\n' '\r' | sed -e "s~<name>.*<\/name>~$(cat sources/scripts/helpers/patches/NAMEpatch-normal_width_VF_SC.xml | tr '\n' '\r')~" | tr '\r' '\n' > $ttxPath
    #     rm -rf $patchPath
    # fi
    # same for either
    cp $ttxPath $patchPath
    cat $patchPath | tr '\n' '\r' | sed -e "s,<STAT>.*<\/STAT>,$(cat sources/scripts/helpers/patches/STATpatch-normal_width_VF.xml | tr '\n' '\r')," | tr '\r' '\n' > $ttxPath
    rm -rf $patchPath

    ## copies temp ttx file back into a new ttf file
    ttx $ttxPath

    rm -rf $ttxPath
fi
done

# ============================================================================
# Sort into final folder =====================================================


for file in variable_ttf/*; do 
    if [ -f "$file" ]; then 
        open $file

        fileName=$(basename $file)

        if [[ $file != *"SC"* ]]; then
            cp $file $finalLocation/$fileName
            echo "new VF location is " $finalLocation/$fileName
            fontbakery check-googlefonts $finalLocation/$fileName --ghmarkdown $finalLocation/${fileName/".ttf"/"-fontbakery-report.md"}
        fi
        if [[ $file == *"SC"* ]]; then
            cp $file $scFinalLocation/$fileName
            echo "new VF location is " $scFinalLocation/$fileName
            fontbakery check-googlefonts $scFinalLocation/$fileName --ghmarkdown $scFinalLocation/${fileName/".ttf"/"-fontbakery-report.md"}
        fi
    fi
done

rm -rf variable_ttf
rm -rf instance_ufo
rm -rf master_ufo