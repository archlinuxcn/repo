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

function add_precompile_deps(compiled, pkg)
    caches = Base.find_all_in_cache_path(pkg)
    if isempty(caches)
        println(stderr, "Warning: Unable to find cache file for $(pkg.name).")
        return
    end
    for (dep, build) in Base.parse_cache_header(caches[1])[3]
        Base.root_module_exists(dep) && continue # Already loaded, this is a stdlib library.
        if !(dep.name in compiled)
            println(stderr, "$(dep.name) compiled as dependency.")
            push!(compiled, dep.name)
            add_precompile_deps(compiled, dep)
        end
    end
end

function precompile(path)
    Core.eval(Base, :(is_interactive = true))
    compiled = Set{String}()
    insert!(Base.DEPOT_PATH, 1, path)
    resize!(Base.DEPOT_PATH, 1)
    # TODO do a topological sort first
    for pkg in readdir(Sys.STDLIB)
        pkg in compiled && continue
        path = check_src(pkg)
        path === nothing && continue
        id = Base.project_deps_get(Sys.STDLIB, pkg)
        id === nothing && continue
        Base.root_module_exists(id) && continue # Already loaded, this is a stdlib library.
        push!(compiled, pkg)
        try
            Base.compilecache(id, path)
            add_precompile_deps(compiled, id)
        catch e
            @show e
        end
    end
    Core.eval(Base, :(is_interactive = false))
end

precompile(ARGS[1])
