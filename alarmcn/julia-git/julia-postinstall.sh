#!/bin/sh

if [ -f /usr/lib/julia/.package-precompile-env ]; then
    . /usr/lib/julia/.package-precompile-env
fi

arch_site=/usr/share/julia/arch-site
arch_compiled=/usr/lib/julia/arch-compiled

for d in "$arch_site"/*; do
    if [[ -d "$d" ]]; then
        ln -sr "$d" "$2"/
    fi
done

for pkg in "$arch_compiled"/*/; do
    for m in "$pkg"/*; do
        mname=$(basename "$m")
        mkdir -p "$1/$mname"
        ln -srf "$m"/* "$1/$mname"/
    done
done

exec /usr/bin/julia --startup-file=no \
     /usr/lib/julia/julia-compile-pkgs.jl /usr/share/julia
