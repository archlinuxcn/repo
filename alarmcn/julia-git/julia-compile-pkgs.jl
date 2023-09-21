#!/usr/bin/julia

using Pkg

const stdlib_dir = get(ENV, "JULIA_PRECOMPILE_STDLIB_DIR", Sys.STDLIB)

struct PkgInfo
    id::Base.PkgId
    src::String
    deps::Vector{String}
    exts::Dict{String,PkgInfo}
    parent::Union{Base.PkgId,Nothing}
end

function ext_pkg_info(stdlib_dir, parent_id, package, depends)
    if !(depends isa String || depends isa Vector{String})
        return
    end
    id = Base.uuid5(parent_id.uuid, package)
    src = joinpath(stdlib_dir, parent_id.name, "ext", "$package.jl")
    isfile(src) || return
    depends = [depends; parent_id.name]
    return PkgInfo(Base.PkgId(id, package), src,
                   depends, Dict{String,PkgInfo}(), parent_id)
end

function pkg_info(stdlib_dir, pkg, d)
    uuid = get(d, "uuid", nothing)
    if uuid === nothing
        return
    end
    id = Base.PkgId(Base.UUID(uuid), pkg)
    src = joinpath(stdlib_dir, "$pkg.jl")
    if !isfile(src)
        src = joinpath(stdlib_dir, pkg, "src", "$pkg.jl")
        isfile(src) || return
    end
    deps = get(d, "deps", nothing)
    if deps isa Dict{String, Any}
        deps = collect(keys(deps))
    elseif !(deps isa Vector{String})
        deps = String[]
    end
    exts = Dict{String,PkgInfo}()
    extensions = get(d, "extensions", nothing)
    if extensions isa Dict{String,Any}
        for (k, v) in extensions
            ext_info = ext_pkg_info(stdlib_dir, id, k, v)
            if ext_info !== nothing
                exts[k] = ext_info
            end
        end
    end
    return PkgInfo(id, src, deps, exts, nothing)
end

function load_pkg_info(stdlib_dir)
    packages = Dict{String,PkgInfo}()
    for pkg in readdir(stdlib_dir)
        pkgdir = joinpath(stdlib_dir, pkg)
        for p in ("JuliaProject.toml", "Project.toml")
            projfile = joinpath(pkgdir, p)
            isfile(projfile) || continue
            d = Base.parsed_toml(projfile)
            info = pkg_info(stdlib_dir, pkg, d)
            if info === nothing
                continue
            end
            packages[pkg] = info
            break
        end
    end
    return packages
end

function check_src(src)
    # Use a heuristic similar to `Pkg.jl` for now.
    # If it is really an issue we could put a tag file in the package that doesn't
    # want precompilation or even patch the affected package in PKGBUILD.
    return !occursin(r"\b__precompile__\(\s*false\s*\)", read(src, String))
end

mutable struct WorkItem
    const id::Base.PkgId
    const src::String
    ndepends::Int
    const dependents::Vector{WorkItem}
end

struct WorkQueue
    blocked::Set{WorkItem}
    free::Set{WorkItem}
    done::Set{WorkItem}
    function WorkQueue(pkg_infos)
        item_map = Dict{PkgInfo,WorkItem}()
        function get_work_item(info)
            # Already loaded, this is a builtin library.
            Base.root_module_exists(info.id) && return true
            check_src(info.src) || return false
            if info in keys(item_map)
                return item_map[info]
            end
            work = WorkItem(info.id, info.src, 0, WorkItem[])
            for dep in info.deps
                # As of now, extensions are never in the dependencies
                # so we should be able to find everything
                # in the top-level infos dict.
                dep_info = get(pkg_infos, dep, nothing)
                if dep_info === nothing
                    return false
                end
                dep_work = get_work_item(dep_info)
                if dep_work === false
                    return false
                end
                if dep_work === true
                    continue
                end
                work.ndepends += 1
                push!(dep_work.dependents, work)
            end
            item_map[info] = work
            return work
        end
        for (name, info) in pkg_infos
            get_work_item(info)
            for (ext_name, ext_info) in info.exts
                get_work_item(ext_info)
            end
        end
        blocked = Set{WorkItem}()
        free = Set{WorkItem}()
        for (info, work) in item_map
            push!(work.ndepends == 0 ? free : blocked, work)
        end
        return new(blocked, free, Set{WorkItem}())
    end
end

function check_already_compiled(binpath, name)
    # This assume the precompiled file to exist as long as the directory exists
    # and also assumes there isn't any name conflicts between packages.
    # Ideally we would also check the time stamp and the `.archpkg` file.
    # Should be good enough for now
    path = joinpath(binpath, "compiled", "v$(VERSION.major).$(VERSION.minor)", name)
    return isdir(path)
end

function compile_one(work_queue, binpath)
    work = pop!(work_queue.free)
    do_log = true
    if !check_already_compiled(binpath, work.id.name)
        try
            Base.compilecache(work.id, work.src)
        catch e
            @show e
        end
    elseif isfile(joinpath(binpath, "compiled", "v$(VERSION.major).$(VERSION.minor)",
                           work.id.name, ".archpkg"))
        do_log = false
    else
        @info "Not touching compiled cache for $(work.id)"
    end
    push!(work_queue.done, work)
    for dep_work in work.dependents
        dep_work.ndepends -= 1
        if dep_work.ndepends == 0
            delete!(work_queue.blocked, dep_work)
            push!(work_queue.free, dep_work)
        end
    end
    if do_log
        @info "Finished: $(length(work_queue.done)); Pending: $(length(work_queue.blocked) + length(work_queue.free))"
    end
end

function compile_available(work_queue, binpath)
    while !isempty(work_queue.free)
        compile_one(work_queue, binpath)
    end
end

const work_queue = WorkQueue(load_pkg_info(stdlib_dir))

function precompile(work_queue, binpath)
    @info "Pending packages: $(length(work_queue.blocked) + length(work_queue.free))"
    compiled = Set{String}()
    insert!(Base.DEPOT_PATH, 1, binpath)
    resize!(Base.DEPOT_PATH, 1)
    Core.eval(Base, :(is_interactive = true))
    compile_available(work_queue, binpath)
    @assert isempty(work_queue.free)
    if !isempty(work_queue.blocked)
        @warn "Dependency tracking failed for $([work.id for work in work_queue.blocked])"
    end
    Core.eval(Base, :(is_interactive = false))
    @info "Done package precompilation"
end

precompile(work_queue, ARGS[1])
