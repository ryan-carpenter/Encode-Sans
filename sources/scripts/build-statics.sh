# TODO: optimize with a variable name rather than the exact path
# fontmake -m master_ufo/EncodeSans.designspace --output ttf --interpolate "Encode Sans Condensed ExtraLight" --autohint

############################################
################# set vars #################

glyphsSource="sources/Encode-Sans.glyphs"

## if the Glyphs source has a non-rectangular master/instance arrangement, this fixes it (WIP)
fixGlyphsDesignspace=true

################# set vars #################
############################################

pwd

echo $glyphsSource

tempGlyphsSource=${glyphsSource/".glyphs"/"-build.glyphs"}

## copy Glyphs file into temp file
cp $glyphsSource $tempGlyphsSource

if [ $fixGlyphsDesignspace == true ]
then
    ## call the designspace fixing script
    python sources/scripts/helpers/fix-designspace.py $tempGlyphsSource
else
    echo "Not morphing designspace."
fi

# this is a hack, to get around current bug in macOS text rendering (see docs/08-QA-beyond-fontbakery-and-glyphs)
oslashDecompGlyphsSource=${tempGlyphsSource/".glyphs"/"-oslash_decomp.glyphs"}
python sources/scripts/helpers/decompose-oslash.py ${tempGlyphsSource}

fontmake -g ${oslashDecompGlyphsSource} --output ttf --interpolate --overlaps-backend booleanOperations
## OR to just make one static font, as a test, use:
## fontmake -g sources/split/Encode-Sans-fixed_designspace.glyphs -i "Encode Sans Condensed Bold" --output ttf --overlaps-backend booleanOperations

## clean up temp glyphs file
rm -rf $tempGlyphsSource
rm -rf $oslashDecompGlyphsSource

python sources/scripts/helpers/shorten-nameID-4-6.py instance_ttf

for file in instance_ttf/*; do 
if [ -f "$file" ]; then 
    echo "fix DSIG in " ${file}
    gftools fix-dsig --autofix ${file}

    echo "TTFautohint " ${file}
    # autohint with detailed info
    hintedFile=${file/".ttf"/"-hinted.ttf"}
    ttfautohint -I ${file} ${hintedFile}
    cp ${hintedFile} ${file}
    rm -rf ${hintedFile}
fi 
done

fontbakeFile()
{
    FILEPATH=$1
    fontbakery check-googlefonts ${FILEPATH} --ghmarkdown ${FILEPATH/".ttf"/"-fontbakery-report.md"}
}

outputDir="fonts"

for file in instance_ttf/*; do 
if [ -f "$file" ]; then 
    fileName=$(basename $file)
    echo $fileName
    if [[ $file == *"EncodeSansCondensed-"* ]]; then
        newPath=${outputDir}/encodesanscondensed/static/${fileName}
        cp ${file} ${newPath}
        
        fontbakeFile ${newPath}
    fi
    if [[ $file == *"EncodeSansSemiCondensed-"* ]]; then
        newPath=${outputDir}/encodesanssemicondensed/static/${fileName}
        cp ${file} ${newPath}
        
        fontbakeFile ${newPath}
    fi
    if [[ $file == *"EncodeSans-"* ]]; then
        newPath=${outputDir}/encodesans/static/${fileName}
        cp ${file} ${newPath}
        
        fontbakeFile ${newPath}
    fi
    if [[ $file == *"EncodeSansSemiExpanded-"* ]]; then
        newPath=${outputDir}/encodesanssemiexpanded/static/${fileName}
        cp ${file} ${newPath}
        
        fontbakeFile ${newPath}
    fi
    if [[ $file == *"EncodeSansExpanded-"* ]]; then
        newPath=${outputDir}/encodesansexpanded/static/${fileName}
        cp ${file} ${newPath}
        
        fontbakeFile ${newPath}
    fi
fi 
done

# clean up build folders
rm -rf instance_ufo
rm -rf instance_ttf
rm -rf master_ufo