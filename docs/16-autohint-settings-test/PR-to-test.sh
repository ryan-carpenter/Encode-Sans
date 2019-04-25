#!/bin/bash

# This script makes separate PRs to m4rc1e/fonts to trigger diffenator tests of Encode with different autohint settings
#
# USAGE: 
# call this script from the root of your encode repo:
# $ chmod +x docs/16-autohint-settings-test/PR-to-test.sh
# $ docs/16-autohint-settings-test/PR-to-test.sh

# for file in hinted folder
#   make m4rc1e/fonts branch labeled with autohint settings
#   force push

set -ex
source venv/bin/activate

encodeDir=$(pwd)
fontDir=$(cd docs/16-autohint-settings-test/hintedFonts && pwd)
testFonts=$(ls docs/16-autohint-settings-test/hintedFonts)
marcFontsDir="/Users/stephennixon/type-repos/google-font-repos/m4rc1e-fonts"
subfamilyName="encodesans"


for ttf in $testFonts; do

    testName=${ttf/".ttf"/""}

    echo $testName

    cd $marcFontsDir
    git checkout master
    git pull origin master
    git reset --hard
    # checkout fresh branch
    git checkout -B $testName
    # clear out any lingering, untracked files
    git reset --hard
    git clean -f -d

    # ----------------------------------------
    # cleanup existing files -----------------

    oldFonts=$(ls ofl/$subfamilyName/*.ttf)

    for oldFont in $oldFonts; do
        echo old font: $oldFont
        rm -rf $oldFont
    done

    # ----------------------------------------
    # move fonts -----------------------------

    mkdir -p ofl/$subfamilyName

    cp $fontDir/$ttf ofl/$subfamilyName/$(basename $ttf)

    # ----------------------------------------
    # commit files ---------------------------

    git add .
    git commit -m "autohint test: $testName"

    git push --force --set-upstream origin $testName 

    # NEVERMIND, this requires login each time over HTTPS
    # https://github.com/github/hub/issues/2105
    # hub pull-request -m "autohint test VF for ofl/$subfamilyName"

    # reset as needed
    cd $encodeDir
    git checkout master

done
# use https://github.com/github/hub to make PRs