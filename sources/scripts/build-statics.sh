# ############################################
# ################# set vars #################

# glyphsSource="sources/Encode-Sans.glyphs"

# ## if the Glyphs source has a non-rectangular master/instance arrangement, this fixes it (WIP)
# fixGlyphsDesignspace=true

# ################# set vars #################
# ############################################

# # ============================================================================
# # Sets up names ==============================================================

# tempGlyphsSource=${glyphsSource/".glyphs"/"-build.glyphs"}

# # ============================================================================
# # Fix non-rectangular designspace ============================================

# # copy Glyphs file into temp file
# cp $glyphsSource $tempGlyphsSource

# if [ $fixGlyphsDesignspace == true ]
# then
#     ## call the designspace fixing script
#     python sources/scripts/helpers/fix-designspace.py $tempGlyphsSource
# else
#     echo "Not morphing designspace."
# fi

# # ============================================================================
# # Generate Variable Font =====================================================

# ## this is a hack, to get around current bug in macOS text rendering (see docs/08-QA-beyond-fontbakery-and-glyphs)
# ## just decomposing the source, and leaving componentized version as a layer for each master
# ## oslashDecompGlyphsSource=${tempGlyphsSource/".glyphs"/"-oslash_decomp.glyphs"}
# ## python sources/scripts/helpers/decompose-oslash.py ${tempGlyphsSource}

# fontmake -g ${tempGlyphsSource} --output ttf --interpolate --overlaps-backend booleanOperations
# ## OR to just make one static font, as a test, use:
# fontmake -g sources/split/Encode-Sans-fixed_designspace.glyphs -i "Encode Sans SemiExpanded Bold" --output ttf --overlaps-backend booleanOperations

# # clean up temp glyphs file
# rm -rf $tempGlyphsSource
# rm -rf $oslashDecompGlyphsSource

# # ============================================================================
# # SmallCap subsetting ========================================================

# get first TTF file in instance_ttf
counter=0
for file in instance_ttf/*; do
    if [[ -f "$file" && $file == *".ttf" && $counter == 0 ]]; then
        echo "hello it's a file"
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
if [ -f "$file" ]; then 
    subsetSC=true
    case $file in
        *"EncodeSansCondensed-"*)
            smallCapFile=${file/"EncodeSansCondensed"/"EncodeSansCondensedSC"}
            familyName="Encode Sans SemiExpanded"
            # subsetSC=true
        ;;
        *"EncodeSansSemiCondensed-"*)
            smallCapFile=${file/"EncodeSansSemiCondensed"/"EncodeSansSemiCondensedSC"}
            familyName="Encode Sans SemiCondensed"
            # subsetSC=true
        ;;
        *"EncodeSans-"*)
            smallCapFile=${file/"EncodeSans"/"EncodeSansSC"}
            familyName="Encode Sans"
            # subsetSC=true
        ;;
        *"EncodeSansSemiExpanded-"*)
            smallCapFile=${file/"EncodeSansSemiExpanded"/"EncodeSansSemiExpandedSC"}
            familyName="Encode Sans SemiExpanded"
            # subsetSC=true
        ;;
        *"EncodeSansExpanded-"*)
            smallCapFile=${file/"EncodeSansExpanded"/"EncodeSansExpandedSC"}
            familyName="Encode Sans Expanded"
            # subsetSC=true
        ;;
        *)
            subsetSC=false
    esac 

    if [ $subsetSC == true ]; then
        pyftfeatfreeze.py -f 'smcp' $file $smallCapFile

        echo "subsetting smallcap font"
        # subsetting with subsetGlyphNames list
        pyftsubset $smallCapFile $subsetGlyphNames

        # update names in font with smallcaps suffix
        echo 'python sources/scripts/helpers/add-smallcaps-suffix.py "$smallCapFile" "$smallCapSuffix" "$familyName"'
        python sources/scripts/helpers/add-smallcaps-suffix.py "$smallCapFile" "$smallCapSuffix" "$familyName"

        subsetSmallCapFile=${smallCapFile/".ttf"/".subset.ttf"}
        rm -rf $smallCapFile
        mv $subsetSmallCapFile $smallCapFile
    fi


    # 🚨 TODO: update SC font family name with TTX patch or python script
fi 
done

# ============================================================================
# Autohinting ================================================================

# python sources/scripts/helpers/shorten-nameID-4-6.py instance_ttf

# for file in instance_ttf/*; do 
# if [ -f "$file" ]; then 
#     echo "fix DSIG in " ${file}
#     gftools fix-dsig --autofix ${file}

#     echo "TTFautohint " ${file}
#     # autohint with detailed info
#     hintedFile=${file/".ttf"/"-hinted.ttf"}
#     ttfautohint -I ${file} ${hintedFile}
#     cp ${hintedFile} ${file}
#     rm -rf ${hintedFile}
# fi 
# done

# # ============================================================================
# # Sort into final folder and fontbake ========================================

# fontbakeFile()
# {
#     FILEPATH=$1
#     fontbakery check-googlefonts ${FILEPATH} --ghmarkdown ${FILEPATH/".ttf"/"-fontbakery-report.md"}
# }

# outputDir="fonts"

# for file in instance_ttf/*; do 
# if [ -f "$file" ]; then 
#     fileName=$(basename $file)
#     echo $fileName
#     if [[ $file == *"EncodeSansCondensed-"* ]]; then
#         newPath=${outputDir}/encodesanscondensed/${fileName}
#     fi
#     if [[ $file == *"EncodeSansCondensedSC-"* ]]; then
#         newPath=${outputDir}/encodesanscondensed_sc/${fileName}
#     fi
#     if [[ $file == *"EncodeSansSemiCondensed-"* ]]; then
#         newPath=${outputDir}/encodesanssemicondensed/${fileName}
#     fi
#     if [[ $file == *"EncodeSansSemiCondensedSC-"* ]]; then
#         newPath=${outputDir}/encodesanssemicondensed_sc/${fileName}
#     fi
#     if [[ $file == *"EncodeSans-"* ]]; then
#         newPath=${outputDir}/encodesans/static/${fileName}
#     fi
#     if [[ $file == *"EncodeSansSC-"* ]]; then
#         newPath=${outputDir}/encodesans_sc/static/${fileName}
#     fi
#     if [[ $file == *"EncodeSansSemiExpanded-"* ]]; then
#         newPath=${outputDir}/encodesanssemiexpanded/${fileName}
#     fi
#     if [[ $file == *"EncodeSansSemiExpandedSC-"* ]]; then
#         newPath=${outputDir}/encodesanssemiexpanded_sc/${fileName}
#     fi
#     if [[ $file == *"EncodeSansExpanded-"* ]]; then
#         newPath=${outputDir}/encodesansexpanded/${fileName}
#     fi
#     if [[ $file == *"EncodeSansExpandedSC-"* ]]; then
#         newPath=${outputDir}/encodesansexpanded_sc/${fileName}
#     fi
#     cp ${file} ${newPath}
        
#     fontbakeFile ${newPath}
# fi 
# done

# # clean up build folders
# rm -rf instance_ufo
# # rm -rf instance_ttf
# rm -rf master_ufo