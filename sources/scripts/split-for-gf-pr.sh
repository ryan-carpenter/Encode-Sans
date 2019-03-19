#!/bin/bash

set -e

# for each family:
# grab files in fonts folder
# move to local google/fonts repo, create branch, add copy files

# temp: sort statics into static folders

fontDirs=$(ls -d fonts/*)

for dir in $fontDirs; do
    statics=$(ls $dir/*.ttf)
    echo $dir
    # echo $statics
    mkdir -p $dir/static
    for static in $statics; do
        echo $static
        echo $(basename $static)
        git mv $static $dir/static/$(basename $static)
    done
    echo ========================
done