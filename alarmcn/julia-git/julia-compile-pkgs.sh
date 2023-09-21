#!/bin/sh

if [ -f /usr/lib/julia/.package-precompile-env ]; then
    . /usr/lib/julia/.package-precompile-env
fi

exec /usr/bin/julia --startup-file=no \
     /usr/lib/julia/julia-compile-pkgs.jl /usr/share/julia
