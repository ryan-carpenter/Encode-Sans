############################################
################# set vars #################

glyphsSource="sources/Encode-Sans.glyphs"

## if the Glyphs source has a non-rectangular master/instance arrangement, this fixes it (WIP)
fixGlyphsDesignspace=true

################# set vars #################
############################################

# clear previous builds if they exist
if [ -d "instance_ttf" ]; then
  rm -rf instance_ttf
fi

# ============================================================================
# Sets up names ==============================================================

tempGlyphsSource=${glyphsSource/".glyphs"/"-build.glyphs"}

# ============================================================================
# Fix non-rectangular designspace ============================================

# copy Glyphs file into temp file
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

## this is a hack, to get around current bug in macOS text rendering (see docs/08-QA-beyond-fontbakery-and-glyphs)
## just decomposing the source, and leaving componentized version as a layer for each master
## oslashDecompGlyphsSource=${tempGlyphsSource/".glyphs"/"-oslash_decomp.glyphs"}
## python sources/scripts/helpers/decompose-oslash.py ${tempGlyphsSource}

fontmake -g ${tempGlyphsSource} --output ttf --interpolate --overlaps-backend booleanOperations
## OR to just make one static font, as a test, use:
## fontmake -g sources/split/Encode-Sans-fixed_designspace.glyphs -i "Encode Sans SemiExpanded .*" --output ttf --overlaps-backend booleanOperations
# fontmake -g sources/split/Encode-Sans-fixed_designspace.glyphs -i "Encode Sans SemiCondensed Bold" --output ttf --overlaps-backend booleanOperations

# clean up temp glyphs file
# rm -rf $tempGlyphsSource
# rm -rf $oslashDecompGlyphsSource

# # ============================================================================
# # SmallCap subsetting ========================================================

