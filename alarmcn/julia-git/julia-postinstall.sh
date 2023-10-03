#!/bin/sh

if [ -f /usr/lib/julia/.package-precompile-env ]; then
    . /usr/lib/julia/.package-precompile-env
fi

for d in "$2"/*; do
    if [[ -d "$d" ]]; then
        ln -sr "$d" "$1"/
    fi
done

exec /usr/bin/julia --startup-file=no \
     /usr/lib/julia/julia-compile-pkgs.jl /usr/share/julia
