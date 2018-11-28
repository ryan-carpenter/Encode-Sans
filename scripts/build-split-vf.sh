### WIP macOS build script for Encode Sans VF, based on a build script by Mike LaGuttuta
### Run in the terminal by entering this file path
### requires a python 3 environment


############################################
################# set vars #################

glyphsSources="sources/split"

## Set this. It's probably your font name without spaces, then "-VF"
# VFname="EncodeSans-VF"

## move VF into new folder of dist/ with timestamp and fontbake
timestampAndFontbakeInDist=true


################# set vars #################
############################################

for file in ${glyphsSources}/*; do 
    if [ -f "$file" ]; then 
        ## make temp glyphs filename with "-build" suffix
        tempGlyphsSource=${file/".glyphs"/"-build.glyphs"}

        cp $file $tempGlyphsSource

        # get font name from glyphs source
        VFname=`python scripts/helpers/get-font-name.py ${glyphsSource}`
        # checking that the name has been pulled out of the source file
        echo "VF Name: ${VFname}"

        ## call fontmake to make a varfont
        fontmake -o variable -g $tempGlyphsSource

        ## clean up temp glyphs file
        rm -rf $tempGlyphsSource
    fi 
done