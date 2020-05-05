# flag technique from Jon Almeida: https://jonalmeida.com/posts/2013/05/26/different-ways-to-implement-flags-in-bash/

source venv/bin/activate

while [ ! $# -eq 0 ]
    do
    case "$1" in
        --statics | -s)
            source $(dirname ${BASH_SOURCE[0]})/build-statics.sh
        ;;
        --variable | -v)
            source $(dirname ${BASH_SOURCE[0]})/build-vf.sh
        ;;
    esac
    shift
done

if [ -z $1 ]; then
    # statics
    source $(dirname ${BASH_SOURCE[0]})/build-statics.sh
    # variable
    source $(dirname ${BASH_SOURCE[0]})/build-vf.sh
fi
