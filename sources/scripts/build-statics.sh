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

tempGlyphsSource=${glyphsSource/".glyphs"/"-Build.glyphs"}

## copy Glyphs file into temp file
cp $glyphsSource $tempGlyphsSource

if [ $fixGlyphsDesignspace == true ]
then
    ## call the designspace fixing script
    python sources/scripts/helpers/fix-designspace.py $tempGlyphsSource
else
    echo "Not morphing designspace."
fi

# fontmake -g ${tempGlyphsSource} --output otf --interpolate --autohint # OTF not used on Google Fonts
fontmake -g ${tempGlyphsSource} --output ttf --interpolate --overlaps-backend --autohint 

## clean up temp glyphs file
rm -rf $tempGlyphsSource

python sources/scripts/helpers/shorten-nameID-4-6.py autohinted/instance_ttf

for file in autohinted/instance_ttf/*; do 
if [ -f "$file" ]; then 
    echo "fix DSIG in " ${file}
    gftools fix-dsig --autofix ${file}
fi 
done

# python scripts/helpers/shorten-nameID-4-6.py instance_otf

# for file in instance_otf/*; do 
# if [ -f "$file" ]; then 
#     echo "fix DSIG in " ${file}
#     gftools fix-dsig --autofix ${file}
# fi 
# done

outputDir="fonts"

for file in autohinted/instance_ttf/*; do 
if [ -f "$file" ]; then 
    fileName=$(basename $file)
    echo $fileName
    if [[ $file == *"EncodeSansCondensed-"* ]]; then
        newPath=${outputDir}/encodesanscondensed/static/${fileName}
        cp ${file} ${newPath}
        fontbakery check-googlefonts ${newPath} --ghmarkdown ${newPath/".ttf"/"-fontbakery-report.md"}
    fi
    if [[ $file == *"EncodeSansSemiCondensed-"* ]]; then
        newPath=${outputDir}/encodesanssemicondensed/static/${fileName}
        cp ${file} ${newPath}
        fontbakery check-googlefonts ${newPath} --ghmarkdown ${newPath/".ttf"/"-fontbakery-report.md"}
    fi
    if [[ $file == *"EncodeSans-"* ]]; then
        newPath=${outputDir}/encodesans/static/${fileName}
        cp ${file} ${newPath}
        fontbakery check-googlefonts ${newPath} --ghmarkdown ${newPath/".ttf"/"-fontbakery-report.md"}
    fi
    if [[ $file == *"EncodeSansSemiExpanded-"* ]]; then
        newPath=${outputDir}/encodesanssemiexpanded/static/${fileName}
        cp ${file} ${newPath}
        fontbakery check-googlefonts ${newPath} --ghmarkdown ${newPath/".ttf"/"-fontbakery-report.md"}
    fi
    if [[ $file == *"EncodeSansExpanded-"* ]]; then
        newPath=${outputDir}/encodesansexpanded/static/${fileName}
        cp ${file} ${newPath}
        fontbakery check-googlefonts ${newPath} --ghmarkdown ${newPath/".ttf"/"-fontbakery-report.md"}
    fi
fi 
done

rm -rf autohinted