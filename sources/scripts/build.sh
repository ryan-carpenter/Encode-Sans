
# flag technique from Jon Almeida: https://jonalmeida.com/posts/2013/05/26/different-ways-to-implement-flags-in-bash/

while [ ! $# -eq 0 ]
    do
    case "$1" in
        --statics | -s)
            source $(dirname ${BASH_SOURCE[0]})/build-statics.sh
        ;;
        --normal | -n)
            source $(dirname ${BASH_SOURCE[0]})/build-normal-width-vf.sh
        ;;
        --full | -f)
            source $(dirname ${BASH_SOURCE[0]})/build-full.sh
        ;;
        --all | -a)
            source $(dirname ${BASH_SOURCE[0]})/build-statics.sh
            source $(dirname ${BASH_SOURCE[0]})/build-normal-width-vf.sh
            source $(dirname ${BASH_SOURCE[0]})/build-full.sh
        ;;
        *)
            echo "Please use argument -statics, --normal, or --full, or --all to build some or all of the font files"
    esac
    shift
done