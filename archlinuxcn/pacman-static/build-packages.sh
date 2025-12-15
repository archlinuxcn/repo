#!/bin/sh

# requires devtools, devtools32 (for extra-i686-build)
# if debug variants of extra-* exist, use them (I have a custom script for this)

rm -rf artifacts/

for buildarch in x86_64 i686; do
    extradir=artifacts/${buildarch}-extracted

    if command -v debug-${buildarch}-build; then
        debug-${buildarch}-build
    else
        extra-${buildarch}-build
    fi

    CARCH=${buildarch} makepkg --packagelist | while read -r pkgfile; do
        if bsdtar -tf "${pkgfile}" usr/bin/pacman-static > /dev/null 2>&1; then
            mkdir -p ${extradir}
            bsdtar --strip-components 2 -C ${extradir} -xf "${pkgfile}" usr/bin/pacman-static
            break
        fi
    done

    xz -ke ${extradir}/pacman-static
    gpg --detach-sign ${extradir}/pacman-static
    gpg --detach-sign ${extradir}/pacman-static.xz
done
