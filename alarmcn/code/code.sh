#!/bin/bash

set -euo pipefail

flags_file="${XDG_CONFIG_HOME:-$HOME/.config}/code-flags.conf"

declare -a codeflags

if [[ -f "${flags_file}" ]]; then
    mapfile -t < "${flags_file}" CODEMAPFILE
fi

for line in "${CODEMAPFILE[@]}"; do
    if [[ ! "${line}" =~ ^[[:space:]]*#.* ]]; then
        codeflags+=("${line}")
    fi
done

# don't edit the electron binary name here! simply change the variable in the PKGBUILD and we will sed it into the correct one :)
name=electron
flags_file="${XDG_CONFIG_HOME:-$HOME/.config}/${name}-flags.conf"

declare -a electronflags

if [[ -f "${flags_file}" ]]; then
    mapfile -t < "${flags_file}" ELECTRONMAPFILE
fi

for line in "${ELECTRONMAPFILE[@]}"; do
    if [[ ! "${line}" =~ ^[[:space:]]*#.* ]]; then
        electronflags+=("${line}")
    fi
done

ELECTRON_RUN_AS_NODE=1 exec /usr/lib/${name}/electron /usr/lib/code/out/cli.js "${electronflags[@]}" /usr/lib/code/code.mjs "${codeflags[@]}" "$@"
