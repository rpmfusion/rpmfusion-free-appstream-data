#!/bin/bash
RELEASE=""
URL=""

main ()
{
    mkdir rpmfusion-free/ -pv
    cd rpmfusion-free || exit -1

    if [ "$RELEASE" =  "32" ]; then
        URL="rsync://rsync.mirrorservice.org/download1.rpmfusion.org/free/fedora/development/rawhide/Everything/x86_64/os/*"
    elif [ "$RELEASE" = "31" ]; then
        URL="rsync://rsync.mirrorservice.org/download1.rpmfusion.org/free/fedora/development/31/Everything/x86_64/os/*"
    elif [ "$RELEASE" = "30" ]; then
        URL="rsync://rsync.mirrorservice.org/download1.rpmfusion.org/free/fedora/releases/30/Everything/x86_64/os/*"
    elif [ "$RELEASE" = "29" ]; then
        URL="rsync://rsync.mirrorservice.org/download1.rpmfusion.org/free/fedora/releases/29/Everything/x86_64/os/*"

    fi

    rsync -avPh "$URL" .
    rm -rf repo*
#
    appstream-builder --verbose --max-threads=6 --log-dir=./logs/ \
    --packages-dir=./Packages/ --temp-dir=./tmp/ --output-dir=./appstream-data/ \
    --basename="rpmfusion-free-$RELEASE" --origin="rpmfusion-free-$RELEASE" \
    --enable-hidpi

    echo "Generated files are present in the appstream-data directory"
}

usage ()
{
    echo "$0 -r <release>"
    echo "- update appdata for rpmfusion free repository"
    echo "options:"
    echo "-r <release> one of 29, 30, 31, and 32"
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
