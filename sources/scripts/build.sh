# flag technique from Jon Almeida: https://jonalmeida.com/posts/2013/05/26/different-ways-to-implement-flags-in-bash/

source venv/bin/activate

while [ ! $# -eq 0 ]
    do
    case "$1" in
        --statics | -s)
            source $(dirname ${BASH_SOURCE[0]})/build-statics.sh
        ;;
        --split | -sp)
            source $(dirname ${BASH_SOURCE[0]})/build-split-vf.sh -c
            source $(dirname ${BASH_SOURCE[0]})/build-split-vf.sh -sc
            source $(dirname ${BASH_SOURCE[0]})/build-split-vf.sh -n
            source $(dirname ${BASH_SOURCE[0]})/build-split-vf.sh -se
            source $(dirname ${BASH_SOURCE[0]})/build-split-vf.sh -e
        ;;
        --full | -f)
            source $(dirname ${BASH_SOURCE[0]})/build-full.sh
        ;;
        --all | -a)
            # statics
            source $(dirname ${BASH_SOURCE[0]})/build-statics.sh
            # full VF
            source $(dirname ${BASH_SOURCE[0]})/build-full.sh
            # all split VFs
            source $(dirname ${BASH_SOURCE[0]})/build-split-vf.sh -c
            source $(dirname ${BASH_SOURCE[0]})/build-split-vf.sh -sc
            source $(dirname ${BASH_SOURCE[0]})/build-split-vf.sh -n
            source $(dirname ${BASH_SOURCE[0]})/build-split-vf.sh -se
            source $(dirname ${BASH_SOURCE[0]})/build-split-vf.sh -e

        ;;
        *)
            echo "Please use argument -statics, --normal, or --full, or --all to build some or all of the font files"
    esac
    shift
done