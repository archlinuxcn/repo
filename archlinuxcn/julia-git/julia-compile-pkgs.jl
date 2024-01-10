#!/usr/bin/julia

const stdlib_dir = get(ENV, "JULIA_PRECOMPILE_STDLIB_DIR", Sys.STDLIB)

const PkgId = Base.PkgId

struct PkgInfo
    id::PkgId
    src::String
    deps::Vector{PkgId}
    exts::Vector{PkgInfo}
    parent::Union{PkgId,Nothing}
end

function ext_pkg_info(stdlib_dir, parent_pkgid, name, depends)
    id = Base.uuid5(parent_pkgid.uuid, name)
    src = joinpath(stdlib_dir, parent_pkgid.name, "ext", "$name.jl")
    isfile(src) || return
    depends = [depends; parent_pkgid]
    return PkgInfo(PkgId(id, name), src, depends, PkgInfo[], parent_pkgid)
end

function try_add_to_uuid_map!(uuid_map, d)
    if d isa Dict{String, Any}
        for (name, uuid) in d
            try
                uuid_map[name] = Base.UUID(uuid)
            catch
            end
        end
    end
end

function name_to_uuid_map(d)
    uuid_map = Dict{String,Base.UUID}()
    try_add_to_uuid_map!(uuid_map, get(d, "deps", nothing))
    try_add_to_uuid_map!(uuid_map, get(d, "extras", nothing))
    try_add_to_uuid_map!(uuid_map, get(d, "weakdeps", nothing))
    return uuid_map
end

function pkg_info(stdlib_dir, name, d)
    uuid = get(d, "uuid", nothing)
    if uuid === nothing
        return
    end
    id = PkgId(Base.UUID(uuid), name)
    src = joinpath(stdlib_dir, "$name.jl")
    if !isfile(src)
        src = joinpath(stdlib_dir, name, "src", "$name.jl")
        isfile(src) || return
    end
    uuid_map = name_to_uuid_map(d)
    deps = get(d, "deps", nothing)
    if deps isa Dict{String, Any}
        deps = [PkgId(Base.UUID(uuid), name) for (name, uuid) in deps]
    elseif deps isa Vector{String}
        deps = [PkgId(uuid_map[name], name) for name in deps]
    else
        deps = PkgId[]
    end
    exts = PkgInfo[]
    extensions = get(d, "extensions", nothing)
    if extensions isa Dict{String,Any}
        for (k, v) in extensions
            ext_info = ext_pkg_info(stdlib_dir, id, k,
                                    isa(v, AbstractString) ? PkgId(uuid_map[v], v) :
                                        [PkgId(uuid_map[name], name) for name in v])
            if ext_info !== nothing
                push!(exts, ext_info)
            end
        end
    end
    return PkgInfo(id, src, deps, exts, nothing)
end

function load_pkg_info(stdlib_dir)
    @info "Loading package info from $stdlib_dir"
    packages = Dict{PkgId,PkgInfo}()
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
            packages[info.id] = info
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
    const id::PkgId
    const src::String
    ndepends::Int
    const dependents::Vector{WorkItem}
end

mutable struct WorkQueue
    const blocked::Set{WorkItem}
    const free::Set{WorkItem}
    const done::Set{WorkItem}
    skipped::Int
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
        for (pkgid, info) in pkg_infos
            get_work_item(info)
            for ext_info in info.exts
                get_work_item(ext_info)
            end
        end
        blocked = Set{WorkItem}()
        free = Set{WorkItem}()
        for (info, work) in item_map
            push!(work.ndepends == 0 ? free : blocked, work)
        end
        return new(blocked, free, Set{WorkItem}(), 0)
    end
end

function check_already_compiled(pkg)
    entrypath, entryfile = Base.cache_file_entry(pkg)
    path = joinpath(Base.DEPOT_PATH[1], entrypath)
    if !isdir(path)
        return false, true
    end
    for file in readdir(path, sort = false) # no sort given we sort later
        if !((pkg.uuid === nothing && file == entryfile * ".ji") ||
            (pkg.uuid !== nothing && startswith(file, entryfile * "_") &&
            endswith(file, ".ji")))
            continue
        end
        filepath = joinpath(path, file)
        if !isfile(filepath)
            continue
        end
        if Base.isprecompiled(pkg, ignore_loaded=true, cachepaths=[filepath])
            if pkg.uuid === nothing
                return true, true
            end
            try
                if islink(filepath) && contains(readlink(filepath), "/arch-compiled/")
                    return true, false
                end
                cachedir = dirname(filepath)
                if isfile(joinpath(cachedir, ".archpkg"))
                    return true, false
                end
            catch e
                @warn "Error checking compiled cache for $(pkg): $(e)"
                return true, true
            end
            return true, true
        end
    end
    return false, true
end

function compile_one(work_queue)
    work = pop!(work_queue.free)
    compiled, do_log = check_already_compiled(work.id)
    if !compiled
        try
            Base.compilecache(work.id, work.src)
        catch e
            @show e
        end
    else
        work_queue.skipped += 1
        if do_log
            @info "Not touching compiled cache for $(work.id)"
        end
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
        @info "Finished: $(length(work_queue.done)); Pending: $(length(work_queue.blocked) + length(work_queue.free)); Skipped: $(work_queue.skipped)"
    end
end

function compile_available(work_queue)
    while !isempty(work_queue.free)
        compile_one(work_queue)
    end
end

const work_queue = WorkQueue(load_pkg_info(stdlib_dir))

function precompile(work_queue, binpath)
    @info "Pending packages: $(length(work_queue.blocked) + length(work_queue.free))"
    compiled = Set{String}()
    insert!(Base.DEPOT_PATH, 1, binpath)
    resize!(Base.DEPOT_PATH, 1)
    Core.eval(Base, :(is_interactive = true))
    try
        compile_available(work_queue)
        @assert isempty(work_queue.free)
        if !isempty(work_queue.blocked)
            @warn "Dependency tracking failed for $([work.id for work in work_queue.blocked])"
        end
    catch e
        @warn "Error during precompilation: $e"
    end
    Core.eval(Base, :(is_interactive = false))
    @info "Done package precompilation"
end

precompile(work_queue, ARGS[1])
