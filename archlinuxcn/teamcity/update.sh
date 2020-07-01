#!/bin/bash

# BEGIN functions for version comparison
verlte() {
    [  "$1" = "`echo -e "$1\n$2" | sort -V | head -n1`" ]
}

verlt() {
    [ "$1" = "$2" ] && return 1 || verlte $1 $2
}
# END functions


wget -O teamcity.json "https://data.services.jetbrains.com/products/releases?code=TC&latest=true&type=release&downloads=linux"
downloadLink=`JSON.sh -b < teamcity.json | grep '\["TC",0,"downloads","linux","link"\]' | sed -r 's/.*(https.*)"/\1/'`
checksumLink=`JSON.sh -b < teamcity.json | grep '\["TC",0,"downloads","linux","checksumLink"\]' | sed -r 's/.*(https.*)"/\1/'`
pkgver=`JSON.sh -b < teamcity.json | grep '\["TC",0,"version"\]' | cut -f2 | cut -d "\"" -f2`
oldpkgver=`grep -oP '(?<=pkgver = ).*' .SRCINFO`

verlt $oldpkgver $pkgver
if [ $? -eq 0 ]; then
    wget $downloadLink
    wget $checksumLink

    checksumFile=$(sed -r 's|.*/(.*\.tar\.gz\.sha256)|\1|' <<< $checksumLink)
    downloadFile=$(sed -r 's|.*/(.*\.tar\.gz)|\1|' <<< $downloadLink)

    sha256sum --status -c "$checksumFile"
    if [ $? -eq 0 ]; then
        checksum=`sha256sum "TeamCity-$pkgver.tar.gz" | cut -d " " -f1`
        sed -ri "s/pkgver=.*/pkgver=$pkgver/" ./PKGBUILD
        sed -ri "s/sha256sums=\('.*'/sha256sums=\('$checksum'/" ./PKGBUILD
        sed -ri "s|source=\(.*|source=\('$downloadLink'|" ./PKGBUILD
        makepkg --printsrcinfo > .SRCINFO
        rm $checksumFile
        rm $downloadFile
        printf "Built updated TeamCity package.\n\nOld version: %s\nNew version: %s" "$oldpkgver" "$pkgver"
    else
        echo "An error occured"
    fi
fi
