# ### based on build script for Encode-Sans-VF, by Mike LaGuttuta

# cp sources/Encode-Sans.glyphs sources/Encode-Sans-Build.glyphs

# python2 scripts/fix-designspace.py sources/Encode-Sans-Build.glyphs

# fontmake -o variable -g sources/Encode-Sans-Build.glyphs

# rm -rf master_ufo
# rm -rf sources/Encode-Sans-Build.glyphs

# cd variable_ttf

# gftools fix-nonhinting EncodeSans-VF.ttf EncodeSans-VF.ttf
# gftools fix-dsig --autofix EncodeSans-VF.ttf
# gftools fix-gasp EncodeSans-VF.ttf

# ttx EncodeSans-VF.ttf

# rm -rf EncodeSans-VF.ttf
# rm -rf EncodeSans-VF-backup-fonttools-prep-gasp.ttf

# cd ..

# cat variable_ttf/EncodeSans-VF.ttx | tr '\n' '\r' | sed -e "s~<name>.*<\/name>~$(cat scripts/patch.xml | tr '\n' '\r')~" | tr '\r' '\n' > variable_ttf/EncodeSans-VF-name.ttx
# cat variable_ttf/EncodeSans-VF-name.ttx | tr '\n' '\r' | sed -e "s,<STAT>.*<\/STAT>,$(cat scripts/patch2.xml | tr '\n' '\r')," | tr '\r' '\n' > variable_ttf/EncodeSans-VF.ttx

# # rm -rf variable_ttf
# rm -rf variable_ttf/EncodeSans-VF-name.ttx

# ttx variable_ttf/EncodeSans-VF.ttx

# rm -rf variable_ttf/EncodeSans-VF.ttx

# # move font into dist, with timestamp – probably with a python script and datetime
# # fontbake the font

python3 scripts/distdate-and-fontbake.py variable_ttf/EncodeSans-VF.ttf