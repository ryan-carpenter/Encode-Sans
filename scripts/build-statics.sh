for file in autohinted/instance_ttf/*; do 
    if [ -f "$file" ]; then 
        echo "fix DSIG in " ${file}
        gftools fix-dsig --autofix ${file}
    fi 
done