#!/bin/bash

# This script copies the latest builds to the google fonts dir in order to run QA checks and prep for a PR
#
# USAGE: 
# call this script from the root of your encode repo, with the absolute path your your google/fonts repo:
# `move-check <your_username>/<path>/fonts`

set -e
source venv/bin/activate

gFontsDir=$1

if [[ -z "$gFontsDir" || $gFontsDir = "--help" ]] ; then
    echo 'Add absolute path to your Google Fonts Git directory, like:'
    echo 'move-check /Users/username/type-repos/google-font-repos/fonts'
    exit 2
fi

fontDirs=$(ls -d fonts/*)

encodeDir=$(pwd)
encodeQADir=$encodeDir/misc/googlefonts-qa

for subfamilyDir in $fontDirs; do
if [[ $subfamilyDir != *"sc" ]]; then #exclude SC versions, per Marc's request
    subfamilyName=$(basename $subfamilyDir)

    echo ===========================================
    echo $subfamilyDir
    # -------------------------------------------------------------------
    # navigate to google/fonts repo, then make PR branch ----------------

    cd $gFontsDir
    git checkout master
    git pull upstream master
    git checkout -B $subfamilyName-vf
    git reset --hard

    # -------------------------------------------------------------------
    # cleanup existing files --------------------------------------------

    oldFonts=$(ls ofl/$subfamilyName/*.ttf)

    for oldFont in $oldFonts; do
        echo old font: $oldFont
        rm -rf $oldFont
    done

    # -------------------------------------------------------------------
    # move fonts --------------------------------------------------------
    mkdir -p ofl/$(basename $subfamilyDir)

    # copy font in split_vf to the branch
    splitVF=$(ls $encodeDir/$subfamilyDir/split_vf/*.ttf) # should only be one
    cp $splitVF ofl/$subfamilyName/$(basename $splitVF)

    # copy in statics to "static" folder

    

    # push to upstream branch to make PR simple
    # TODO: ¿Make a PR from the command line?

    # reset as needed
    cd $encodeDir
    # git checkout master
fi
done
