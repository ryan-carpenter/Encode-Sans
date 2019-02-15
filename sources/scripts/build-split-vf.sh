### WIP macOS build script for Encode Sans VF, based on a build script by Mike LaGuttuta
### Run in the terminal by entering this file path (must be given execute permissions with chmod)
### requires a python 3 environment

# print each line as it executes. Add -e to stop on the first error, for debugging
set -x

while [ ! $# -eq 0 ]
    do
    case "$1" in
        --condensed | -c)
            glyphsSource="sources/split/Encode-Sans-condensed.glyphs"
            finalLocation="fonts/encodesanscondensed"
            scFinalLocation="fonts/encodesanscondensedsc"
        ;;
        --semicondensed | -sc)
            glyphsSource="sources/split/Encode-Sans-semicondensed.glyphs"
            finalLocation="fonts/encodesanssemicondensed"
            scFinalLocation="fonts/encodesanssemicondensedsc"
        ;;
        --normal | -n)
            glyphsSource="sources/split/Encode-Sans-normal.glyphs"
            finalLocation="fonts/encodesans"
            scFinalLocation="fonts/encodesanssc"
        ;;
        --semiexpanded | -se)
            glyphsSource="sources/split/Encode-Sans-semiexpanded.glyphs"
            finalLocation="fonts/encodesanssemiexpanded"
            scFinalLocation="fonts/encodesanssemiexpandedsc"
        ;;
        --expanded | -e)
            glyphsSource="sources/split/Encode-Sans-expanded.glyphs"
            finalLocation="fonts/encodesansexpanded"
            scFinalLocation="fonts/encodesansexpandedsc"
        ;;
        #####
        # To build all split VFs, run: sources/scripts/build.sh --split
        #####
    esac
    shift
done

# if varfont folder exists, clean it up
if [ -d "variable_ttf" ]; then
  rm -rf variable_ttf
fi

# ============================================================================
# Generate Variable Font =====================================================

# ## call fontmake to make a varfont
fontmake -o variable -g $glyphsSource

# ============================================================================
# SmallCap subsetting ========================================================

subsetSmallCaps()
{
    FILE=$1
    SC_NAME=$2

    echo making ${smallCapFontName}.ttf

    python ./sources/scripts/helpers/pyftfeatfreeze.py -f 'smcp' -S -U SC $FILE $SC_NAME

    ttx $FILE
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
    smallCapFontName=${file/"-VF"/"SC-VF"}
    subsetSmallCaps $file ${smallCapFontName}
done




# ============================================================================
# Autohinting ================================================================

for file in variable_ttf/*; do 
if [ -f "$file" ]; then 
    hintedFile=${file/".ttf"/"-hinted.ttf"}
    ttfautohint-vf -I $file $hintedFile  --increase-x-height 9 --stem-width-mode nnn

    cp ${hintedFile} ${file}
    rm -rf ${hintedFile}
fi 
done

# ============================================================================
# OpenType table fixes =======================================================

for file in variable_ttf/*; do 
if [ -f "$file" ]; then 
    echo "fix DSIG in " $file
    gftools fix-dsig --autofix $file

    ## sets up temp ttx file to insert correct values into tables # also drops MVAR table to fix vertical metrics issue
    ttx -x "MVAR" $file 
    rm -rf $file

    ## copies temp ttx file back into a new ttf file
    ttxPath=${file/".ttf"/".ttx"}
    ttx $ttxPath
    rm -rf $ttxPath

    ## Marc's solution to fix VF metadata
    gftools fix-vf-meta $file
    mv "$file.fix" $file
fi
done

# ============================================================================
# Abbreviate names ===========================================================

for file in variable_ttf/*; do 
if [[ -f "$file" && $file == *".ttf" ]]; then
    python sources/scripts/helpers/shorten-nameID-4-6.py $file
fi
done

# ============================================================================
# Sort into final folder =====================================================

for file in variable_ttf/*; do 
    if [ -f "$file" ]; then 
        fileName=$(basename $file)
        fileName=${fileName/"VF"/"Thin"}

        if [[ $file != *"SC"* ]]; then
            finalPath=$finalLocation/split_vf/$fileName
            cp $file $finalPath
            echo "new VF location is " $finalPath
            fontbakery check-googlefonts $finalPath --ghmarkdown $finalLocation/split_vf/${fileName/".ttf"/"-fontbakery-report.md"}
            open $finalPath
        fi
        if [[ $file == *"SC"* ]]; then
            finalPath=$scFinalLocation/split_vf/$fileName
            cp $file $finalPath
            echo "new VF location is " $finalPath
            fontbakery check-googlefonts $finalPath --ghmarkdown $scFinalLocation/split_vf/${fileName/".ttf"/"-fontbakery-report.md"}
            open $finalPath
        fi
    fi
done

rm -rf variable_ttf #comment out to debug
rm -rf instance_ufo
rm -rf master_ufo
