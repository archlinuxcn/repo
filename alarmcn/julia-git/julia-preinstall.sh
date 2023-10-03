#!/bin/bash

# Clear precompiled cache from postinstall hook
for d in "$1"/*; do
    if [[ -f "$d"/.archpkg ]]; then
        # Packaged precompiled cache, do not delete
        continue
    fi
    rm -rf "$d" &> /dev/null
done

arch_site=$(realpath "$3")

# Clear symlink from arch-site
for d in "$2"/*; do
    if ! [[ -L "$d" ]]; then
        continue
    fi
    case "$(realpath "$d")" in
        "$arch_site"/*)
            rm "$d"
            ;;
    esac
done
