#!/bin/bash

sh get_pkg.sh asahi-meta

if grep -q 'package()' PKGBUILD; then
    # Already fixed upstream
    exit 0
fi

in_depends=0
while read line; do
    case "$line" in
        depends=*)
            echo "package() {"
            in_depends=1
            ;;
    esac
    printf '%s\n' "$line"
    case "$line" in
        *\))
            if ((in_depends)); then
                in_depends=0
                echo "}"
            fi
            ;;
    esac
done < PKGBUILD > PKGBUILD.patched
mv PKGBUILD.patched PKGBUILD
