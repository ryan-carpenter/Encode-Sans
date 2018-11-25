for file in instance_otf/*; do 
    if [ -f "$file" ]; then 
        echo "fix DSIG in " ${file}
        gftools fix-dsig --autofix ${file}
    fi 
    done