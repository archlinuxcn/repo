#!/bin/sh

for f in /usr/share/makepkg/lint_pkgbuild/*; do
    echo > "$f"
done
