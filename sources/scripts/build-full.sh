### WIP macOS build script for Encode Sans VF, based on a build script by Mike LaGuttuta
### Run in the terminal by entering this file path (must be given execute permissions with chmod)
### requires a python 3 environment


############################################
################# set vars #################

glyphsSource="sources/Encode-Sans.glyphs"
finalLocation="fonts/encodesans/full_vf"
scFinalLocation="fonts/encodesans_sc/full_vf"

## if the Glyphs source has a non-rectangular master/instance arrangement, this fixes it (WIP)
fixGlyphsDesignspace=true

## move VF into new folder of dist/ with timestamp and fontbake
timestampAndFontbakeInDist=false

## keep designspace file if you want to check values later
keepDesignspace=false

################# set vars #################
############################################

# if varfont folder exists, clean it up
if [ -d "variable_ttf" ]; then
  rm -rf variable_ttf
fi

# ============================================================================
# Sets up names ==============================================================

## make temp glyphs filename with "-build" suffix
tempGlyphsSource=${glyphsSource/".glyphs"/"-Build.glyphs"}

# get font name from glyphs source
VFname=`python sources/scripts/helpers/get-font-name.py ${glyphsSource}`
# checking that the name has been pulled out of the source file
echo "VF Name: ${VFname}"

# ============================================================================
# Fix non-rectangular designspace ============================================

## copy Glyphs file into temp file
cp $glyphsSource $tempGlyphsSource

if [ $fixGlyphsDesignspace == true ]
then
    ## call the designspace fixing script
    python sources/scripts/helpers/fix-designspace.py $tempGlyphsSource
else
    echo "Not morphing designspace."
fi

# ============================================================================
# Generate Variable Font =====================================================

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

# ============================================================================
# SmallCap subsetting ========================================================

# smallCapFontName, e..g 'SignikaSC-VF'
smallCapFontName=${VFname/"-VF"/"SC-VF"}
ttfPath="variable_ttf/${VFname}.ttf"
echo $ttfPath

open $ttfPath

subsetSmallCaps()
{
    FILE=$1
    SC_FILE=$2

    echo making ${smallCapFontName}.ttf

    pyftfeatfreeze.py -f 'smcp' -S -U SC $FILE $SC_FILE

    ttx $FILE
    # ttxPath="variable_ttf/${VFname}.ttx"
    ttxPath=${FILE/".ttf"/".ttx"}

    #get glyph names, minus smcp glyphs
    subsetGlyphNames=`python sources/scripts/helpers/get-smallcap-subset-glyphnames.py $ttxPath`

    # echo $subsetGlyphNames
    echo "subsetting smallcap font"

    echo "pyftsubset ${SC_FILE} ${subsetGlyphNames} --glyph-names"

    # subsetting with subsetGlyphNames list
    pyftsubset $SC_FILE $subsetGlyphNames --glyph-names

    # remove feature-frozen font & simplifying name of subset font

    subsetSmallCapFontName=${SC_FILE/"VF"/"VF.subset"}

    rm -rf $SC_FILE

    mv ${subsetSmallCapFontName} $SC_FILE

    # removes temp ttx file
    rm -rf $ttxPath
}

# subsetSmallCaps variable_ttf/${VFname}.ttf variable_ttf/${smallCapFontName}.ttf
subsetSmallCaps $ttfPath variable_ttf/${smallCapFontName}.ttf

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

fi
done

# ============================================================================
# Sort into final folder and fontbake ========================================

for file in variable_ttf/*; do 
    if [ -f "$file" ]; then 
        open $file

        if [ $timestampAndFontbakeInDist == true ]; then
            newFontLocation=`python sources/scripts/helpers/distdate.py ${file}`

            fontbakery check-googlefonts ${newFontLocation}/${VFname}.ttf --ghmarkdown ${newFontLocation}/${VFname}-fontbakery-report.md

            echo "new VF location is " ${newFontLocation}
        else
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
    fi
done

rm -rf variable_ttf
rm -rf instance_ufo
rm -rf master_ufo