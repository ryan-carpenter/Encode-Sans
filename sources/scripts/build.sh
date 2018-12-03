
# flag technique from Jon Almeida: https://jonalmeida.com/posts/2013/05/26/different-ways-to-implement-flags-in-bash/

# TODO: separate scripts for flags
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
            source $(dirname ${BASH_SOURCE[0]})/build-static.sh
            source $(dirname ${BASH_SOURCE[0]})/build-linked.sh
            source $(dirname ${BASH_SOURCE[0]})/build-full.sh
        ;;
    esac
    shift
done