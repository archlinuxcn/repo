module NodeJS

export nodejs_cmd, npm_cmd

function conditional_nodejs_load()
    return "/usr/"
end

const nodejs_path = conditional_nodejs_load()

const node_exe_name = "node"
const npm_exe_name = "npm"

const node_executable_path = "/usr/bin/node"
const npm_executable_path = "/usr/bin/npm"

"""
Return the full path of the node command.
"""
function nodejs_cmd()
    return `/usr/bin/node`
end

"""
Return the full path of the npm command.
"""
function npm_cmd()
    return `/usr/bin/npm`
end

end # module
