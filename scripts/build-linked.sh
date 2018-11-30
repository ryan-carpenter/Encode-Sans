### WIP macOS build script for Encode Sans VF, based on a build script by Mike LaGuttuta
### Run in the terminal by entering this file path
### requires a python 3 environment


############################################
################# set vars #################

glyphsSources="sources/split"

## move VF into new folder of dist/ with timestamp and fontbake
timestampAndFontbakeInDist=true

## keep designspace file if you want to check values later
keepDesignspace=true

################# set vars #################
############################################

for file in ${glyphsSources}/*; do 
    if [ -f "$file" ]; then 
        ## make temp glyphs filename with "-build" suffix
        tempGlyphsSource=${file/".glyphs"/"-build.glyphs"}

        cp $file $tempGlyphsSource

        # get font name from glyphs source
        VFname=`python scripts/helpers/get-font-name.py ${file}`
        # checking that the name has been pulled out of the source file
        echo "VF Name: ${VFname}"

        ## call fontmake to make a varfont
        fontmake -o variable -g $tempGlyphsSource

        ## clean up temp glyphs file
        rm -rf $tempGlyphsSource
    fi 
done

# fix name length in generated VFs
python scripts/helpers/shorten-nameID-4-6.py variable_ttf

for file in variable_ttf/*; do 
    if [ -f "$file" ]; then 
        echo "fix DSIG in " ${file}
        gftools fix-dsig --autofix ${file}
    fi 
done



for file in variable_ttf/*; do 
    if [ -f "$file" ]; then
        echo ${file}
        # if you set timestampAndFontbakeInDist variable to true, this creates a new folder in 'dist' to put it into and run fontbake on
        if [ $timestampAndFontbakeInDist == true ]
        then
            ## move font into folder of dist/, with timestamp, then fontbake the font
            pwd
            python3 scripts/helpers/distdate-and-fontbake.py "EncodeSans-VF" "linked_vf" ${file}
        else
            ttx ${file}
            echo "font and ttx in variable_ttf folder"
        fi
    fi 
done

#  TODO Add NAMEpatch??

rm -rf variable_ttf

if [ $keepDesignspace == true ]
then
    echo "designspace in master_ufo folder"
else
    rm -rf master_ufo
fi
