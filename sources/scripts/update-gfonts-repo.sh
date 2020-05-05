#!/bin/bash

# This script copies the latest builds to the google fonts dir in order to run QA checks and prep for a PR
#
# USAGE: 
# Install requirements with `pip install -U -r misc/googlefonts-qa/requirements.txt`
# 
# after  `misc/googlefonts-qa/build.sh`
# call this script from the root of your inter repo, with the absolute path your your google/fonts repo
# `misc/googlefonts-qa/fix-move-check.sh <your_username>/<path>/fonts`
#
# add `push` to the end if you wish to push the result to GitHub

projectDir=$(pwd)

# -------------------------------------------------------------------
# UPDATE VARIABLES ABOVE AS NEEDED

gFontsDir="/Users/stephennixon/type-repos/google-font-repos/fonts" # absolute path to your google/fonts repo directory

category="SAN_SERIF"
designer="Impallari Type, Andres Torresi, Jacques Le Bailly"


if [[ $1 = "smallcaps" || $1 =  "sc" ]] ; then
    gFontsSubDir="encodesanssc"                                     # name for this directory within google/fonts/ofl
    fontDir=$projectDir/fonts/EncodeSansSC
    fontPath=$fontDir/EncodeSansSC\[wdth,wght\].ttf

elif [[ $1 = "normal" || $1 = "n" ]] ; then
    gFontsSubDir="encodesans"                                     # name for this directory within google/fonts/ofl
    fontDir=$projectDir/fonts/EncodeSans
    fontPath=$fontDir/EncodeSans\[wdth,wght\].ttf
fi

# option to push to GitHub. Without this, it will do a dry run.
pushToGitHub=$2

# UPDATE VARIABLES ABOVE AS NEEDED
# -------------------------------------------------------------------

set -e
source venv/bin/activate

# -------------------------------------------------------------------
# get latest font version to use in PR commit message 
set +e

ttx -t head $fontPath
fontVersion=v$(xml sel -t --match "//*/fontRevision" -v "@value" ${fontPath/".ttf"/".ttx"}) # TODO?: convert to a TTFont script

echo $fontVersion

rm ${fontPath/".ttf"/".ttx"}

set -e

# -------------------------------------------------------------------
# navigate to google/fonts repo, get latest, then clear branch & font subdirectory

cd $gFontsDir
git checkout master
git pull upstream master
git reset --hard
git checkout -B $gFontsSubDir
git clean -f -d
[ -d ofl/$gFontsSubDir ] && rm -r ofl/$gFontsSubDir

# -------------------------------------------------------------------
# copy fonts

mkdir -p ofl/$gFontsSubDir

cp $fontPath    ofl/$gFontsSubDir/$(basename $fontPath)

# -------------------------------------------------------------------
# make or move basic metadata 

gftools add-font ofl/$gFontsSubDir # do this the first time, then edit as needed 

# update these to be accurate if needed
sed -i "" "s/SANS_SERIF/$category/g" ofl/$gFontsSubDir/METADATA.pb
sed -i "" "s/UNKNOWN/$designer/g" ofl/$gFontsSubDir/METADATA.pb

cp $projectDir/OFL.txt ofl/$gFontsSubDir/OFL.txt

cp $projectDir/gfonts-description.html ofl/$gFontsSubDir/DESCRIPTION.en_us.html

# -------------------------------------------------------------------
# copy static fonts

cp -r $fontDir/static ofl/$gFontsSubDir/static

# -------------------------------------------------------------------
# adds and commits new changes, then force pushes

if [[ $pushToGitHub = "push" ]] ; then
    git add .
    git commit -m "$gFontsSubDir: $fontVersion added."

    # push to upstream branch (you must manually go to GitHub to make PR from there)
    # this is set to push to my upstream (google/fonts) rather than origin so that TravisCI can run
    git push --force upstream $gFontsSubDir
fi