# get first TTF file in instance_ttf
counter=0
for file in instance_ttf/*; do
    if [[ -f "$file" && $file == *".ttf" && $counter == 0 ]]; then
        exampleTTF=$file
        counter=1
    fi
done

ttx $exampleTTF
ttxPath=${exampleTTF/".ttf"/".ttx"}

echo exampleTTF is $exampleTTF
echo ttxPath is $ttxPath

#get glyph names, minus .smcp glyphs
subsetGlyphNames=`python sources/scripts/helpers/get-smallcap-subset-glyphnames.py $ttxPath`
rm -rf $ttxPath

# echo $subsetGlyphNames

smallCapSuffix="SC"

for file in instance_ttf/*; do 
if [[ -f "$file" && $file == *".ttf" ]]; then 
    subsetSC=true
    case $file in
        *"EncodeSansCondensed-"*)
            smallCapFile=${file/"EncodeSansCondensed"/"EncodeSansCondensedSC"}
            familyName="Encode Sans Condensed"
        ;;
        *"EncodeSansSemiCondensed-"*)
            smallCapFile=${file/"EncodeSansSemiCondensed"/"EncodeSansSemiCondensedSC"}
            familyName="Encode Sans SemiCondensed"
        ;;
        *"EncodeSans-"*)
            smallCapFile=${file/"EncodeSans"/"EncodeSansSC"}
            familyName="Encode Sans"
        ;;
        *"EncodeSansSemiExpanded-"*)
            smallCapFile=${file/"EncodeSansSemiExpanded"/"EncodeSansSemiExpandedSC"}
            familyName="Encode Sans SemiExpanded"
        ;;
        *"EncodeSansExpanded-"*)
            smallCapFile=${file/"EncodeSansExpanded"/"EncodeSansExpandedSC"}
            familyName="Encode Sans Expanded"
        ;;
        *)
            subsetSC=false
    esac 

    if [ $subsetSC == true ]; then
        pyftfeatfreeze.py -f 'smcp' $file $smallCapFile

        echo "subsetting smallcap font"
        # subsetting with subsetGlyphNames list
        pyftsubset --name-IDs='*' $smallCapFile $subsetGlyphNames
        subsetSmallCapFile=${smallCapFile/".ttf"/".subset.ttf"}
        rm -rf $smallCapFile
        mv $subsetSmallCapFile $smallCapFile

        # update names in font with smallcaps suffix
        echo python sources/scripts/helpers/add-smallcaps-suffix.py $smallCapFile $smallCapSuffix "$familyName"
        python sources/scripts/helpers/add-smallcaps-suffix.py $smallCapFile $smallCapSuffix "$familyName"

        # just for testing results
        # ttx $smallCapFile
    fi
fi 
done

# ============================================================================
# Abbreviate names ===========================================================

for file in instance_ttf/*; do 
if [[ -f "$file" && $file == *".ttf" ]]; then
    python sources/scripts/helpers/shorten-nameID-4-6.py $file
fi
done


# ============================================================================
# Autohinting ================================================================

for file in instance_ttf/*; do 
if [[ -f "$file" && $file == *".ttf" ]]; then 
    echo "fix DSIG in " ${file}
    gftools fix-dsig --autofix ${file}

    echo "TTFautohint " ${file}
    # autohint with detailed info
    hintedFile=${file/".ttf"/"-hinted.ttf"}
    ttfautohint -I ${file} ${hintedFile} --stem-width-mode nnn
    cp ${hintedFile} ${file}
    rm -rf ${hintedFile}
fi 
done

# ============================================================================
# Remove MVAR table ==========================================================

for file in instance_ttf/*; do 
if [ -f "$file" ]; then 
    ttxPath=${file/".ttf"/".ttx"}
    ## sets up temp ttx file to insert correct values into tables # also drops MVAR table to fix vertical metrics issue
    ttx -x "MVAR" $file
    rm -rf $file
    ## copies temp ttx file back into a new ttf file
    ttx $ttxPath
    rm -rf $ttxPath
fi
done

# # ============================================================================
# # Sort into final folder and fontbake ========================================

fontbakeFile()
{
    FILEPATH=$1
    FBPATH=$2
    fontbakery check-googlefonts $FILEPATH --ghmarkdown $FBPATH
}

outputDir="fonts"

for file in instance_ttf/*; do 
if [[ -f "$file" && $file == *".ttf" ]]; then 
    fileName=$(basename $file)
    echo $fileName
    case $file in
        *"EncodeSansCondensed-"*)
            newPath=${outputDir}/encodesanscondensed/${fileName}
            fontbakePath=${outputDir}/encodesanscondensed/fontbakery-checks/${fileName/".ttf"/"-fontbakery_checks.md"}
        ;;
        *"EncodeSansCondensedSC-"*)
            newPath=${outputDir}/encodesanscondensed_sc/${fileName}
            fontbakePath=${outputDir}/encodesanscondensed_sc/fontbakery-checks/${fileName/".ttf"/"-fontbakery_checks.md"}
        ;;
        *"EncodeSansSemiCondensed-"*)
            newPath=${outputDir}/encodesanssemicondensed/${fileName}
            fontbakePath=${outputDir}/encodesanssemicondensed/fontbakery-checks/${fileName/".ttf"/"-fontbakery_checks.md"}
        ;;
        *"EncodeSansSemiCondensedSC-"*)
            newPath=${outputDir}/encodesanssemicondensed_sc/${fileName}
            fontbakePath=${outputDir}/encodesanssemicondensed_sc/fontbakery-checks/${fileName/".ttf"/"-fontbakery_checks.md"}
        ;;
        *"EncodeSans-"*)
            newPath=${outputDir}/encodesans/static/${fileName}
            fontbakePath=${outputDir}/encodesans/static/fontbakery-checks/${fileName/".ttf"/"-fontbakery_checks.md"}
        ;;
        *"EncodeSansSC-"*)
            newPath=${outputDir}/encodesans_sc/static/${fileName}
            fontbakePath=${outputDir}/encodesans_sc/static/fontbakery-checks/${fileName/".ttf"/"-fontbakery_checks.md"}
        ;;
        *"EncodeSansSemiExpanded-"*)
            newPath=${outputDir}/encodesanssemiexpanded/${fileName}
            fontbakePath=${outputDir}/encodesanssemiexpanded/fontbakery-checks/${fileName/".ttf"/"-fontbakery_checks.md"}
        ;;
        *"EncodeSansSemiExpandedSC-"*)
            newPath=${outputDir}/encodesanssemiexpanded_sc/${fileName}
            fontbakePath=${outputDir}/encodesanssemiexpanded_sc/fontbakery-checks/${fileName/".ttf"/"-fontbakery_checks.md"}
        ;;
        *"EncodeSansExpanded-"*)
            newPath=${outputDir}/encodesansexpanded/${fileName}
            fontbakePath=${outputDir}/encodesansexpanded/fontbakery-checks/${fileName/".ttf"/"-fontbakery_checks.md"}
        ;;
        *"EncodeSansExpandedSC-"*)
            newPath=${outputDir}/encodesansexpanded_sc/${fileName}
            fontbakePath=${outputDir}/encodesansexpanded_sc/fontbakery-checks/${fileName/".ttf"/"-fontbakery_checks.md"}
        ;;
    esac

    cp ${file} ${newPath}
        
    fontbakeFile $newPath $fontbakePath
fi 
done

# clean up build folders
rm -rf instance_ufo
# rm -rf instance_ttf
rm -rf master_ufo