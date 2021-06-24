#!/usr/bin/julia

using Pkg

function get_deps(pkg)
    try
        projfile = joinpath(Sys.STDLIB, pkg, "Project.toml")
        isfile(projfile) &&
            return String[dep for (dep, id) in Pkg.Types.read_project(projfile).deps]
    catch
    end
    try
        reqfile = joinpath(Sys.STDLIB, pkg, "REQUIRE")
        if isfile(reqfile)
            res = String[]
            for line in readlines(reqfile)
                line = strip(line)
                if isempty(line) || startswith(line, '#')
                    continue
                end
                pkg = split(split(line)[1], "#")[1]
                if !isempty(pkg) && pkg != "julia"
                    push!(res, pkg)
                end
            end
            return res
        end
    catch
    end
    return String[]
end

function add_compile_pkg(pkgs, pkg)
    pkg in pkgs && return
    for dep in get_deps(pkg)
        add_compile_pkg(pkgs, dep)
    end
    push!(pkgs, pkg)
end

if isdefined(Base, :TOMLCache) && !isdefined(Base, :CachedTOMLDict)
    project_deps_get(pkg) = Base.project_deps_get(Sys.STDLIB, pkg, Base.TOMLCache())
else
    project_deps_get(pkg) = Base.project_deps_get(Sys.STDLIB, pkg)
end

function get_compile_list()
    # Get a topologically sorted list of packages to compile
    pkgs = String[]
    for pkg in readdir(Sys.STDLIB)
        id = project_deps_get(pkg)
        id === nothing && continue
        Base.root_module_exists(id) && continue # Already loaded, this is a stdlib library.
        add_compile_pkg(pkgs, pkg)
    end
    return pkgs
end

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

function check_already_compiled(binpath, name)
    # This assume the precompiled file to exist as long as the directory exists
    # and also assumes there isn't any name conflicts between packages.
    # Ideally we would also check the time stamp and the `.archpkg` file.
    # Should be good enough for now
    path = joinpath(binpath, "compiled", "v$(VERSION.major).$(VERSION.minor)")
    return isdir(path)
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

function precompile(binpath)
    compiled = Set{String}()
    insert!(Base.DEPOT_PATH, 1, binpath)
    resize!(Base.DEPOT_PATH, 1)
    Core.eval(Base, :(is_interactive = true))
    for pkg in get_compile_list()
        pkg in compiled && continue
        if check_already_compiled(binpath, pkg)
            push!(compiled, pkg)
            continue
        end
        path = check_src(pkg)
        path === nothing && continue
        id = project_deps_get(pkg)
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
