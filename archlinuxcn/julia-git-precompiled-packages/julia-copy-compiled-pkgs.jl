#!/usr/bin/julia

struct PkgInfo
    name::String
    syntax_ver::VersionNumber
    sources::Dict{String,String}
    deps::Vector{String}
    weakdeps::Vector{String}
end

const has_syntax_ver = isdefined(Base, :PkgLoadSpec)

@static if has_syntax_ver
    import Base: project_get_syntax_version, PkgLoadSpec
    stale_cachefile(src, syntax_ver, cachepath) =
        Base.stale_cachefile(PkgLoadSpec(src, syntax_ver), cachepath,
                             ignore_loaded=true)
else
    project_get_syntax_version(d) = VERSION
    stale_cachefile(src, syntax_ver, cachepath) =
        Base.stale_cachefile(src, cachepath, ignore_loaded=true)
end


function read_deps(d, field)
    deps = get(d, field, nothing)
    if deps isa Dict{String, Any}
        return [name for (name, uuid) in deps]
    elseif deps isa Vector{String}
        return deps
    else
        return String[]
    end
end

function pkg_info(srcdir, pkg, d)
    src = joinpath(srcdir, "src", "$pkg.jl")
    isfile(src) || return
    sources = Dict{String,String}(pkg=>src)
    extensions = get(d, "extensions", nothing)
    if extensions isa Dict{String,Any}
        for (k, v) in extensions
            extsrc = joinpath(srcdir, "ext", "$(k).jl")
            if !isfile(extsrc)
                extsrc = joinpath(srcdir, "ext", k, "$(k).jl")
                isfile(extsrc) || continue
            end
            sources[k] = extsrc
        end
    end
    deps = read_deps(d, "deps")
    weakdeps = read_deps(d, "weakdeps")
    setdiff!(deps, weakdeps)
    return PkgInfo(pkg, project_get_syntax_version(d), sources, deps, weakdeps)
end

function get_pkginfo(stdlib_dir, pkg)
    srcdir = joinpath(stdlib_dir, pkg)
    for p in ("JuliaProject.toml", "Project.toml")
        projfile = joinpath(srcdir, p)
        isfile(projfile) || continue
        d = Base.parsed_toml(projfile)
        info = pkg_info(srcdir, pkg, d)
        if info === nothing
            continue
        end
        return info
    end
    return
end

function copy_pkg_cache_for_src(name, syntax_ver, src, compiled_dir, pkg_tgt_dir)
    pkgcache_dir = joinpath(compiled_dir, name)
    if !isdir(pkgcache_dir)
        return
    end
    for file in readdir(pkgcache_dir)
        endswith(file, ".ji") || continue
        cachepath = joinpath(pkgcache_dir, file)
        if stale_cachefile(src, syntax_ver, cachepath) === true
            continue
        end
        mkpath(joinpath(pkg_tgt_dir, name))
        cp(cachepath, joinpath(pkg_tgt_dir, name, file), force=true)
        sofile = file[1:end-2] * "so"
        sopath = joinpath(pkgcache_dir, sofile)
        if isfile(sopath)
            cp(sopath, joinpath(pkg_tgt_dir, name, sofile), force=true)
        end
    end
end

function write_arch_deps(io, deps, name)
    if isempty(deps)
        return
    end
    print(io, "$(name)+=(")
    isfirst = true
    for dep in deps
        if isfirst
            isfirst = false
        else
            print(io, " ")
        end
        print(io, "julia-git-$(lowercase(dep))")
    end
    println(io, ")")
    return
end

function copy_pkg_cache(info, compiled_dir, tgt_dir)
    pkg_tgt_dir = joinpath(tgt_dir, info.name)
    mkpath(pkg_tgt_dir)
    for (pkg, src) in info.sources
        copy_pkg_cache_for_src(pkg, info.syntax_ver, src, compiled_dir, pkg_tgt_dir)
    end
    open(joinpath(tgt_dir, "package-$(info.name)_vars.sh"), "w") do io
        write_arch_deps(io, info.deps, "depends")
        write_arch_deps(io, info.weakdeps, "optdepends")
    end
end

const stdlib_dir = ARGS[1]
const compiled_dir = ARGS[2]
const tgt_dir = ARGS[3]
const pkgnames = ARGS[4:end]

for name in pkgnames
    local info = get_pkginfo(stdlib_dir, name)
    if info === nothing
        error("Unable to load package $(name)")
    end
    copy_pkg_cache(info, compiled_dir, tgt_dir)
end
