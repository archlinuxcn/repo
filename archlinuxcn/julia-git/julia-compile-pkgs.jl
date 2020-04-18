#!/usr/bin/julia

using Pkg

function find_src(name)
    path = joinpath(Sys.STDLIB, "$name.jl")
    isfile(path) && return path
    path = joinpath(Sys.STDLIB, name, "src", "$name.jl")
    isfile(path) && return path
    return nothing
end

function check_src(name)
    path = find_src(name)
    path === nothing && return
    # Use a heuristic similar to `Pkg.jl` for now.
    # If it is really an issue we could put a tag file in the package that doesn't
    # want precompilation or even patch the affected package in PKGBUILD.
    occursin(r"\b__precompile__\(\s*false\s*\)", read(path, String)) && return
    return path
end

function precompile(path)
    Core.eval(Base, :(is_interactive = true))
    insert!(Base.DEPOT_PATH, 1, path)
    for pkg in readdir(Sys.STDLIB)
        path = check_src(pkg)
        path === nothing && continue
        id = Base.project_deps_get(Sys.STDLIB, pkg)
        id === nothing && continue
        Base.root_module_exists(id) && continue # Already loaded, this is a stdlib library.
        try
            Base.compilecache(id, path)
        catch e
            @show e
        end
    end
    Core.eval(Base, :(is_interactive = false))
end

precompile(ARGS[1])
