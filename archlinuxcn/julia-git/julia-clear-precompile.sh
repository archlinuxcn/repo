#!/bin/bash

for d in "$1"/*; do
    if [[ -f "$d"/.archpkg ]]; then
        # Packaged precompiled cache, do not delete
        continue
    fi
    rm -rf "$d" &> /dev/null
done
