
fontbakeFile()
{
    FILEPATH=$1
    fontbakery check-googlefonts ${FILEPATH} --ghmarkdown ${FILEPATH/".ttf"/"-fontbakery-report.md"}
}


for file in fonts/encodesanscondensed/static/*; do 
if [ -f "$file" ]; then 
    echo checking $file
    # if [[ $file == *"EncodeSans"* ]]; then
    if [[ $file == *".ttf"* ]]; then
        fontbakeFile ${file}
    fi
fi 
done
for file in fonts/encodesanssemicondensed/static/*; do 
if [ -f "$file" ]; then 
    echo checking $file
    if [[ $file == *"EncodeSans"* ]]; then
        fontbakeFile ${file}
    fi
fi 
done
for file in fonts/encodesansstatic/*; do 
if [ -f "$file" ]; then 
    echo checking $file
    if [[ $file == *"EncodeSans"* ]]; then
        fontbakeFile ${file}
    fi
fi 
done
for file in fonts/encodesanssemiexpanded/static/*; do 
if [ -f "$file" ]; then 
    echo checking $file
    if [[ $file == *"EncodeSans"* ]]; then
        fontbakeFile ${file}
    fi
fi 
done
for file in fonts/encodesansexpanded/static/*; do 
if [ -f "$file" ]; then 
    echo checking $file
    if [[ $file == *"EncodeSans"* ]]; then
        fontbakeFile ${file}
    fi
fi 
done