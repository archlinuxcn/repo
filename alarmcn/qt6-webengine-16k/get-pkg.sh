#!/bin/bash

git clone --depth 1 https://github.com/archlinuxarm/PKGBUILDs
mv PKGBUILDs/extra/qt6-webengine/* .
rm -rf PKGBUILDs/

# Replace use of pkgname
sed -i -e 's/\bpkgname\b/_orig_pkgname/g' PKGBUILD

{
    while IFS= read -r line; do
        case "$line" in
            groups=*)
                # Remove group
                continue
                ;;
            arch=*)
                # Fix arch
                line='arch=(aarch64 armv7h x86_64)'
                ;;
            _orig_pkgname=*)
                # Replace pkgname
                echo "pkgname=qt6-webengine-16k"
                ;;
        esac
        printf '%s\n' "$line"
        case "$line" in
            build\(*)
                echo "  _prebuild"
                continue
                ;;
        esac
    done < PKGBUILD
    cat <<EOF
source+=(qt6-webengine-16kpage.patch)
provides+=(qt6-webengine)
conflicts+=(qt6-webengine)
_prebuild() {
  export NINJAJOBS="-j3"
  export NINJAFLAGS="-j3"
  patch -p1 -d "\$srcdir/qtwebengine/src/3rdparty" -i "\$srcdir"/qt6-webengine-16kpage.patch # Support 16k page
}
EOF
} > PKGBUILD.tmp

mv PKGBUILD.tmp PKGBUILD

updpkgsums || true
