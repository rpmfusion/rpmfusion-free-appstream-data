#!/bin/bash
RELEASE=""
URL=""
#URL1=""

main ()
{
    mkdir rpmfusion-free/ -pv
    cd rpmfusion-free || exit -1

    if [ "$RELEASE" =  "34" ]; then
        URL="rsync://download1.rpmfusion.org/rpmfusion/free/fedora/development/rawhide/Everything/x86_64/os/*"
    elif [ "$RELEASE" = "33" ]; then
        URL="rsync://download1.rpmfusion.org/rpmfusion/free/fedora/development/33/Everything/x86_64/os/*"
    elif [ "$RELEASE" = "32" ]; then
        URL="rsync://download1.rpmfusion.org/rpmfusion/free/fedora/releases/32/Everything/x86_64/os/*"
        #URL1="rsync://download1.rpmfusion.org/rpmfusion/free/fedora/updates/32/x86_64/*"
    elif [ "$RELEASE" = "31" ]; then
        URL="rsync://download1.rpmfusion.org/rpmfusion/free/fedora/releases/31/Everything/x86_64/os/*"
        #URL1="rsync://download1.rpmfusion.org/rpmfusion/free/fedora/updates/31/x86_64/*"

    fi

    rsync -avPh "$URL" .
#    rsync -avPh --exclude debug "$URL1" ./Packages/

    rm -rf repo*
#    rm -rf Packages/repo*
#    createrepo -d Packages/
#    repomanage -o --space  ./Packages/ | xargs rm
#    rm -rf Packages/repo*
#
    appstream-builder --verbose --include-failed --max-threads=6 --log-dir=./logs/ \
    --packages-dir=./Packages/ --temp-dir=./tmp/ --output-dir=./appstream-data/ \
    --basename="rpmfusion-free-$RELEASE" --origin="rpmfusion-free-$RELEASE" \
    --enable-hidpi --veto-ignore=missing-parents

    echo "Generated files are present in the appstream-data directory"
}

usage ()
{
    echo "$0 -r <release>"
    echo "- update appdata for rpmfusion free repository"
    echo "options:"
    echo "-r <release> one of 31, 32, 33 and 34"
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
