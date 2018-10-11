# based on build script for Encode-Sans-VF, by Mike LaGuttuta

cp sources/Encode-Sans.glyphs sources/Encode-Sans-Build.glyphs

python2 scripts/fix-designspace.py sources/Encode-Sans-Build.glyphs

fontmake -o variable -g Encode-Sans-Build.glyphs

rm -rf master_ufo
rm -rf Encode-Sans-Build.glyphs

cd variable_ttf

gftools fix-nonhinting Encode-Sans-VF.ttf Encode-Sans-VF.ttf
gftools fix-dsig --autofix Encode-Sans-VF.ttf
gftools fix-gasp Encode-Sans-VF.ttf

ttx Encode-Sans-VF.ttf

rm -rf Encode-Sans-VF.ttf
rm -rf Encode-Sans-VF-backup-fonttools-prep-gasp.ttf

cd ..

cat variable_ttf/Encode-Sans-VF.ttx | tr '\n' '\r' | sed -e "s~<name>.*<\/name>~$(cat scripts/patch.xml | tr '\n' '\r')~" | tr '\r' '\n' > Encode-Sans-VF-name.ttx
cat Encode-Sans-VF-name.ttx | tr '\n' '\r' | sed -e "s,<STAT>.*<\/STAT>,$(cat scripts/patch2.xml | tr '\n' '\r')," | tr '\r' '\n' > Encode-Sans-VF.ttx

rm -rf variable_ttf
rm -rf Encode-Sans-VF-name.ttx

ttx Encode-Sans-VF.ttx

rm -rf Encode-Sans-VF.ttx