

for file in fonts/encodesanscondensed/static/*; do 
if [ -f "$file" ]; then 
    echo checking $file
    if [[ $file == *"EncodeSans"* ]]; then
        fontbakery check-googlefonts ${file} --ghmarkdown ${file/".ttf"/"-fontbakery-report.md"}
    fi
fi 
done
for file in fonts/encodesanssemicondensed/static/*; do 
if [ -f "$file" ]; then 
    echo checking $file
    if [[ $file == *"EncodeSans"* ]]; then
        fontbakery check-googlefonts ${file} --ghmarkdown ${file/".ttf"/"-fontbakery-report.md"}
    fi
fi 
done
for file in fonts/encodesansstatic/*; do 
if [ -f "$file" ]; then 
    echo checking $file
    if [[ $file == *"EncodeSans"* ]]; then
        fontbakery check-googlefonts ${file} --ghmarkdown ${file/".ttf"/"-fontbakery-report.md"}
    fi
fi 
done
for file in fonts/encodesanssemiexpanded/static/*; do 
if [ -f "$file" ]; then 
    echo checking $file
    if [[ $file == *"EncodeSans"* ]]; then
        fontbakery check-googlefonts ${file} --ghmarkdown ${file/".ttf"/"-fontbakery-report.md"}
    fi
fi 
done
for file in fonts/encodesansexpanded/static/*; do 
if [ -f "$file" ]; then 
    echo checking $file
    if [[ $file == *"EncodeSans"* ]]; then
        fontbakery check-googlefonts ${file} --ghmarkdown ${file/".ttf"/"-fontbakery-report.md"}
    fi
fi 
done