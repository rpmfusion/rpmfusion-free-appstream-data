#!/bin/bash
RELEASE=""
URL=""

main ()
{
    mkdir rpmfusion-free/ -pv
    cd rpmfusion-free || exit -1

    if [ "$RELEASE" =  "8" ]; then
        URL="rsync://rsync.mirrorservice.org/download1.rpmfusion.org/free/el/updates/8/x86_64/*"

    fi

    rsync -avPh "$URL" .
    rm -rf repo*
#
    appstream-builder --verbose --max-threads=6 --log-dir=./logs/ \
    --packages-dir=./ --temp-dir=./tmp/ --output-dir=./appstream-data/ \
    --basename="rpmfusion-free-el$RELEASE" --origin="rpmfusion-free-el$RELEASE" \
    --enable-hidpi

    echo "Generated files are present in the appstream-data directory"
}

usage ()
{
    echo "$0 -r <release>"
    echo "- update appdata for rpmfusion free repository"
    echo "options:"
    echo "-r <release> one of 8"
}


if [ "$#" -eq 0 ]; then
    usage
    exit 0
fi

# parse options
while getopts "r:h" OPTION
do
    case $OPTION in
        r)
            RELEASE=$OPTARG
            main
            ;;
        h)
            usage
            exit 1
            ;;
        ?)
            usage
            exit 1
            ;;
    esac
done
