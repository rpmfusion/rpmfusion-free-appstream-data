#!/bin/bash
TYPE="free"

main ()
{
    RAWHIDE="$(curl --silent --get https://bodhi.fedoraproject.org/releases/rawhide | jq -r '.version')"
    RELEASE="$(git branch --show-current)"

    if [ "$RELEASE" == "master" ] || [ "$RELEASE" == "rawhide" ] || [ "$RELEASE" == "main" ]
    then
        RELEASE=$RAWHIDE
    fi

    echo "Current release is: $RELEASE"

    URL_DEV=""
    URL_RELEASE=""
    TEMPDIR="rpmfusion-$TYPE"

    rm -rf "$TEMPDIR"
    mkdir "$TEMPDIR" -pv
    cd "$TEMPDIR" || exit -1

    if [ $RELEASE -le $RAWHIDE ] && [ $RELEASE -ge $((RAWHIDE - 3)) ]; then
        if [ "$RELEASE" == "$RAWHIDE" ]
        then
            URL_DEV="rsync://download1.rpmfusion.org/rpmfusion/$TYPE/fedora/development/rawhide/Everything/x86_64/os/*"
        else
            URL_DEV="rsync://download1.rpmfusion.org/rpmfusion/$TYPE/fedora/development/${RELEASE}/Everything/x86_64/os/*"
        fi
        URL_RELEASE="rsync://download1.rpmfusion.org/rpmfusion/$TYPE/fedora/releases/${RELEASE}/Everything/x86_64/os/*"

        echo "Regenerating for $RELEASE"
        rsync -avPh "$URL_RELEASE" . || rsync -avPh "$URL_DEV" .
    else
        echo "Please check if ${RELEASE} is currently supported. Rawhide is at ${RAWHIDE}."
        exit -1
    fi

    if ! command -v appstream-builder > /dev/null
    then
        echo "appstream-builder not installed. Installing now."
        sudo dnf install /usr/bin/appstream-builder -y
    fi

    appstream-builder --verbose --include-failed --log-dir=./logs/ \
    --packages-dir=./Packages/ --temp-dir=./tmp/ --output-dir=./appstream-data/ \
    --basename="rpmfusion-$TYPE-$RELEASE" --origin="rpmfusion-$TYPE-$RELEASE" \
    --veto-ignore=missing-parents

    echo "Generated files are present in the appstream-data directory"
    echo "To import new sources, run:"
    echo "rfpkg new-sources ${TEMPDIR}/appstream-data/rpmfusion-$TYPE-${RELEASE}-icons.tar.gz ${TEMPDIR}/appstream-data/rpmfusion-$TYPE-${RELEASE}.xml.gz"

    echo "To bump the spec:"
    echo "rpmdev-bumpspec -c "Regenerate" rpmfusion-$TYPE-appstream-data.spec"

}

usage ()
{
    echo "$0: update appdata for rpmfusion $TYPE repository"
}


if [ "$#" -ne 0 ]; then
    usage
    exit 0
fi


main
