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
    # make sure we are up-to-date with upstream master
    git checkout master
    git pull upstream master
    git reset --hard
    # checkout fresh branch
    git checkout -B $subfamilyName-vf
    # clear out any lingering, untracked files
    git reset --hard
    git clean -f -d

    # -------------------------------------------------------------------
    # cleanup existing files --------------------------------------------

    oldFonts=$(ls ofl/$subfamilyName/*.ttf)

    for oldFont in $oldFonts; do
        echo old font: $oldFont
        rm -rf $oldFont
    done

    # -------------------------------------------------------------------
    # move fonts --------------------------------------------------------
    mkdir -p ofl/$subfamilyName

    # copy font in split_vf to the branch
    splitVF=$(ls $encodeDir/$subfamilyDir/split_vf/*.ttf) # should be only one file
    cp $splitVF ofl/$subfamilyName/$(basename $splitVF)

    # copy description
    cp $encodeDir/$subfamilyDir/DESCRIPTION.en_us.html ofl/$subfamilyName/DESCRIPTION.en_us.html

    # make new Metadata
    gftools add-font ofl/$subfamilyName

    # copy in statics to "static" folder
    mkdir -p ofl/$subfamilyName/static
    staticsToMove=$(ls $encodeDir/$subfamilyDir/static/*.ttf)
    for static in $staticsToMove; do
        cp $static ofl/$subfamilyName/static/$(basename $static)
    done

    # -------------------------------------------------------------------
    # commit files ------------------------------------------------------

    git add .
    git commit -m "add fresh split VF and statics for ofl/$subfamilyName"

    # push to upstream branch (you must manually go to GitHub to make PR from there)
    git push --force origin $subfamilyName-vf

    # reset as needed
    cd $encodeDir
    git checkout master
fi
done

